n= int(input())
transactions = list (map(int, input().split())) 
# Reading transaction values
 
balance = 0 
# Initializing balance
valid = True  
 
# Looping through transactions
for i in transactions:  
    # Adding transaction value to balance
    balance +=i  
    if balance < 0 : 
        # If balance goes negative, transaction is invalid
        valid = False 
        break 
 
print('YES' if valid else 'NO')     