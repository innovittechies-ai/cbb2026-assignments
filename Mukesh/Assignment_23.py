n = int(input()) # takes n number of input

arr = list ( map ( int, input().split() ) ) 
# Reading array elements
   
current_sum = max_sum = arr[0]   
 
# Initializing current_sum and max_sum with first element
for i in range (1,n):
 
    # Either extend the existing subarray or start a new one
    current_sum = max(arr[i], current_sum + arr[i])
 
    # Update max_sum if current_sum is greater
    max_sum = max(max_sum, current_sum)
 
# Print the maximum sum of contiguous subarray
print(max_sum)    