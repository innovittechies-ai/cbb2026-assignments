n = int(input()) # takes input from the user as a integer

balance = 0 # initializing balance as 0
 
# Loop through all the records
for i in range(n): 
    # Read the transaction and update the balance
    balance += int(input())     
print(balance) 
