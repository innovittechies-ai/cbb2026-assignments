# Festival Crowd Panic

n = int(input("Number of entries"))

events = []

for i in range(n):
    entry, exit = map(int, input("Enter entry and exit time").split())
    events.append((entry, 1))   # entry increases crowd
    events.append((exit, -1))   # exit decreases crowd

# Sort all events by time
events.sort()

current_crowd = 0
max_crowd = 0

for time, change in events: # iterate through sorted events
    current_crowd += change # update current crowd based on entry or exit
    if current_crowd > max_crowd: #
        max_crowd = current_crowd
print(max_crowd)

    