L = int(input("Enter number of lanes:"))
vehicles = list(map(int, input().split()))

total_vehicles = sum(vehicles)
green_time = []

for v in vehicles:
        green_time.append(int((v / total_vehicles) * 120))
print(green_time)
