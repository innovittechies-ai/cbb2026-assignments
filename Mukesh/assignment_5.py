n = int ( input()) # Take input N

percentages = list (map(int,input().split())) # Take percentage values

for i in range (n): # Loop N times and print values
    print(percentages[i], end =" ")