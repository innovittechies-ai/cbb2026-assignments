N=int(input())
sum=0
count=0
students_marks=list(map(int,input().split()))
for marks in students_marks:
    sum += marks
class_avg=sum/N
for marks in students_marks:
    if(marks>class_avg):
        count +=1
print(count)