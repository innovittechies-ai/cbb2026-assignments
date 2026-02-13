n = int(input())

traffic = list( map(int, input().split()))

max_len = 1
current_len = 1

for i in range(1,n):
    if traffic[i] > traffic[i-1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1
    
print(max_len)        