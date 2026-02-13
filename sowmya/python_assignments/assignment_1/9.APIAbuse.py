N=int(input())
request_counts={}
violators=set()# used set to avoid duplicates
for _ in range(N):
    user_id,minute=input().split()
    key=(user_id,minute)
    if key in request_counts:
        request_counts[key] += 1
    else:
        request_counts[key]=1
    if request_counts[key]>3:
        violators.add(user_id)
if violators:
    for user in violators:
        print(user)
else:
    print('No violators')