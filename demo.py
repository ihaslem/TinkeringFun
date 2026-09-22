# ============================================================
# Quick lesson: How to tinker with code
# ============================================================
# 1. Predict what will happen before running.
# 2. Add a breakpoint or print statement.
# 3. Change one small thing.
# 4. Run again and compare.
# 5. Ask: What changed? Why?
#
# Breakpoints pause the program so you can inspect values.
# Print statements show values while the code runs.
# Both are tools for exploration.
#
# You do not need to understand everything right away.
# The goal is curiosity and experimentation.
# ============================================================


# ------------------------------------------------------------
# Demo 1: Counting a running total
# ------------------------------------------------------------
# Predict the final total before running.
# Add a breakpoint inside the loop and inspect current_value and running_total.
# Then change one item in the list and run again.
values = [10, 4*4, 21, 5, 8]
running_total = 0

for current_value in values:
    # Breakpoint idea: pause here and inspect current_value and running_total.
    # Print idea: print(f"current={current_value}, total={running_total}")
    running_total = running_total + current_value

print("Running total:", running_total)
# Try changing:
# - one value in the list
# - the operation to subtraction
# - add a new value at the end of the list


# ------------------------------------------------------------
# Demo 2: Temperature check
# ------------------------------------------------------------
# Predict which message will print.
# Place a breakpoint on the if statement and inspect temp and threshold.
def weather_message(temp):
    threshold = 70
    # Breakpoint idea: pause here and inspect temp and threshold.
    # Print idea: print(f"temp={temp}, threshold={threshold}")
    if temp >= threshold:
        return "Hot outside"
    return "Cool outside"

temperature = 59
print(weather_message(temperature))
# Try changing:
# - temperature to a different value
# - threshold to 60 or 80
# - change >= to >


# ------------------------------------------------------------
# Demo 3: Score categories
# ------------------------------------------------------------
# Predict which label will be printed.
# Add a breakpoint inside the if/elif/else flow and inspect score.
score = 85

if score >= 90:
    label = "A"
elif score >= 85:
    label = "Joe Mama"
elif score >= 80:
    label = "B"
elif score >= 70:
    label = "C"
else:
    label = "You're Cooked Kid"

print("Letter grade:", label)
# Try changing:
# - score to 89, 90, and 95
# - one cutoff value
# - add another category for 60 or 100

print("Demo complete. What did you notice?")