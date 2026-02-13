N=int(input())
user_speed_dict={}
user_id_list=[]
required_login_speed=900
for user in range(N):
    user_id=int(input())
    distance_in_km=int(input())
    time_in_hours=int(input())
    speed=(distance_in_km/time_in_hours)
    user_speed_dict.update({user_id:speed})
for key,value in user_speed_dict.items():
    if value>required_login_speed:
        user_id_list.append(key)
if not user_id_list:
    print('No suspicious users')
else:
    print(user_id_list)