def credit_reverse():
    N = int(input('Enter The no that you want to stored:-'))
    records = {}
    for i in range (N):
        emp_id,time,amount = map(int, input().split(','))

        if emp_id not in records:
            records[emp_id] = []

        records[emp_id].append((time,amount))
    affected_employee = set()

    for ind_emp_id in records.keys():
        emp_id = ind_emp_id
        transaction = records[ind_emp_id]
        #print(emp_id)

        credits = []
        reverse = []
        for time,amount in transaction:
            if amount>0:
                credits.append((time,amount))
            else:
                reverse.append((time,amount))
        
        for c_time,c_amount in credits:
            for r_time,r_amount in reverse:
                if (r_amount == -c_amount) and (r_time > c_time) and (r_time-c_time <=24):
                    affected_employee.add(emp_id)
        
        # print(credits)
        # print(reverse)

    for ind_aff_emp_id in sorted(affected_employee):
        print(ind_aff_emp_id) 

credit_reverse()