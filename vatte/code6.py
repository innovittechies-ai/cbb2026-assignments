#rahul teleporting login
n_str = input("Enter number of records: ")

# Check if n is a valid positive integer
if not n_str.strip().isdigit():
    print("Invalid input. Please enter a whole number.")
else:
    n = int(n_str)
    suspicious = []

    for i in range(n):
        line = input().split()
        
        #  Check for all 3 pieces of data
        if len(line) < 3:
            continue
            
        user_id = line[0]
        dist_str = line[1]
        time_str = line[2]

        #  Validate that distance and time are numeric 
        # (replace .isdigit() with a check that handles decimals if needed)
        if dist_str.replace('.', '', 1).isdigit() and time_str.replace('.', '', 1).isdigit():
            distance = float(dist_str)
            time = float(time_str)

            #  Check for Zero and  Speed Threshold
            if time > 0:
                if (distance / time) > 900:
                    suspicious.append(user_id)
        else:
            print(f"Skipping record for {user_id}: Invalid numeric data.")

    
    if len(suspicious) == 0:
        print("No suspicious users")
    else:
        # Using sorted(set()) ensures unique names in alphabetical order
        for user in sorted(set(suspicious)):
            print(user)