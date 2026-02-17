# reads how many records are coming
n = int(input())

# stores all transactions employee-wise
data = {}

# input employee_id, time, amount and stores in data dictionary
for _ in range(n):
    emp_id, time, amount = map(int, input().split())
    if emp_id not in data:
        data[emp_id] = []  #If employee not already in dictionary, create list
    data[emp_id].append([time, amount]) #Add transaction into that employee list

affected = [] #This will store employees whose salary was credited and reversed within 24 hours

# Check each employee and loop employee by employee
for emp_id in data:
    records = data[emp_id]
    for i in range(len(records)):  #this picks one record at a time
        time1, amt1 = records[i] 
        if amt1 > 0:  # positive salary means credited
            for j in range(len(records)):  #This checks every transaction again for same employee
                time2, amt2 = records[j]
                if amt2 < 0:  # negative means reversal
                    if amt1 == -amt2 and 0 < time2 - time1 <= 24:  # amt1 == -amt2 → 50000 == 50000
                        if emp_id not in affected:
                            affected.append(emp_id) #Add employee only once

# Sort affected employees
affected.sort()

# Print output
for emp in affected:
    print(emp)
