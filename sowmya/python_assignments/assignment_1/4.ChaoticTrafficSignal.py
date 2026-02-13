L=int(input())
total_vehicles=0
list=[]
green_times=[]
green_signal_time=120
for lane in range(L):
    veh_lane=int(input())
    list.append(veh_lane)
    total_vehicles=total_vehicles+veh_lane
for veh_lane in list:
    green_time_per_lane=((veh_lane/total_vehicles)*green_signal_time)
    green_times.append(green_time_per_lane)
print(green_times)