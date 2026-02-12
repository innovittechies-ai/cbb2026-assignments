# Rohit's Expense Dicipline Challange
n = int(input("Enter number of days: ")) #input number of days

daily_expenses = list(map(int, input("Enter daily expenses: ").split())) #input daily expenses list
limit = int(input("Enter limit: "))#input limit for expenses

current_streak = 0# initialize current streak of days within limit 
max_streak = 0 #iterate through daily expenses to find longest streak of days within limit

for expense in daily_expenses: #iterate through daily expenses
    if expense <= limit:# check if expense is within limit
        current_streak += 1 # increase current streak
        max_streak = max(max_streak, current_streak) # update max streak
    else:
        current_streak = 0   # streak breaks

print(max_streak)
            


