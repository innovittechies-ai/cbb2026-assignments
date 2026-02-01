Num_Lanes= int(input("Enter number of lanes: "))
vehicle_count_at_Lanes = list(map(int, input("Enter vehicle counts at lanes: ").split()))

total_vehicles = sum(vehicle_count_at_Lanes)
green_light_duration = []

for i in range(Num_Lanes):
    V1= vehicle_count_at_Lanes[i]   
    green_light_duration.append(float(V1/total_vehicles * 120))
    print(f"Lane {i+1} : {green_light_duration[i]} seconds")


