# Autoscaling Decisin Engine

n = int(input("Enter number of traffic logs: ")) 
traffic_sequence = list(map(int, input("Enter traffic sequence: ").split())) #input traffic sequence list

max_len = 1
current_len = 1

for i in range(1, len(traffic_sequence)): # iterate through traffic sequence to find longest increasing consecutive sequence
    if traffic_sequence[i] > traffic_sequence[i - 1]: # check if current traffic is greater than previous traffic
        current_len += 1 # increase current length of increasing sequence
        max_len = max(max_len, current_len) # update max lenth of increasing sequence
    else:
        current_len = 1

print("Longest increasing consecutive sequence length:", max_len)



