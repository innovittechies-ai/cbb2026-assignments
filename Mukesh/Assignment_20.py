n = int(input()) # takes n number of  input

expenses = list( map(int, input().split())) 
# Reading expense values

Limit = int(input()) 
# Reading spending limit
 
# Initializing variables to track maximum consecutive days
max_streak = 0 
current_streak = 0
 
# Looping through expenses
for expense in expenses: 
    if expense < Limit: 
        # If expense is under limit, increment current streak
        current_streak += 1 
        # Update max streak if current streak is greater
        max_streak = max( max_streak,current_streak)
         
    else: 
        current_streak = 0   # Reset current streak if expense exceeds limit
print(max_streak)        