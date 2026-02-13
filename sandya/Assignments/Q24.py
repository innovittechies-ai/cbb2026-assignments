# The Food Delivery Route Optimizer

n = int(input("Enter number of delivery points:")) #input number of delivery points
distances = list(map(int, input("Enter distances of delivery points:").split())) # input distances off delivery points
distances.sort() # sort distances to find minimum difference between delivery points
min_diff = float('inf')  # initialize minimum difference to infinity
for i in range(1,n):
    difference = distances[i]-distances[i-1] # calculate difference between current and previous delivery point
    min_diff = min(min_diff, difference) 
print("Minimum distance difference between delivery points:", min_diff)
        
    
