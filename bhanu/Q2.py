# Neha’s Salary Shock
total_employees = int(input("Enter number of employees: "))
transactions = [tuple(map(int, input().split())) for _ in range(total_employees)]

credits = {}
affected = set()

for e_id, time, amount in transactions:
    if amount > 0:
        credits.setdefault(e_id,[]).append((time, amount))
    else:
        if e_id in credits:
            for c_time, c_amt in credits[e_id]:
                if c_amt == -amount and abs(time - c_time) <= 24:
                    affected.add(e_id)

# Output affected employees in ascending order
for emp in sorted(affected):
    print(emp)

