n = int(input())

total_fine = 0

for i in range (n):
    days_late = int(input())
    total_fine += 2 * days_late

print("total_fine:",total_fine)