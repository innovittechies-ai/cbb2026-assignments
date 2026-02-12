# ATM Queue Analyzer

n = int(input("Enter number of customers: ")) 
time = list(map(int, input("Enter time spent by each customer").split())) # input time spent by each customer
count = 0 # initialize count of customers who spent more than twice the time of the previous customer
for i in range(1, n):  # iterate through time list starting from the second customer
    if time[i] > 2 * time[i-1]: # check if current customer's time is more than twice the previous customer's time
        count +=1 # increase count if condition is met
print("count:", count) 
