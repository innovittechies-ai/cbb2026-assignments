import string

N = int(input())
resumes = []

# Read and preprocess resumes
for _ in range(N):
    text = input().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = set(text.split())
    resumes.append(words)

found = False

# Compare resume pairs
for i in range(N):
    for j in range(i + 1, N):
        common = resumes[i] & resumes[j]
        min_len = min(len(resumes[i]), len(resumes[j]))

        if min_len > 0 and (len(common) / min_len) * 100 >= 80:
            print(f"({i},{j})")
            found = True

if not found:
    print("no duplicates")

    
    