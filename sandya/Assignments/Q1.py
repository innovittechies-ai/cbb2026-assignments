N = int(input().strip())
total_minutes = 0

for _ in range(N):
    join_time, leave_time = map(int, input().strip().split())
    total_minutes += leave_time - join_time

print(total_minutes)
 
 
