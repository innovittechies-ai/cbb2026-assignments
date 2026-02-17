# The Library Fine Spiral 
# Ask for the number of books
n = int(input("Enter the total number of books: "))

total_fine = 0

# Loop through each book to get the days late and calculate the fine
for i in range(n):
    days = int(input(f"Enter the days late for book {i + 1}: "))
    
    # Fine = days * 2
    current_fine = days * 2
    total_fine += current_fine

# Print the final total
print("The calculated total fine is:", total_fine)