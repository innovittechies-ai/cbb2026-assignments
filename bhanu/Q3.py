# Q3 - The Curious Case of the Copy Paste Resumes
import string
N = int(input("Num of resumes:")) # number of resumes
resumes = [input()
           .strip()
           .lower()
           .translate(str.maketrans('','', string.punctuation))
           .split()
             for _ in range(N)]

resumes = [set(r) for r in resumes]
found = False

for i in range(N):
    for j in range(i+1, N):
        common_words = resumes[i] & resumes[j]
        similarity = (len(common_words) /min(len(resumes[i]), len(resumes[j]))) * 100
        if similarity >=80:
            print(i,j)
            found = True

if not found :
    print("no duplicates found")