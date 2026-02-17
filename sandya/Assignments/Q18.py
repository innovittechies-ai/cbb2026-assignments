#The Principal's Result Shock
n = int(input("Enter number of students: "))
marks = list(map(int, input("Enter student marks: ").split()))

average = sum(marks) / n #calculate average marks

count = 0 # initialize count of student marks scoring above average
for mark in marks:
    if mark > average: #compare each mark with average
        count += 1

print("Count:", count)
