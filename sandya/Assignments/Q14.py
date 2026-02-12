# The Exam Seating Chaos
n = int(input("Enter number of students:"))
rolls_numbers= list(map(int, input("Enter roll numbers:").split()))

evens = []
odds = []

# Separate even and odd roll numbers
for r in rolls_numbers:
    if r % 2 == 0:
        evens.append(r)
    else:
        odds.append(r)
result = []
i = j = 0

# Decide which group to start with
# Start with the group that appears first in the original list
if rolls_numbers[0] % 2 == 0:
    start_even = True
else:
    start_even = False

# Alternate evens and odds
while i < len(evens) or j < len(odds): # using whille loop to continue until we have added all evens and odds to the result list
    if start_even and i < len(evens): # if we are starting with evens and there are still evens left to add
        result.append(evens[i]) # add the current even number to the result list
        i += 1
    elif not start_even and j < len(odds): # if we are starting with odds and there are still odds left to add
        result.append(odds[j])
        j += 1

    start_even = not start_even # switch between even and odd for next iteration

# Print result
print(*result)
