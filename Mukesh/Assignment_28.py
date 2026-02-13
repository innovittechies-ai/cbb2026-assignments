n = int(input())

arr = [int(input()) for i in range(n)]

free_space = 0

max_count = 0

for num in arr:
    if num ==0:
        free_space += 1
        max_count = max (max_count , free_space)
    else:
        free_space = 0

print("output :", max_count)             