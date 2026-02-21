n = int(input()) 

arr = [int(input()) for i in range(n)] 
# Reading array elements
 
free_space = 0 
max_count = 0
 
# Traversing through array elements
for num in arr: 
    if num ==0: 
        # If element is zero, increase free_space count
        free_space += 1  
        # Update max_count with maximum of max_count and free_space
        max_count = max (max_count , free_space) 
        # Else reset free_space count
    else: 
        free_space = 0

print("output :", max_count)             