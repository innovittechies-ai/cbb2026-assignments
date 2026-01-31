n=int(input("Enter number of sessions: "))
total_time=0
for i in range(n):
    while True:
        data = input("Enter join and leave time: ").strip()
        if data:
            join_time, leave_time = map(int, data.split())
            break
    total_time += (leave_time - join_time)
print("Total attended time:", total_time)
