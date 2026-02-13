n = int ( input()) # Read number of records

suspicious = [] # store all user_ids who are suspicious
 
# Loop through all records
for i in range (n):  
    # Read user_id, distance, time and calculate speed
    user_id, distance, time = map(int, input().split())
    
    speed = distance / time # Calculate 

    # If speed is greater than 900, add user to suspicious list
    if speed > 900:
        suspicious.append(user_id)
 
# Print all suspicious users
if suspicious:  # If suspicious list is not empty
    suspicious.sort() # Sort suspicious users
    for user in suspicious:       
        print(user) 
 
else: 
    # If suspicious list is empty
    print("no suspicious user")                