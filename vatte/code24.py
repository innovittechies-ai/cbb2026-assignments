#The Food Delivery Route Optimizer
# Ask for the total number of locations/points
n_input = input("Enter the number of points to check: ")
n = int(n_input)

# Check if we have at least two points to find a difference
if n < 2:
    print("You need at least two points to find a difference.")
else:
    # Ask for the distances or coordinates separated by spaces
    dist_input = input("Enter the point values separated by spaces: ")
    dist = list(map(int, dist_input.split()))

    # Sort the list so that the closest values are adjacent
    dist.sort()
    
    # Initialize with a very large number
    # float('inf') is standard, but you could also use dist[1] - dist[0]
    min_diff = float('inf')

    # Compare each pair of neighbors
    for i in range(1, n):
        diff = dist[i] - dist[i-1]
        if diff < min_diff:
            min_diff = diff

    print("The minimum difference between any two points is:", min_diff)