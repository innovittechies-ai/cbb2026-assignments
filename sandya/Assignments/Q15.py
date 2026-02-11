# The Library Fine Spiral

n = int(input("Number of late returns: "))

total_fine = 0   # initialize total fine

for l in range(n):
    days_late = int(input("Enter days late for each return: "))
    fine = days_late * 2 # calculating fine for each late return
    total_fine += fine   # add each fine

print("Total fine:", total_fine)
    