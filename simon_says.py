import random
import time

COLORS = ["red", "blue", "green", "yellow"]


def show_pattern(pattern):
    print("\nWatch closely! Simon says:")
    for color in pattern:
        print(f"  {color.upper()}!")
        time.sleep(0.6)
        print("  ...")
        time.sleep(0.3)


def clean_guess(text):
    cleaned = text.lower().replace(",", " ")
    return cleaned.split()


def play_game():
    print("\n🎉 Welcome to Simon Says! 🎉")
    print("Simon will show you a pattern of colors.")
    print("You need to type the colors in the same order.")
    print("Example: red blue green")
    print("Type 'quit' anytime to stop playing.\n")

    pattern = []
    score = 0

    while True:
        pattern.append(random.choice(COLORS))
        show_pattern(pattern)

        guess = input("Your turn! Type the colors with spaces: ").strip()

        if guess.lower() == "quit":
            print(f"\nOkay! You made it to {score} point(s). See you next time!")
            break

        player_guess = clean_guess(guess)

        if player_guess == pattern:
            score += 1
            print(f"Nice job! You got {score} point(s).")
            print("Ready for another round!\n")
        else:
            print("\nOops! That was not the right pattern.")
            print(f"The correct pattern was: {' '.join(pattern)}")
            print(f"Your final score: {score}")
            print("Good try! Play again soon!\n")
            break


if __name__ == "__main__":
    play_game()
