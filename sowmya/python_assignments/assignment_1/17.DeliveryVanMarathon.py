N=int(input())
distance_travelled=list(map(int,input().split()))
total_distance_travelled=0
for distance in distance_travelled:
    total_distance_travelled += distance
print(total_distance_travelled)
