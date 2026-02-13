N=int(input())  # enter the number of lane
vehicles = []   # creating the empty list for storing number of vehicles  

for i in range(N): # iterating though the range of lane
    vehicles.append(int(input(f"enter number of vehicles in lane {i+1} :")))  # updating the empty list

tot_veh = sum(vehicles)  # suming up all the vehicles

g_time = []   # green time 
for v in vehicles:  # iterating through the list
    g_time.append((v * 120)/tot_veh)  # updating the g_time list (distribuiting the 120 sec in each lane respectively)

print(g_time)    