n = int (input()) # takes number of trips
     
distance = list ( map (int,input().split())) # input().split() → splits into strings:
# map(int, ...)converts each string into integer
# list(...) makes it a list 
 
print( sum(distance))