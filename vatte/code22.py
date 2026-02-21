#Auto Scaling Decision Engine
# Ask for the number of time intervals recorded
n_input = input("Enter the number of traffic records: ")
n = int(n_input)

# Handle the case where there is no data
if n == 0:
    print("Longest increasing traffic streak: 0")
else:
    # Get the traffic counts as a list
    traffic_input = input("Enter the traffic counts separated by spaces: ")
    traffic = list(map(int, traffic_input.split()))

    max_len = 1
    current_len = 1
    
    # Iterate through the list starting from the second element
    for i in range(1, n):
        # Check if traffic is strictly increasing
        if traffic[i] > traffic[i-1]:
            current_len += 1
            # Update max_len if the current streak is the new record
            if current_len > max_len:
                max_len = current_len
        else:
            # Reset current streak if traffic stays the same or decreases
            current_len = 1
            
    print("The length of the longest increasing traffic sequence is:", max_len)