
n = int(input("Enter number of records: "))

credits = {}
affected = set()

for i in range(n):
    print("Enter: employee_id time amount")
    emp_id, time, amount = map(int, input().split())

    if amount > 0:
        credits.setdefault(emp_id, []).append((time, amount))
    else:
        if emp_id in credits:
            for credit_time, credit_amount in credits[emp_id]:
                if credit_amount == -amount and 0 <= time - credit_time <= 24:
                    affected.add(emp_id)

print("Affected employees:")
for emp in sorted(affected):
    print(emp)
