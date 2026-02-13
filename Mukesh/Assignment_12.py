n = int(input())

from collections import defaultdict

booking_count = defaultdict(int)

for i in range(n):
    user_id , hour = map(int,input().split())
    booking_count[(user_id,hour)] += 1

violators = set()
for (user_id, hour), count in booking_count.items():
    if count > 3:
        violators.add(user_id)

if violators:
    print(*sorted( violators))
else:
    print('NO violations')                