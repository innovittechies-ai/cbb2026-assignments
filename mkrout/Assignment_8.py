n= int(input())

Stocks = {}

violations = set()

for i in range ( n ):
    product, change =( input().split())
    change = int(change)

    if product not in Stocks:
        Stocks[product] = 0

    Stocks[product] += change

    if Stocks[product] < 0:
        violations.add(product)

if violations:
    for product in sorted(violations):
        print(product)           
  

else:
    print('no violations')          