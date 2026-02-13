n = int(input()) # Input reading 
 
calls = list (map (int, input().split()))  
# Sort the calls based on their durations

calls.sort() # This arranges calls in increasing order (shortest first)

# Initialize variables
waiting_time = 0 
total_wait = 0
 
# Loop through each call
for  duration in calls: 
    total_wait += waiting_time 
    waiting_time += duration  


# Print the average waiting time
print( (total_wait//n))
