#The Food Delivery Apology Refund
# Get the total number of entries to check
n = int(input("Enter the total number of flights or events: "))
delayed = []

for i in range(n):
    # Prompt the user for expected and actual times for each event 
    # Using a sentence in the input to guide the user
    user_input = input(f"Enter expected and actual time for event {i+1}: ")
    expected, actual = map(int, user_input.split())
    
    # Calculate the difference
    if (actual - expected) > 15:
        # If the delay is more than 15 minutes, add the index (1-based) to the delayed list
        delayed.append(str(i))

# Output the findings
if not delayed:
    print("No delays")
else:
    # Joins the list of indices into a single string separated by spaces
    print("Indices of significantly delayed events:", " ".join(delayed))