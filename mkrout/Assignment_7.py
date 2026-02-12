n = int ( input())

suspicious = []

for i in range (n):
    user_id, distance, time = map(int, input().split())

    speed =distance/time

    if speed > 900:
        suspicious.append(user_id)

if suspicious:
    for user in suspicious:
        print(user)

else:
    print("no suspicious user")                