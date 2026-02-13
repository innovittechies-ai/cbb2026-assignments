n = int(input()) # Takes input n as total number of ticket booking records

# Dictionary to store count of bookings for each user_id and hour combination
booking_count = {} 

# Loop through all the records
for _ in range(n): 
    # Reading user_id and hour
    user_id, hour = map(int, input().split())
 
    # Creating key as tuple of user_id and hour
    key = (user_id, hour)
 
    # Incrementing count of bookings for this user_id and hour
    if key in booking_count:
        booking_count[key] += 1
    else: 
        booking_count[key] = 1

 
# Set to store all the violators
violators = set()   
  
# Loop through all the entries in dictionary
for key in booking_count: 
    # If count of bookings for this user_id and hour is greater than 5
    if booking_count[key] > 5:
        violators.add(key[0])   # key[0] is user_id
 
# Checking if any violators found 
if len(violators) > 0:   
    # Printing all the violators in sorted order
    violators = sorted(violators)   
    for user in violators:  # Loop through violators and print them
        print(user)
else: 
    # If no violators found
    print("No violations")
