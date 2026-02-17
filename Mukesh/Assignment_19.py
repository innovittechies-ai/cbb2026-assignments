n = int ( input()) #enter the number of deliveries 
delayed_del = []   # empty list to store the indices of delayed orders

for i in range (n):    # iterating through the number of deliveries
    expected , actual = list ( map ( int, input().split()))  # taking expected and actual time of orders 
    if actual - expected > 15 :      # checking if the actual time of order is greater than 15 mins of expected time
        delayed_del .append(i)    
         
if delayed_del:   # if delayed orders are present print the indices
    for i in delayed_del:   # iterating through the delayed orders and printing the indices
        print(i)  
else: 
    # else print no delay
    print('No Delay')
