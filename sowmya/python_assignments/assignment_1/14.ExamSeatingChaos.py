N = int(input())
roll_numbers = list(map(int, input().split()))
# Separate into evens and odds
evens = [x for x in roll_numbers if x % 2 == 0]
odds = [x for x in roll_numbers if x % 2 != 0]
rearranged = []
e_idx, o_idx = 0, 0
# Determine which list to pull from first based on original input
# (Alternatively, you can start with the larger list to maximize alternation)
starts_even = (roll_numbers[0] % 2 == 0)
for i in range(N):
    if starts_even:
        if e_idx < len(evens):
            rearranged.append(evens[e_idx])
            e_idx += 1
        starts_even = False # Switch to odd for next iteration
    else:
        if o_idx < len(odds):
            rearranged.append(odds[o_idx])
            o_idx += 1
        starts_even = True # Switch to even for next iteration
# Print the list as space-separated integers
print(*(rearranged))