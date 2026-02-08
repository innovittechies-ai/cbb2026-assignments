#neha salary shock
n = int(input("enter number of transactions: "))
transactions = []
for i in range(n):
    # Read employee_id, time, and amount
    # Handling potential dash in sample like 101 20-50000
    line = input().replace('-', ' -').split()
    emp_id = int(line[0])
    time = int(line[1])
    amount = int(line[2])
    transactions.append([emp_id, time, amount])

affected_employees = []

for i in range(len(transactions)):
    emp_i, time_i, amt_i = transactions[i]
    
    # If it's a credit (positive amount)
    if amt_i > 0:
        for j in range(len(transactions)):
            emp_j, time_j, amt_j = transactions[j]
            
            # Check if same employee, negative amount matches, and within 24 hours
            if emp_i == emp_j and amt_i == -amt_j:
                time_diff = time_j - time_i
                if 0 < time_diff <= 24:
                    if emp_i not in affected_employees:
                        affected_employees.append(emp_i)

# Sort and print
affected_employees.sort()
for emp in affected_employees:
    print(emp)