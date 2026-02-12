n = int (input()) 

tot_time = 0

for i in range (n):
    j_time , l_time = map(int,input().split())
    tot_time += (l_time - j_time)

print(tot_time)