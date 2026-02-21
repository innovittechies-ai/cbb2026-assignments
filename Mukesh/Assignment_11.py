n = int(input()) # Taking input n (number of hours)
 
steps = list ( map (int,input().split()))   # Reading steps data and converting into list
     
# Initializing empty list to store abnormal hours
abnormal = []
 
# Looping through steps list starting from 5th hour
for i in range ( 5, n ): 
    # Calculating average of previous 5 hours
    avg_prev_5 = sum(steps[i-5 : i] / 5)
    
    # Checking if current step count is more than twice the average
    if steps[i] > 2 * avg_prev_5: 
        # If yes, add the index to abnormal hours
        abnormal.append (i)  

  
if abnormal :  
    # If abnormal hours found
    for idx in abnormal: 
        # Loop through abnormal hours and print them
        print(idx)
else: 
    # If no abnormal hours found
    print('no abnormal hours')
    
                    