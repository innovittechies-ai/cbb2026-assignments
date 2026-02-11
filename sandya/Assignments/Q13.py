#Calculate the final wallet balance after all transactions
 
n = int(input("Enter number of transactions: "))

positive_values = [] #Storing positive values in a list
negative_values = [] #storing negative values in a list

for t in range(n):
    transaction_amount = int(input("Enter positive or negative value: "))# taking input of transaction amount

    if transaction_amount > 0: #checking if the transaction amount is positive or negative
        positive_values.append(transaction_amount) #adding positive values to the list
    else:
        negative_values.append(transaction_amount) #adding negative values to the list

sum_positive = sum(positive_values)#calculating sum of positive values
sum_negative = sum(negative_values)#calculating sum of negative values

final_balance = sum_positive + sum_negative #calculating final balance in the wallet
print("Final wallet balance:", final_balance) #printing the final balance in the wallet
