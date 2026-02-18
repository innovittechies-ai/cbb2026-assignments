# The Principal’s Result Shock
# Get the number of students
n_input = input("Enter the total number of students: ")
n = int(n_input)

# Check to prevent division by zero if n is 0
if n > 0:
    # Get the marks as a list of integers
    marks_input = input("Enter all marks separated by spaces: ")
    marks = list(map(int, marks_input.split()))

    # Calculate the average (sum of all marks divided by number of students)
    average = sum(marks) / n
    
    count = 0
    # Loop through marks to find how many are strictly greater than the average
    for m in marks:
        if m > average:
            count += 1

    print("Number of students with marks above average:", count)
else:
    print("The number of students must be greater than zero.")