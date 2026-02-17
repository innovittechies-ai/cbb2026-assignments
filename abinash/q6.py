def suspect_user():
    N = int(input('Enter Your No of input:-'))
    records = []
    for _ in range(N):
        user_id,distance_in_km,time_in_hours = input().split(',')
        records.append((int(user_id),int(distance_in_km),int(time_in_hours)))
    suspect_user= []
    for ind_record in records:
        user_id = ind_record[0]
        distance_in_km = ind_record[1]
        time_in_hours = ind_record[2]
        speed = distance_in_km/time_in_hours
        if speed >=900:
            suspect_user.append(user_id)
    if suspect_user:
        for user in suspect_user:
            return user
    else:
        return 'No suspicious users'

print(suspect_user())