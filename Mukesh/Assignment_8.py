n= int(input()) # Read number of transactions

Stocks = {}  # store the current stock of each product

violations = set() # store the name of products which are violating the rule
 
# Loop through all transactions
for i in range ( n ): 
    product, change =( input().split()) 
    # Read product name and change in stock
    change = int(change) 
    # Convert change to integer

    if product not in Stocks: 
        # If product is not in Stocks, initialize its stock to 0
        Stocks[product] = 0

    # Update stock of the product
    Stocks[product] += change 
 
    # If stock goes below 0, add product to violations
    if Stocks[product] < 0:
        violations.add(product)
 
# Print products with negative stock in lexicographical order
if violations:
    for product in sorted(violations):
        print(product)           
      
else:
    print('no violations')          