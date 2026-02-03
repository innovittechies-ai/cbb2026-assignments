N = int(input("Enter number of employees: "))
transactions = {}

for _ in range(N):
    employee_id, time_in_hours, amount = map(int, input().split())

    if employee_id not in transactions:
        transactions[employee_id] = []

    transactions[employee_id].append((time_in_hours, amount))

affected = []

for employee_id, records in transactions.items():
    credits = []
    reversals = []

    for time, amount in records:
        if amount > 0:
            credits.append((time, amount))
        else:
            reversals.append((time, -amount))

    for c_time, c_amt in credits:
        for r_time, r_amt in reversals:
            if c_amt == r_amt and abs(r_time - c_time) <= 24:
                affected.append(employee_id)
                break

affected = sorted(set(affected))

for emp in affected:
    print(emp)
   
        
