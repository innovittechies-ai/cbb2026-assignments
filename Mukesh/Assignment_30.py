n= int(input())

ranks = list(map(int, input().split())) 
# Reading rank elements
 
# Sorting ranks in ascending order
sorted_rank = sorted(ranks)
 
# Initializing empty list to store indices where ranks differ from sorted ranks
diff = []
 
# Comparing ranks with sorted ranks and storing indices where they differ
for i in range (n):   
    if ranks[i] != sorted_rank[i] : 
        diff.append(i) 
  
# If there are no differences or exactly two differences, output "yes", otherwise "no"
if len(diff) == 0 or len(diff) == 2: 
    print("yes") 
else: 
    print("no")            
