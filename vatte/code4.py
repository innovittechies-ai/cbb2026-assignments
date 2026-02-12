# Reading number of lanes (l)
l = int(input("enter the number of lanes: "))

# Reading number of vehicles in each lane
vehicles = list(map(int, input("enter the number of vehicles in each lane: ").split()))

total_vehicles = sum(vehicles)
green_times = []

# Logic to handle 120-second proportional split
if total_vehicles > 0:
    for v in vehicles:
        # Calculate time for each lane based on the proportion of vehicles
        time = (v * 120) // total_vehicles
        green_times.append(str(time))
elif l > 0: # Handle case where there are lanes but no vehicles
    # If no vehicles, split time equally among all lanes
    equal_time = 120 // l
    green_times = [str(equal_time)] * l
else:
    green_times = []

# Output the green times for each lane
print(" ".join(green_times))