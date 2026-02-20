#The Night Shift Server Logs 
# n = int(input())
# Ask for the total number of records to be checked
n = int(input("Enter the number of data points to analyze: "))

# Ask for the error values separated by spaces
errors = list(map(int, input("Enter the error values for each point separated by spaces: ").split()))

# Ask for the threshold value
t = int(input("Enter the threshold limit for an acceptable error: "))

max_streak = 0
current_streak = 0

# Scan through the errors to find the longest consecutive run below the threshold
for e in errors:
    if e < t:
        current_streak += 1
        # Update the maximum record if the current streak surpasses it
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        # Reset the current streak when an error hits or exceeds the threshold
        current_streak = 0

# Print the final result
print("The longest streak of values below the threshold is:", max_streak)