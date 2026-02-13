n , k , s = map ( int, input().split(()))  # Reading n, k, s
arr = list( map ( int, input().split() ))    # Reading array elements
   
window_sum = sum(arr[:k])  # Sum of first window of size k
 
# Sliding window technique 
if window_sum > s: 
    print ("YES") 
  
else:  
    found = False   
    # Loop through remaining elements
    for i in range (k , n):  
        window_sum = window_sum - arr[i-k] + arr[i] # This is sliding window technique
                                                    # Remove element leaving window → arr[i - k]
                                                    # Add element entering window → arr[i]
        if window_sum > s:  # Check updated sum
            print("YES") 
            found = True
            break
    print("YES" if found else "NO")        


            
