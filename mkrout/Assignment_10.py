n = int(input())

calls = list (map (int, input().split()))

calls.sort()

waiting_time = 0
total_wait = 0

for  duration in calls:
    total_wait += waiting_time
    waiting_time+=duration

print( (total_wait//n))
