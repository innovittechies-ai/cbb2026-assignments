num_of_students = int(input("enter number of students: "))

watch_percent = list(map(int, input("enter watch percentages: ").split()))

for i in range(num_of_students):
    if watch_percent[i] >= 80:
        print("HIGH", end=" ")
    elif watch_percent[i] >= 50:
        print("MEDIUM", end=" ")
    else:
        print("LOW", end=" ")
