n = int(input())

Response_time = [int(input()) for i in range(n)] 
# Reading response time

seen = set() 
# Use set to track elements we have already seen
 
# Iterate through the list
for i in Response_time: 
    if i in seen:    
        # If element is already in the set, print it and break
        print(i) 
        break
 
    seen.add(i) 
# Add element to the set
else : 
    # If loop completes without breaking, print -1
    print(-1)