# ============================================================
# How to Tinker with Code
# ============================================================
# The point of this activity is not to get everything right on the first try.
# The point is to notice patterns, test ideas, and learn from what happens.
#
# Try this routine at every section:
# 1. Predict what will happen before you run the code.
# 2. Set a breakpoint or add a print statement.
# 3. Change one small thing and rerun.
# 4. Compare your prediction to the actual result.
# 5. Ask: "What changed, and why?"
#
# Helpful questions:
# - What value is this variable holding right now?
# - What line is running next?
# - Which branch of the if statement is being chosen?
# - What happens when I change a number, a condition, or a loop range?
#
# Breakpoints help you pause and inspect.
# Print statements help you track values while the program runs.
# Neither one is "the answer"; they are just tools for exploration.
#
# Exploration mindset:
# - It is okay to be wrong.
# - A surprising result is a clue, not a failure.
# - Try one change at a time.
# - If the output changes, ask why.
#
# Mini challenge:
# Pick one variable in this file and change it.
# Then answer: What did I expect? What actually happened? Why?
# ============================================================


# ------------------------------------------------------------
# Part 1: Predict, Pause, and Inspect
# ------------------------------------------------------------
# Prediction challenge:
# Before you run, predict what this loop will print.
# Then use a breakpoint on the if statement and inspect num and even_count.
# Change one number in the list and run again.
numbers = [2, 4, 5, 7, 8, 10, 13]
even_count = 0

for num in numbers:
    # Breakpoint idea: pause here and inspect the value of num.
    # Print idea: print(f"Before check: num={num}, even_count={even_count}")
    if num % 2 == 0:
        even_count += 1

print("Even numbers found:", even_count)
# Tinker ideas:
# - Change one number in the list to an odd number.
# - Change the condition from % 2 == 0 to % 2 == 1.
# - Change the starting value of even_count.
# - Add a new number to the list.


# ------------------------------------------------------------
# Part 2: Function Tinkering
# ------------------------------------------------------------
# Prediction challenge:
# Before running, predict the output of the function calls below.
# Then place a breakpoint inside calculate_total() and inspect total.
# Try changing the numbers and the math operation.
def calculate_total(a, b):
    total = a + b
    # Breakpoint idea: pause here and inspect a, b, and total.
    # Print idea: print(f"Inside function: a={a}, b={b}, total={total}")
    return total

x = 6
y = 9

result = calculate_total(x, y)
print("Total:", result)
# Tinker ideas:
# - Change x and y to new values.
# - Change the + to * or - inside the function.
# - Add a third value and update the function call.
# - Add a print statement to show the function inputs before the calculation.


# ------------------------------------------------------------
# Part 3: Condition Testing
# ------------------------------------------------------------
# Prediction challenge:
# What happens when x > y, when x == y, and when x < y?
# Put a breakpoint on the if statement and watch which branch runs.
# Then change values and rerun.
x = 12
y = 8

if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x")
# Tinker ideas:
# - Change x and y to other values.
# - Add a third variable and compare more than two values.
# - Try changing > to >= and notice the difference.
# - Add print statements before each branch to show which condition is being checked.


# ------------------------------------------------------------
# Part 4: Loop Investigation
# ------------------------------------------------------------
# Prediction challenge:
# Before running, guess what the final value of total will be.
# Use a breakpoint inside the loop to inspect score and total.
# Try changing the numbers in the list and see how the output changes.
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total = total + score
    # Breakpoint idea: pause here and inspect the current score and total.
    # Print idea: print(f"score={score}, running total={total}")

print("Final total:", total)
print("Average:", total / len(scores))
# Tinker ideas:
# - Add a new score to the list.
# - Change one score to a much larger or smaller value.
# - Change total = total + score to total = total - score.
# - Print the index as you loop so you can track position in the list.


# ------------------------------------------------------------
# Part 5: Looking Inside a Dictionary
# ------------------------------------------------------------
# Prediction challenge:
# What will the program print for each student?
# Add a breakpoint inside the loop and inspect name and scores.
# Then try changing one student's list or adding a new student.
students = {
    "Ada": [98, 91, 87],
    "Ben": [72, 68, 75],
    "Chloe": [100, 94, 99],
}

for name, scores in students.items():
    average = sum(scores) / len(scores)
    # Breakpoint idea: pause here and inspect name, scores, and average.
    # Print idea: print(f"{name}: scores={scores}, average={average}")
    print(f"{name} average: {average:.1f}")
# Tinker ideas:
# - Add a new student to the dictionary.
# - Change one score in a list.
# - Print the length of each list.
# - Change how average is calculated, such as rounding or using a different formula.


# ------------------------------------------------------------
# Part 6: Debugging Challenge
# ------------------------------------------------------------
# This section contains a small bug on purpose.
# Your job is not to fix it instantly. Your job is to investigate.
# Use a breakpoint and print statements to discover what is happening.
# Then try changing one thing to see whether the behavior changes.
transactions = [100, -35, -40, -80, 50]
balance = 200

for transaction in transactions:
    print(f"Before transaction: balance={balance}, transaction={transaction}")
    if transaction > 0:
        balance = balance - transaction
    else:
        balance = balance + transaction
    print(f"After transaction: balance={balance}")

print("Final balance:", balance)
# Tinker ideas:
# - Change the initial balance.
# - Change one transaction to a larger value.
# - Change the if condition to test different logic.
# - Add a print statement to show whether the code is taking the if or else branch.


# ------------------------------------------------------------
# Part 7: Your Turn to Tinker
# ------------------------------------------------------------
# Try making your own small experiment.
# Choose one idea from the list below and change the code.
# Then explain what happened.
#
# Possible experiments:
# - Change one number and rerun.
# - Change a comparison operator such as > to <.
# - Add a new item to a list.
# - Add a print statement to track a variable.
# - Change a loop to iterate a different number of times.
# - Add a breakpoint in a new location to check the program state.

print("\nTinkering complete. What did you discover?")