n = int(input())

expenses = list( map(int, input().split()))

Limit = int(input())

max_streak = 0
current_streak = 0

for expense in expenses:
    if expense < Limit:

        current_streak += 1
        max_streak = max( max_streak,current_streak)
        
    else:
        current_streak = 0
print(max_streak)        