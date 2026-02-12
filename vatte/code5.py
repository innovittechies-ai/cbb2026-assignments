# riya's learning discipline
n = int(input("Enter the number of students: "))
percentages = list(map(int, input("Enter the percentages of students: ").split()))
results = []

for p in percentages:
    if p >= 80:
        results.append("HIGH")
    elif p >= 50:
        results.append("MEDIUM")
    else:
        results.append("LOW")

print(" ".join(results))