employes_count=int(input())
list=[]
print(employes_count)
for i in range(employes_count):
    emp_id=int(input())
    time_in_hours=int(input())
    amount=int(input())
    print(emp_id,time_in_hours,amount)
    if(amount<0):
        list.append(emp_id)
print(list)