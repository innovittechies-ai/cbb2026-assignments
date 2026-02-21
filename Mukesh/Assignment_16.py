n = int(input()) # takes n number of inputs
    
events = []  # This list will store all entry and exit times in a single list.
     
 
# Read all entry and exit times
for i in range(n): 
    entry , exit = map(int,input().split()) 
     
    # 1 represents entry and -1 represents exit
    events.append((entry,1))    
    events.append((exit, -1)) 

# Sort all events based on time. If time is same, exit should be considered before entry.
events.sort(key=lambda x: (x[0], -x[1]))
 
# Track current crowd and max crowd 
current = 0 
max_crowd = 0 
  
# Loop through all events and find max crowd
for time, change in events: 
    current += change     
    # Update max crowd if current crowd is greater than max crowd
    max_crowd = max(max_crowd, current)

# Print maximum crowd
print(max_crowd)    