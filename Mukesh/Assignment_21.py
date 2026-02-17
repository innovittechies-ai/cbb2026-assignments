n = int(input())

errors = list( map(int, input().split())) 
# Reading error codes

T = int(input()) 
# Reading threshold value
 
# Initializing variables to track maximum consecutive days
max_streak = 0
current_streak = 0
     
# Looping through errors
for e in errors: 
    if e > T: 
        # If error count is above threshold, increment current streak
        current_streak += 1 
        # Update max streak if current streak is greater
        max_streak = max( max_streak,current_streak) 
    else:
        current_streak = 0   # Reset current streak if error count is below threshold
print(max_streak)        