n = int(input())

errors = list( map(int, input().split()))

T = int(input())

max_streak = 0
current_streak = 0

for e in errors:
    if e > T:
        current_streak += 1
        max_streak = max( max_streak,current_streak)
print(max_streak)        