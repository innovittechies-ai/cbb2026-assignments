# Freelancer Payment Balancer 
#  the total number of transactions
n_input = input("Enter the number of transactions to process: ")
n = int(n_input)

# Check if there are any transactions to process
if n == 0:
    print("No transactions recorded. Balance remains at 0.")
else:
    # the transaction amounts in a single line, separated by spaces
    transactions_input = input("Enter the transaction amounts separated by spaces: ")
    transactions = list(map(int, transactions_input.split()))

    balance = 0
    possible = True

    # Process each transaction one by one
    for t in transactions:
        balance += t
        # If at any point the balance is negative, the sequence is impossible
        if balance < 0:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")