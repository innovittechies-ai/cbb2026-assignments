# Step 1: Get the number of resumes
n = int(input("Enter number of resumes: "))
resumes = []

# Step 2: Collect and process each resume
for i in range(n):
    # This cleans the text, splits it into words, and removes duplicates using set()
    processed_resume = set(input(f"Enter resume {i}: ").lower().split())
    resumes.append(processed_resume)

found = False

# Step 3: Compare every pair (Nested Loop)
for i in range(n):
    for j in range(i + 1, n):
        # '&' finds words that appear BOTH resumes (Intersection)
        common_words = resumes[i] & resumes[j]
        matches = len(common_words)
        
        # Calculate the length of the larger resume to find the percentage
        max_len = max(len(resumes[i]), len(resumes[j]))
        
        # To avoid division by zero error if a resume is empty
        if max_len > 0:
            similarity = matches / max_len
            
            # Step 4: Check if it meets the 80% threshold
            if similarity >= 0.8:
                print(f"Duplicate found: Resume {i} and Resume {j}")
                found = True

# Step 5: Final output if no matches were found
if not found:
    print("No duplicates")