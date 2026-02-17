n = int (input())  # takes input N ( how many times the arav joined and left the class)

tot_time = 0 # total minutes Aarav attended

for i in range (n):  # Loop through all sessions
    j_time , l_time = map(int,input().split()) # Take join and leave time input
    tot_time += (l_time - j_time) # Add attended time of that session

print(tot_time)