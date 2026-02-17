n = int(input()) # Reads the number of hours N

usage = list (map ( int, input().split())) # Reads the power usage values in one line 
# breaks them into strings (input().split())
# converts them into integers ( map(int, ...)
# makes it a list (list)

spikes = []   # Stores indices where spikes occur

for i in range ( 3, n):   # Start from index 3, since we need at least 3 previous values
    # Calculate average of previous 3 hours
    avg_prev_3 = (usage[i-1] + usage[i-2] + usage[i-3])/3 
    
    # Check if current usage is more than double the average
    if usage[i] > 2*avg_prev_3 : 
        # If so, it's a spike. Add index to spikes list
        spikes.append(i) 

# Print the indices where spikes occur
if spikes: 
    # If spikes list is not empty
    print(*spikes)

else: 
    # If spikes list is empty
    print(" no spikes")            