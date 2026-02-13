n= int(input())  # Read number of requests
  
request_count = {} # store the count of requests for each (user_id, minute) pair

violations = set() # store the user_ids which are violating the rule
 
# Loop through all requests
for i in range ( n ): 
    
    # Read user_id and minute
    user_id , minute = map ( int, input().spit()) 
    # Create a key from user_id and minute
    key = (user_id , minute)
    # Increment the count of requests for this key
    request_count[key] = request_count.get(key,0) +1 
    if request_count[key] > 3: # If count of requests for this key is greater than 3,
        # add user_id to violations
        violations.add(user_id)

if violations:      # If violations set is not empty
        
    for user_id in sorted(violations): 
        # Print user_ids in sorted order
        print(user_id)
else: 
    # If violations set is empty
    print('no violations')          