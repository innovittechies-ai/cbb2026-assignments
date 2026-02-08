# Read the number of segments
n = int(input("enter the value:"))
total_time = 0

for i in range(n):
    # Read join and leave time for each segment
    data = input().split()
    join_time = int(data[0])
    leave_time = int(data[1])
    
    # Calculate duration and add to total
    duration = leave_time - join_time
    total_time = total_time + duration

print(total_time)