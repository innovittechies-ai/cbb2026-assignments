#the MORNING CALL CENTER RUSH
# Get the number of customers
n = int(input("Enter the number of customers: "))

# Get the duration of each call as a list
durations = list(map(int, input("Enter the call durations separated by spaces: ").split()))

# Sort durations to minimize waiting time (Shortest Job First)
durations.sort()

total_waiting_time = 0
current_wait = 0

# Calculate waiting time
# Each customer waits for the sum of all previous customers' durations
for i in range(n - 1):
    current_wait += durations[i]
    total_waiting_time += current_wait

# Calculate the average (using / for decimal precision or // for integer)
average_wait = total_waiting_time / n
print("The average waiting time is:", average_wait)