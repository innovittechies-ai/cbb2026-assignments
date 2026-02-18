
# Rohit's expense discipline challenge
#  the number of days recorded
n = int(input("Enter the number of days recorded: "))

# the daily expenses
expenses = list(map(int, input("Enter the daily expenses separated by spaces: ").split()))

# the spending limit
limit = int(input("Enter your daily spending limit: "))

max_streak = 0
current_streak = 0

# Iterate through each expense to find the longest streak under the limit
for e in expenses:
    if e < limit:
        current_streak += 1
        # Update the max_streak if the current one is longer
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        # Reset the streak if an expense hits or exceeds the limit
        current_streak = 0

# Output the longest streak found
print("The longest streak of staying under the limit is:", max_streak, "days")