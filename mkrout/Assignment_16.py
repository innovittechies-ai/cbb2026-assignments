n = int(input())

events = []

for i in range(n):
    entry , exit = map(int,input().split())
    events.append((entry,1))

    events.append((exit, -1))
    
events.sort(key=lambda x: (x[0], -x[1]))

current = 0
max_crowd = 0

for time, change in events:
    current += change
    max_crowd = max(max_crowd, current)

print(max_crowd)    