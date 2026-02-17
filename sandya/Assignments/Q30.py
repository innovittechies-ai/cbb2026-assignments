#	The AI Hiring Challenge

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

diff = []

for i in range(n):
    if arr[i] != sorted_arr[i]:
        diff.append(i)

if len(diff) == 0 or len(diff) == 2:
    print("YES")
else:
    print("NO")
