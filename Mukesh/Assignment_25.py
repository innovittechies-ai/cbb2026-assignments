n = int(input())

transaction_time = [int(input()) for i in range(n)]

count = 0

for num in range(1,n):
    if transaction_time[num] > 2*transaction_time[num-1] :
        count +=1

print(count)      