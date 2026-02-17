n_input = input("enter the number of products:").strip()
if not n_input:
    exit()

n = int(n_input)
stock_levels = {}
violated = []
seen_violation = set() # To keep track of duplicates efficiently

for i in range(n):
    line = input().strip()
    if not line:
        continue
    
    # Robust Parsing: Handles "A 10", "A -10", and "A-10"
    if ' ' in line:
        parts = line.split()
        pid = parts[0]
        change = int(parts[1])
    elif '-' in line:
        parts = line.split('-')
        pid = parts[0]
        change = -int(parts[1])
    else:
        # Fallback for unexpected formats
        continue
        
    # Update Stock
    if pid not in stock_levels:
        stock_levels[pid] = 0
    stock_levels[pid] += change
    
    # Check for Violation
    if stock_levels[pid] < 0:
        if pid not in seen_violation:
            violated.append(pid)
            seen_violation.add(pid)
if not violated:
    print("No violation")
else:
    for p in violated:
        print(p)