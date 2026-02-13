N=int(input())
result=[]
res=''
for student in range(N):
    student_watch_percentage=int(input())
    if student_watch_percentage>80 and student_watch_percentage<100:
        res="HIGH"
    elif student_watch_percentage>50 and student_watch_percentage<=80 :
        res="MEDIUM"
    elif student_watch_percentage>0 and  student_watch_percentage<=50:
        res="LOW"
    else:
        res="INVALID PERCENTAGE"
    result.append(res)
#print(result)
for i in range(0,len(result)):
    print(result[i])