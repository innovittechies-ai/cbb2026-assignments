# The Exam Seating Chaos
#Get the number of elements
n = int(input("Enter the total number of dice rolls: "))

# Get the rolls as a list of integers
rolls = list(map(int, input("Enter the rolls separated by spaces: ").split()))

evens = []
odds = []

# Separate the numbers into two categories
for r in rolls:
    if r % 2 == 0:
        evens.append(str(r))
    else:
        odds.append(str(r))

rearranged = []
i, j = 0, 0

# Determine whether to start with an Odd or Even number based on the first roll
start_with_odd = (rolls[0] % 2 != 0)

# Rearrange the numbers by alternating between odd and even
while i < len(odds) or j < len(evens):
    if start_with_odd:
        # Try to add an Odd number first
        if i < len(odds):
            rearranged.append(odds[i])
            i += 1
        # Then try to add an Even number
        if j < len(evens):
            rearranged.append(evens[j])
            j += 1
    else:
        # Try to add an Even number first
        if j < len(evens):
            rearranged.append(evens[j])
            j += 1
        # Then try to add an Odd number
        if i < len(odds):
            rearranged.append(odds[i])
            i += 1

# Print the rearranged rolls
print("Rearranged rolls:", " ".join(rearranged))