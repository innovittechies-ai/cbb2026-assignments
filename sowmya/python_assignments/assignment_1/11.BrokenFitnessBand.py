N = int(input())
# Read N integers from a single line
steps_per_hour = list(map(int, input().split()))
abnormal_hours= []
for i in range(5, N):
    prev_sum = steps_per_hour[i-5]+steps_per_hour[i-4]+steps_per_hour[i-3] + steps_per_hour[i-2] + steps_per_hour[i-1]
    avg = prev_sum / 5
    if steps_per_hour[i] > 2 * avg:
       abnormal_hours.append(i)
if abnormal_hours:
    for index in abnormal_hours:
        print(index)
else:
    print("No abnormal hours")