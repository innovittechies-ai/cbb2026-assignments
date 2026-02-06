
# Meera and the Fitness Band

n = int(input("Enter number of hours: "))

steps_per_hour = list(map(int, input("Enter steps per hour: ").split()))
abnormal = []

# start from index 5 because we need previous 5 hours
for i in range(5, n): 
    average = (
        steps_per_hour[i-1] +
        steps_per_hour[i-2] +
        steps_per_hour[i-3] +
        steps_per_hour[i-4] +
        steps_per_hour[i-5]
    ) / 5

    if steps_per_hour[i] > 2 * average: #checking for abnormal hours
        abnormal.append(i)

if abnormal: # checking if abnormaal lis is not empty
    print("indices of abnormal hours:", abnormal)
else:
    print("no abnormal hours")
