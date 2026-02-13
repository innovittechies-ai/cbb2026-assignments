N=int(input())
expenses=list(map(int,input().split()))
limit=int(input())
current_streak_count=0
max_streak_count=0
current_streak_list = []
best_streak_list = []
#Iterate through expenses
for amount in expenses:
    if amount < limit:
        current_streak_list.append(amount)
        # If the current sequence is the longest we've seen, save it
        if len(current_streak_list) > max_streak_count:
            max_streak_count = len(current_streak_list)
            best_streak_list = list(current_streak_list) # Copy the list
    else:
        # Sequence broken: Clear the current list
        current_streak_list = []
print(max_streak_count)