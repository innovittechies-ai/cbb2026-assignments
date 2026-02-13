N = int(input())
# Read N integers from a single line
powerUsageList = list(map(int, input().split()))
spikes = []
# Start from index 3 to ensure there are 3 previous hours
for i in range(3, N):
    # Calculate sum and average of previous 3 hours
    prev_sum = powerUsageList[i-3] + powerUsageList[i-2] + powerUsageList[i-1]
    avg = prev_sum / 3
    # Check spike condition: usage > 2 * average
    if powerUsageList[i] > 2 * avg:
        spikes.append(i)
# Output formatting
if spikes:
    for index in spikes:
        print(index)
else:
    print("No spikes")