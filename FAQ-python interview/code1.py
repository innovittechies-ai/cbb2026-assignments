#11 missing num in array.
data= [1,2,3,5,6,7,8] # data 
for i in range(data[-1]):
    if i in data:
        print("available",i)
    else:
        print("missing",i)