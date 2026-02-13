# The Smart Parking Sensor
n = int(input())
arr = list(map(int, input().split()))  # input parking spots

max_count = 0      # maximum consecutive zeros
current_count = 0  # current consecutive zeros

for num in arr:
    if num == 0:              # empty parking spot
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0     # reset if not zero

print(max_count)



 