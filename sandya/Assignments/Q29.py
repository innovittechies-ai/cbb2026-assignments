#Freelancer Payment Balancer
n = int(input())
transactions = list(map(int, input().split()))
balance = 0
for t in transactions:
    balance += t
    if balance < 0:
        print("NO")
        break
else:
    print("YES")
