n = int ( input()) #enter the number of deliveries 
delayed_del = [] # create a empty list where delayed orders will be saved

for i in range (n):  #iterating through the range of delivery orders
    expected , actual = list ( map ( int, input().split()))  # providing two delivery duration 
                                                             #  expected delivery time and actual time 
    if actual - expected > 15 :  # providing condition :  if the differnce is greater than the 15 minutes

        delayed_del .append(i) # if the condition satisfies then update the empty list

if delayed_del:   # if the delayed order list has atleast one value than the condition is true else false
    for i in delayed_del:
        print(i)  # print the indices of delayed orders
else:
    print('No Delay')
