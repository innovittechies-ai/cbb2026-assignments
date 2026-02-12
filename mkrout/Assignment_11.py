n = int(input())

steps = list ( map (int,input().split()))

abnormal = []

for i in range ( 5,n ):
    avg_prev_5 = sum(steps[i-5:i]/5)
    if steps[i] > 2 * avg_prev_5:
        abnormal.append (i)

if abnormal : 
    for idx in abnormal:
        print(idx)
else:
    print('no abnormal')
    
                    