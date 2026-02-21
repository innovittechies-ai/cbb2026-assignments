#The Cyber Attack Window
# Read N (total packets), K (window size), and S (threshold sum)
line1 = input("Enter N (total), K (window size), and S (limit) separated by spaces: ").split()

# Ensure we have enough inputs before unpacking
if len(line1) >= 3:
    n = int(line1[0])
    k = int(line1[1])
    s = int(line1[2])

    # Read the N packet values
    packets = list(map(int, input(f"Enter the {n} packet sizes separated by spaces: ").split()))
    found = False

    # Check if a window of size K exists
    if k <= n:
        # Loop through the packets to check each consecutive window of size K
        for i in range(n - k + 1):
            # Calculate the sum of the current window
            window_sum = sum(packets[i : i+k])
            
            # If the sum exceeds the limit S, we found a violation
            if window_sum > s:
                found = True
                break

    
    if found:
        print("YES")
    else:
        print("NO")
else:
    print("Invalid input. Please provide N, K, and S.")