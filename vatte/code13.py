#Arjun’s Digital Wallet Confusion
#  Ask the user for the number of transactions to process
n = int(input("How many transactions would you like to record? "))

# Initialize the starting balance at zero
balance = 0

# Loop through each transaction
for i in range(n):
    # Ask for the specific amount for this transaction
    # User can enter positive for deposits and negative for withdrawals
    amount = float(input(f"Enter amount for transaction {i + 1}: "))
    
    # Update the running total
    balance += amount

# Display the final calculated balance
print("The final total balance is:", balance)