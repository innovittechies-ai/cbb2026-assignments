n= int(input())

request_count = {}

violations = set()

for i in range ( n ):
    user_id , minute = map ( int, input().spit())
    key = (user_id , minute)
    request_count[key] = request_count.get(key,0) +1
    if request_count[key] > 3:
        violations.add(user_id)

if violations:
        
    for user_id in sorted(violations):
        print(user_id)
else:
    print('no violations')          