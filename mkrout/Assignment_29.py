n= int(input())
transactions = list (map(int, input().split()))

balance = 0
valid = True

for i in transactions:
    balance +=i
    if balance < 0 :
        valid = False
        break

print('YES' if valid else 'NO')    