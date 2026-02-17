# The food Delivery Apology Fund

n = int(input("Enter number of orders"))

delayed_indices = []

for i in range(n):
    expected_time, actual_time = map(int, input("Enter expected_time and actual_time: ").split()) #input expected_time and actual_time
    delay = actual_time - expected_time #calculating delay

    if delay > 15:# if delay is greater than 15 minutes add the index to the delayed_indices list
        delayed_indices.append(i)

if delayed_indices:
    for idx in delayed_indices:
        print(idx)
else:
    print("No delays")
