#midnight power spike 
n = int(input("Enter the number of data points: "))
usage = list(map(int, input("enter the usage values: ").split()))
spikes = []

# Starting from index 3 ensures we have at least 3 previous points to average
for i in range(3, n):
    prev_three = usage[i-3 : i]
    avg = sum(prev_three) / 3
    
    #  Check for spike: current usage is more than double the average of the previous three
    if avg > 0 and usage[i] > (2 * avg):
        spikes.append(str(i))
    elif avg == 0 and usage[i] > 0:
        # If the history was all 0s, any positive number its a spike
        spikes.append(str(i))

# Effective output handling
if not spikes:
    print("No spikes")
else:
    print(" ".join(spikes))