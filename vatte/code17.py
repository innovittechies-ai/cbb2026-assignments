#The Delivery Van Marathon 
# Ask for the total number of segments or distances
n = int(input("Enter the number of distance segments to sum up: "))

# user  input each distance value separated by a space
distances = list(map(float, input("Enter each distance value separated by a space: ").split()))

# Calculate the total distance
total_distance = sum(distances)

# Print the result with a descriptive message
print("The total calculated distance is:", total_distance)