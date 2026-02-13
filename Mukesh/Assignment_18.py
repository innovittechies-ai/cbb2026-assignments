n = int(input())  # enter the total number of student

marks = list( map( int,input().split()))   # enter the marks

avg = sum(marks)/n  #Average of the marks
count = 0  # initiallizing the count as o

for i in marks:  # iterating over the marks
    if i > avg:  # giving condition :if the mark is greater than average marks 
        count+=1 # if condition staifies : count = count+1
print(count)
