# The HR Resume Filter


n = int(input("Enter number of resumes").strip()) # input number of resumes
scores = list(map(int, input("Enter resume scores").split())) # input resume scores

max_sum = scores[0] #initialize max_sum with the first score
current_sum = scores[0] 

for i in range(1, n): # iterate through resume scores starting from the second score
    current_sum = max(scores[i], current_sum + scores[i]) # update current sum by either starting a new sum  with the current_sum 
    max_sum = max(max_sum, current_sum) #

print(max_sum)
    


        