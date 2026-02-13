total_attended_time=0
n=int(input())
for i in range(n):
    join_time=int(input())
    leave_time=int(input())
    print(join_time,' ',leave_time)
    duration=leave_time-join_time
    total_attended_time=total_attended_time+duration
print(total_attended_time)