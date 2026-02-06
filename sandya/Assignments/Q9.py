
#API Abuse at Midnight

n = int(input("Enter number of users: ")) #input from user

users = {} #creatimg an empty dictionary to store user_id and minute

for _ in range(n):
    user_id, minute = map(int, input("Enter user_id and minute: ").split()) #iput user_id and minute
    
    if user_id in users:
        users[user_id] += 1 # increment count if user_id already exists
    else:
        users[user_id] = 1  #initialize couunt if user_id not exists

violating_users = [] #list to store user_ids with violations 

for user_id, count in users.items():
    if count >= 3:
        violating_users.append(user_id)

if violating_users:
    print("Violating user IDs:", violating_users) #print violating user_ids
else:
    print("No violations")
