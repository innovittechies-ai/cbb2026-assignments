#1.----------------------------------------------------------------
# n = int(input())
# total_time = 0 

# for _ in range(n):
#     join_time, leave_time = map(int, input().split())   # Split input into two integers
#     total_time += (leave_time - join_time) 
#     # total_time=total_time + (leave_time - join_time)
# print(total_time)

#3.----------------------------------------------------------------
# n=int(input())
# resumes=[]
# for _ in range(n):
#     text=input().lower() # Convert to lowercase
#     text=text.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ") # Remove punctuation
#                 #     words=text.split()
#                 #     resumes.extend(words)
#                 # unique_words=set(resumes)
#     resumes.append(set(text.split())) # Split into words and store unique words in a set

# found=False # Flag to check if duplicates are found

# for i in range(n):
#     for j in range(i+1,n): # Compare each pair only once
#         common = resumes[i] & resumes[j] # Find common words using set intersection
#         max_words = max(len(resumes[i]), len(resumes[j])) # Find the maximum number of words in either resume
        
#         if max_words > 0 and len(common) / max_words >= 0.8: # Check if 80% or more words are common
#             print(i, j)
#             found = True # Set flag to True if duplicates are found
# if not found:
#         print("no duplicates")
    
#4.---------------------------------------------------------------
# L=int(input())
# vehicles=list(map(int,input().split())) # List of vehicles at each signal
# total_vehicles=sum(vehicles) # Total number of vehicles
# green_time=[]
# for v in vehicles:  # Calculate green light time for each signal
#    green_time.append(int((v / total_vehicles) * 120))
#    # green_time.append(int((v*120)/total_vehicles))  # Proportional green light time
    
# print(*green_time) # *Unpack and print green light times

#5.---------------------------------------------------------------
# N = int(input())
# percentages = list(map(int, input().split()))

# result = []
# for p in percentages:
#     if p >= 75:
#         result.append("HIGH")
#     elif p >= 40:
#         result.append("MEDIUM")
#     else:
#         result.append("LOW")

# print(*result)

#8.---------------------------------------------------------------
# N = int(input())

# stock = {}  # Dictionary to track stock levels
# violations = set()  # Set to track products with negative stock

# for _ in range(N):
#     product_id, change = input().split()    # Read product ID and stock change
#     change = int(change)    # Convert change to integer

#     stock[product_id] = stock.get(product_id, 0) + change   # Update stock level

#     if stock[product_id] < 0:   # Check for negative stock
#         violations.add(product_id)  # Add product ID to violations set

# if violations:
#     print(*violations)
# else:
#     print("No violation")

#9.---------------------------------------------------------------
N = int(input())

requests = {}
violations = set()

for _ in range(N):
    user_id, minute = input().split()   # Read user ID and minute
    key = (user_id, minute)  # Create a unique key for user and minute

    #requests[key] = requests.get(key, 0) + 1    # Increment request count for this user and minute
   
    if key in requests:
        requests[key] += 1
    else:
        requests[key] = 1
    

    if requests[key] > 3:   # Check if requests exceed 3
            violations.add(user_id)     # Add user ID to violations set

if violations:
    print("Violated user= " *violations)
else:
    print("No violations")



    