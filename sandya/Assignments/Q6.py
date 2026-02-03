n = int(input("number of user logins: "))
suspicious_user_ids = []

for _ in range(n):
    user_id, distance_in_km, time_in_hours = map(int, input().split())

    
    travel_speed = distance_in_km / time_in_hours

    if travel_speed > 900:
        suspicious_user_ids.append(user_id)

if suspicious_user_ids:
    print(suspicious_user_ids)
else:
    print("no suspicious user_ids")
