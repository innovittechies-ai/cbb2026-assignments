N=int(input())
transaction_amount=0
for i in range(N):
    transaction=int(input())
    transaction_amount +=transaction
print(transaction_amount)