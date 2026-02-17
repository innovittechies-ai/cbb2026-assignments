# The Night Shift Server Logs

n = int(input("Enter number of hours: "))

error_counts_perhour = list(
    map(int, input("Enter error counts per hour: ").split()) # input error counts for each hour as a list of integers
)

T = int(input("Enter T value: ")) #input threshold for error counts

current_streak = 0 # initialize current streak of hours with error counts below
max_streak = 0

for error in error_counts_perhour: # iterate through error counts for each hour
    if error < T: # check if error count is below threshold
        current_streak += 1 # increase current streak
        max_streak = max(max_streak, current_streak)# update max streak 
    else:
        current_streak = 0

print(max_streak)
