# Q1: Aarav vs the Unstable Internet
def online_class(join_times, leave_times):
    total_attended_time = 0
    for i in range(len(join_times)):
        attended_time = leave_times[i] - join_times[i]
        total_attended_time += attended_time
    return total_attended_time

n = int(input("enter num of sessions: "))
join_times = []
leave_times = []

for i in range(n):
    join_time = int(input(f"Enter join time for session {i+1}: "))
    leave_time = int(input(f"Enter leave time for session {i+1}: "))
    join_times.append(join_time)
    leave_times.append(leave_time)

print("total attended time:", online_class(join_times, leave_times))


# or 

n = int(input("enter num of sessions: "))

sessions = [tuple(map(int, input("Enter join and leave time: ").split()))
            for _ in range(n)]

total_time = sum(leave - join for join, leave in sessions)

print("total attended time:", total_time)


