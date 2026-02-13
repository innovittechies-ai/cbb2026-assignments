N = int(input())
# Read N integers from a single line
durations = list(map(int, input().split()))
# Step 1: Always sort for Shortest Job First
durations.sort()
waiting_times = []
current_wait = 0
for i in range(N):
    waiting_times.append(current_wait)
    current_wait += durations[i]
# Step 2: Sum all wait times except the first (0) and divide by (N-1)
# 0 + 1 + 3 = 4. Then 4 / (3 - 1) = 2
total_wait = sum(waiting_times)
result = total_wait / (N - 1)
print(int(result))