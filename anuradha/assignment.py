# #question 1 Aarav vs the Unstable Internet 

num_of_times = int(input("Enter the number of times he join the class: "))
total =0 

for i in range(num_of_times):
    join_time=int(input("enter join time: "))
    leave_time=int(input("enter join time: "))
    duration = leave_time - join_time
    total = total + duration
print(" total time:",total)

############################################################################################################################################################################


# # question 2Neha’s Salary Shock 
num_of_emp = int(input("enter num of emp: "))
employees =[]
for i in range (num_of_emp):
    emp_id = int(input("enter emp_id: "))
    time = int (input("enter time: "))
    amount = float(input("Eneter amount:"))
    employees.append((emp_id, time, amount))

affected_emp=[]
for emp in employees:
      if emp[2]< 0:
        affected_emp.append(emp)
        
sorted_by_id= sorted(affected_emp, key=lambda x: x[0])
for emp in sorted_by_id:
    print(emp[0])
    
############################################################################################################################################################################


#3 question The Curious Case of the Copy Paste 

import string
# #step 1
num_of_resume = int(input("enter a num of resume: "))
#step 2 read all resume
resumes =[]
for i in range(num_of_resume):
    resume_info=str(input("resume_info: "))
    resumes.append(resume_info)
    
#Step3 preprocessing words
processed_resume =[]

for resume in resumes:
    #convert lower case
    resume_lower = resume.lower()
    
    # remove punchuations
    for punct in string.punctuation:
        resume_lower = resume_lower.replace(punct,"")
        
    #split word
    words = resume_lower.split()
    processed_resume.append(words)
    
#step 4 compare each pair of resume
for i in range(num_of_resume):
    for j in range(i+1,num_of_resume):
        set1 = set(processed_resume[i])
        set2 = set(processed_resume[j])
        
        #find common word
        common = set1 & set2
        
        #find total unique words
        total = set1 | set2
        
        # calculate similar percentage
        if len(total)>0:
            similarity=(len(common))/len(total)*100
        
            # Check if twins (>= 80%)
            if similarity >= 80:
                print(f"Resume {i} and Resume {j} are twins")
        

############################################################################################################################################################################


# Question 4  The Chaotic Traffic Signal
#step1
num_of_lane = int(input("enter num of lane: "))

#step2
num_vahicles= []
for i in range(num_of_lane):
    vahicles =int(input("Enter vahicles: "))
    num_vahicles.append(vahicles)
    

#step3 calculate total vaichals
toatal_vahicles =  sum(num_vahicles)

green_times=[]
for i in range(num_of_lane):
    green_time = int((num_vahicles[i]/toatal_vahicles)*120)
    green_times.append(green_time)
    
for time in green_times:
    print("ALL green times:", time, end=" ")
        


############################################################################################################################################################################

#5 Riya’s Learning Discipline Story 

num_of_student = int(input("enter num of stu: "))

percentage=[]
for i in range(num_of_student):
    stud_watch_time= int(input("Enter watch percentage: "))
    percentage.append(stud_watch_time)
    
for i in range(num_of_student):
    if percentage >= 75:
        print("HIGH")
    
    elif percentage >= 50:
        print("MEDIUM")
        
    else:
        print("LOW")
    print(i, end=" ")
        

    
    
    

    




    
