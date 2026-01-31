l = int(input("Enter number of lanes: "))
vehicles = list(map(int, input("Enter vehicle count per lane: ").split()))
total_vehicles = sum(vehicles)
green_times = [v * 120 // total_vehicles for v in vehicles]
print(*green_times)
