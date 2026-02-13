#AI Chatbot Response Delay

n = int(input()) # input number of responses
arr = list(map(int, input().split())) #input array of responses

seen = set() # create an empty set to store elements 

for num in arr: # iterate through the array
    if num in seen: # checks if number is in seen
        print(num) # print the repeated number
        break
    seen.add(num) # add number to seen
else:
    print(-1)

    

