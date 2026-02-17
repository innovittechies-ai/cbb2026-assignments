#The Midnight Ticket Scam
# Get the total number of booking records
n = int(input("Enter the total number of booking records: "))

bookings = {}
violators = []

# Process each booking entry
for i in range(n):
    # Read the user ID and hour from input
    line = input(f"Enter record {i+1} (User ID and Hour): ").split()
    
    # Basic check to ensure the input has two parts
    if len(line) < 2:
        continue
        
    uid = line[0]
    hour = line[1]
    
    # Create a unique key for the user-hour combination
    key = (uid, hour)
    
    # Count occurrences of this specific user in this specific hour
    if key not in bookings:
        bookings[key] = 0
    bookings[key] += 1
    
    # If bookings exceed 5, add to violators list if not already there
    if bookings[key] > 5:
        if uid not in violators:
            violators.append(uid)

if not violators:
    print("No violations")
else:
    print("Users violating the booking limit:")
    for v in violators:
        print(v)