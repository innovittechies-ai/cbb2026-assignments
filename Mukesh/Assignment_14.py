n = int(input()) # takes number of students

arr = list(map(int,input().split()))  # takes input array of numbers

evens = [x for x in arr if x % 2 == 0]  # fetch even numbers from array
odds = [x for x in arr if x % 2 != 0]  # fetch odd numbers from array

result = [] 
# empty list to store result
  
i = j = 0 

# Decide Who Starts First
evens_turns = len(evens) and j >= len(odds) 
 
# Alternating Even and Odd 
while i < len(evens) or j < len(odds): 
 
    # Add Even Number
    if evens_turns and i < len(evens):
        result.append(evens[i])
        i += 1
        
 
    # Add Odd Number
    elif not evens_turns and j < len(odds): 
        result.append(odds[j])  
        j += 1  
    evens_turns = True  
 
 
#append remaining elements

result.extend(evens[i:])
result.extend(odds[j:])

print(*result)