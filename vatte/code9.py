# Get the number of entries
n_str = input("Enter the number of log entries: ")
n = int(n_str)

requests = {}
violators = []

for i in range(n):
    # Prompting for user data
    data = input(f"Enter entry {i+1} (UserID Minute): ")
    parts = data.split()
    
    # Basic validation to prevent errors if input is malformed
    if len(parts) < 2:
        continue
        
    user_id = parts[0]
    minute = parts[1]
    
    key = (user_id, minute)
    
    # Tracking request counts
    if key not in requests:
        requests[key] = 1
    else:
        requests[key] += 1
    
    # Check for violation (more than 3 requests)
    if requests[key] > 3:
        if user_id not in violators:
            violators.append(user_id)

# Output
print("\n--- Results ---")
if not violators:
    print("No violations")
else:
    for v in violators:
        print(v)