#The Smart Parking Sensor
# Ask for the total number of parking spots or data points
n_input = input("Enter the total number of parking spots to check: ")
n = int(n_input)

# Ask for the occupancy status (0 for empty, 1 for occupied)
spots_input = input("Enter the occupancy status (0s and 1s) separated by spaces: ")
spots = list(map(int, spots_input.split()))

max_zeros = 0
current_zeros = 0

# Loop through each spot to find the longest sequence of zeros
for s in spots:
    if s == 0:
        current_zeros += 1
        # Update max_zeros if the current streak is the new record
        if current_zeros > max_zeros:
            max_zeros = current_zeros
    else:
        # Reset current_zeros when we encounter an occupied spot
        current_zeros = 0

# Output the final result
print("The longest sequence of available (zero) spots is:", max_zeros)