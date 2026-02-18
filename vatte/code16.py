#festival crowd panic
# Get the number of people/events
n = int(input("Enter the total number of people attending the event: "))

events = []

for i in range(n):
    # Input : "entry_time exit_time"
    line = input(f"Enter entry and exit time for person {i+1}: ").split()
    entry = int(line[0])
    exit = int(line[1])
    
    # We create two events for each person: one for entry and one for exit.
    # If the problem states that the exit time is exclusive, you would use (exit, -1) as is.
    #
    events.append((entry, 1))   
    events.append((exit, -1))  
# We sort the events first by time, and then by type of event (entry before exit).   
# If times are equal, (-1) will come before (1) because -1 < 1.
# This ensures that if a person enters and another exits at the same time, the exiting person is counted as leaving before the entering person is counted as arriving.
events.sort()

max_crowd = 0
current_crowd = 0

# We iterate through the sorted events, updating the current crowd count based on whether it's an entry or exit event, and we keep track of the maximum crowd size at any point in time.
for time, change in events:
    current_crowd += change
    if current_crowd > max_crowd:
        max_crowd = current_crowd

print("The maximum number of people present at once was:", max_crowd)