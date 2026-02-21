#AI Chatbot Response Delay
# Ask for the total number of delay records
n_input = input("Enter the number of delay entries to check: ")
n = int(n_input)

# Check if there is any data to process
if n == 0:
    print("No data provided.")
else:
    # Ask for the delay values separated by spaces
    delays_input = input("Enter the delay values separated by spaces: ")
    delays = list(map(int, delays_input.split()))

    seen = []
    repeated = -1

    # Loop through each delay to find the first one that appears twice
    for d in delays:
        # If d is already in our 'seen' list, we found our first duplicate
        if d in seen:
            repeated = d
            break
        # Otherwise, add it to the list of values we have encountered
        seen.append(d)

    # Output the result
    if repeated != -1:
        print("The first repeated delay value found is:", repeated)
    else:
        print("No repeated delays found.")