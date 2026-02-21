n = int(input())  # enter the total number of student

marks = list( map( int,input().split())) 
# taking marks of students

avg = sum(marks)/n 
# calculating average of marks

count = 0  
# initialising count to zero
   
for i in marks:    
    # traversing through marks
    if i > avg: 
        # checking if marks are greater than average 
        count+=1 
        # incrementing count
print(count)
