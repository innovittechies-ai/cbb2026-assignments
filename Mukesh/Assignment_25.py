n = int(input())  #
 
transaction_time = [int(input()) for i in range(n)] # Takes the second line input (space separated numbers)
#split() breaks the string into parts
# map(int, ...) converts each part into integer
# list() stores them in a list
 
count =  0 
# Initialize count of spikes
  
for num in range(1,n):  
    if transaction_time[num] > 2*transaction_time[num-1] : 
        count +=1     

print(count)      