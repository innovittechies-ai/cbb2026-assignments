# Get the number of time intervals recorded
n_input = input("Enter the total number of time intervals: ")
n = int(n_input)

# Check if there is enough data to make comparisons
if n < 2:
    if n == 1:
        # Ask for the single value anyway to keep the flow
        input("Enter the single time value: ")
    print("Not enough data to find spikes. Spikes found: 0")
else:
    # Get the time values as a list
    times_input = input("Enter the time values separated by spaces: ")
    times = list(map(int, times_input.split()))

    count = 0
    # Start the loop from the second element (index 1) 
    # so we can always look back at the previous one
    for i in range(1, n):
        # Logic: If the current time is more than double the previous time
        if times[i] > (2 * times[i-1]):
            count += 1

    print("Total number of significant spikes detected:", count)