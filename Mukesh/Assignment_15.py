n = int(input())  # Takes input N ( N means how many students/books are returned late)

# Initialize total fine
total_fine = 0

# Loop through each late return  
for i in range (n):
    days_late = int(input()) 
    total_fine += 2 * days_late  # Calculate fine for each book (2 rupees per day)
 
print("total_fine:",total_fine) 