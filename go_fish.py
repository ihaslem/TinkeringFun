import random
from collections import Counter

RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def build_deck():
    deck = []
    for rank in RANKS:
        for _ in range(4):
            deck.append(rank)
    random.shuffle(deck)
    return deck


def deal_hand(deck, size=5):
    hand = []
    for _ in range(size):
        if deck:
            hand.append(deck.pop())
    return hand


def remove_pairs(hand):
    counts = Counter(hand)
    leftover = []
    pairs_found = 0

    for rank, number_of_cards in counts.items():
        pairs_found += number_of_cards // 2
        leftover.extend([rank] * (number_of_cards % 2))

    return leftover, pairs_found


def show_hand(title, hand):
    if not hand:
        print(f"{title}: no cards left")
    else:
        print(f"{title}: {' '.join(hand)}")


def player_turn(deck, player_hand, computer_hand, score):
    if not player_hand and deck:
        player_hand.append(deck.pop())
        print("You had no cards, so you drew one.")

    if not player_hand:
        print("You are out of cards and the deck is empty.\n")
        return score, False

    show_hand("Your cards", player_hand)
    ask = input("Which number do you want to ask for? Pick 1 to 10: ").strip()

    while ask not in RANKS:
        print("Oops! Please pick a number from 1 to 10.")
        ask = input("Which number do you want to ask for? Pick 1 to 10: ").strip()

    matches = [card for card in computer_hand if card == ask]

    if matches:
        print(f"Nice! The computer gave you all of its {ask}s.")
        player_hand.extend(matches)
        computer_hand[:] = [card for card in computer_hand if card != ask]
    else:
        print("Nope! Go fish!")
        if deck:
            drawn = deck.pop()
            player_hand.append(drawn)
            print(f"You drew a {drawn}.")
        else:
            print("The deck is empty, so no card is left to draw.")

    player_hand, new_pairs = remove_pairs(player_hand)
    score += new_pairs
    print(f"You made {new_pairs} pair(s)! Your score is now {score}.\n")

    return score, True


def computer_turn(deck, player_hand, computer_hand, score):
    if not computer_hand and deck:
        computer_hand.append(deck.pop())

    if not computer_hand:
        print("The computer is out of cards and the deck is empty.\n")
        return score

    ask = random.choice(computer_hand)
    print(f"The computer asks for {ask}s.")

    matches = [card for card in player_hand if card == ask]

    if matches:
        print(f"You had {ask}s, so you gave them to the computer.")
        computer_hand.extend(matches)
        player_hand[:] = [card for card in player_hand if card != ask]
    else:
        print("The computer didn't get a match. Go fish!")
        if deck:
            drawn = deck.pop()
            computer_hand.append(drawn)
            print(f"The computer drew a {drawn}.")

    computer_hand, new_pairs = remove_pairs(computer_hand)
    score += new_pairs
    print(f"The computer made {new_pairs} pair(s)! The computer score is now {score}.\n")

    return score


def game_over(deck, player_hand, computer_hand):
    return not deck and not player_hand and not computer_hand


def play_game():
    print("\n🎴 Welcome to Go Fish! 🎴")
    print("Goal: make pairs of the same number.")
    print("If you ask for a number and someone has it, they give all of their cards with that number.")
    print("If they do not have it, you draw a card from the deck.")
    print("Every pair is worth 1 point.")
    print("Type numbers from 1 to 10 when you play.\n")

    deck = build_deck()
    player_hand = deal_hand(deck)
    computer_hand = deal_hand(deck)
    player_score = 0
    computer_score = 0

    while not game_over(deck, player_hand, computer_hand):
        player_score, ok = player_turn(deck, player_hand, computer_hand, player_score)
        if game_over(deck, player_hand, computer_hand):
            break

        if not ok:
            break

        computer_score = computer_turn(deck, player_hand, computer_hand, computer_score)

        if game_over(deck, player_hand, computer_hand):
            break

    print("\nGame over!")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print("You win! Great job!")
    elif computer_score > player_score:
        print("The computer wins this round. Try again!")
    else:
        print("It is a tie!")


if __name__ == "__main__":
    play_game()
