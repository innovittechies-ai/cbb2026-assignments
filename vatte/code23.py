#
# Ask for the total number of scores recorded
n_input = input("Enter the number of scores in the sequence: ")
n = int(n_input)

# Handle the case where the list might be empty
if n == 0:
    print("No scores to calculate.")
else:
    # Get the scores as a list of integers
    scores_input = input("Enter the scores separated by spaces: ")
    scores = list(map(int, scores_input.split()))

    # Initialize with the first element
    max_so_far = scores[0]
    current_max = scores[0]

    # Iterate through the scores starting from the second one
    for i in range(1, n):
        # Decision: Is it better to start a new subarray or add to the current one?
        # We start new if the current score is higher than the sum so far + current score
        if scores[i] > (current_max + scores[i]):
            current_max = scores[i]
        else:
            current_max = current_max + scores[i]
            
        # Update the overall maximum found across the entire process
        if current_max > max_so_far:
            max_so_far = current_max

    print("The maximum sum of a contiguous score sequence is:", max_so_far)