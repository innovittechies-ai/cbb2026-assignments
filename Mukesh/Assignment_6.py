n = int(input())

usage = list (map ( int, input().split()))

spikes = []

for i in range ( 3, n):
    avg_prev_3 = (usage[i-1] + usage[i-2] + usage[i-3])/3

    if usage[i] > 2*avg_prev_3 :
        spikes.append(i)

if spikes:
    print(*spikes)

else:
    print(" no spikes")            