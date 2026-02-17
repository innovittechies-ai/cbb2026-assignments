#Meera and the Broken Fitness Band
# Get the total number of hours recorded
n = int(input("Enter the total number of hours recorded: "))

# Get the steps data as a list
steps = list(map(int, input("Enter the steps for each hour separated by spaces: ").split()))

abnormal = [] 
for i in range(5, n):
    # Calculate the average of the previous 5 hours
    avg_prev = sum(steps[i-5:i]) / 5
    
    # Check if the current steps are more than double the average
    if steps[i] > (2 * avg_prev):
        # We append i (the index) or i+1 if you want the 'Hour Number'
        abnormal.append(str(i))

if not abnormal:
    print("No abnormal hours")
else:
    print("Abnormal hours detected at indices:", " ".join(abnormal))