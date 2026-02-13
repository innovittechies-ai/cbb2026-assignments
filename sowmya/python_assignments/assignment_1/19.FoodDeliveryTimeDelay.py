N=int(input())
orders_delay=[]
for _ in range(N):
    line=input().split()
    expected_time=int(line[0])
    actual_time=int(line[1])
    delay_time=actual_time-expected_time
    orders_delay.append(delay_time)
found_delay=False
for i in range(len(orders_delay)):
    if orders_delay[i] > 15:
        print(i) # Print the index, not the delay time
        found_delay = True
if not found_delay:
    print("No delays")