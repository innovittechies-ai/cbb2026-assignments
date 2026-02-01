def calculate_total_time():
    N = int(input('Enter the number of sessions:'))
    session = []
    for i in range(N):
        user_input = input()
        time_values = user_input.split(',')
        joined_time = int(time_values[0])
        leave_time = int(time_values[1])
        session.append((joined_time, leave_time))

    total_spend_time = 0
    for joined_time, leave_time in session:
        if leave_time > joined_time:
            total_spend_time += (leave_time - joined_time)
    
    print(f'Total time spent by all users in the website is: {total_spend_time}')

calculate_total_time()