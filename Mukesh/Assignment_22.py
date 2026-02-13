n = int(input())

traffic = list( map(int, input().split())) 
# Reading traffic data
 
# Initializing variables to track maximum increasing sequence
max_len = 1
current_len = 1
 
# Looping through traffic data starting from second element
for i in range(1,n): 
    # If current traffic is greater than previous traffic
    if traffic[i] > traffic[i-1]: 
        # Increment current sequence length
        current_len += 1 
        # Update max length if current length is greater
        max_len = max(max_len, current_len) 
    # Reset current length if traffic is not increasing
    else:
        current_len = 1
     
# Print maximum length of increasing sequence
print(max_len)        