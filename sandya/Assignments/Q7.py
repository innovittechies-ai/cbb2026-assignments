#Midnight Power Spike
n = int(input("Enter number of hours: "))

hourly_usage = list(map(int, input("Enter hourly usage values: ").split()))
spikes = []

# start from index 3 because we need previous 3 hours
for i in range(3, n):
    average = (hourly_usage[i-1] +
               hourly_usage[i-2] +
               hourly_usage[i-3]) / 3

    if hourly_usage[i] > 2 * average:
        spikes.append(i)

if spikes:
    print(*spikes)
else:
    print("no spikes")
