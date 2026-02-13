N=int(input())
resume_list=[]
for i in range(N):
    resume=str(input())
    resume_list.append(resume)
print(resume_list)
has_duplicates=False
for i in range(N):
    for j in range(i+1,N):
        resume_i=resume_list[i]
        resume_j=resume_list[j]
        if(resume_i==resume_j):
            print(i,j)
            has_duplicates=True
            break
        if has_duplicates:
            break
if not has_duplicates:
    print('No duplicates')