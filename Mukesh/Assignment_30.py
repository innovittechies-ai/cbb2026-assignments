n= int(input())

ranks = list(map(int, input().split()))

sorted_rank = sorted(ranks)

diff = []

for i in range (n):
    if ranks[i] != sorted_rank[i] :
        diff.append(i)

if len(diff) == 0 or len(diff) == 2:
    print("yes")
else:
    print("no")            
