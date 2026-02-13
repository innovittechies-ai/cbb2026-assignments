N=int(input())
booking_counts={}
violators=set()# used set to avoid duplicates
for _ in range(N):
    user_id,hour=input().split()
    key=(user_id,hour)
    if key in booking_counts:
        booking_counts[key] += 1
    else:
        booking_counts[key]=1
    if booking_counts[key]>5:
        violators.add(user_id)
if violators:
    for user in violators:
        print(user)
else:
    print('No violations')