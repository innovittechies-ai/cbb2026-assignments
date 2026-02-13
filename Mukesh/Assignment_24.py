n= int ( input()) # enter the number of deliveries
a = list (map ( int, input().split()))  # enter the delivery distance in KM

a.sort() # sort the data
m = abs( a[1] - a[0] )  # initialling the min value 

for i in range( n-1 ):  # iterating over the range of deliveries
    if a[i+1] - a[i] < m:   # giving condtion that the difference of the consecutive is less than the min
        m = a[ i + 1 ] - a[i]  # if condn satifies then update the min value

print(m)        