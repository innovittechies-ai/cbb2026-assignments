import string

def preprocess(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words = text.split()
    return words
n = int(input("Enter number of resumes: "))
resumes = []
for i in range(n):
    resume = input(f"Enter resume {i+1}: ")
    resumes.append(resume)
resumes_words = [preprocess(resume) for resume in resumes]
found = False
for i in range(n):
    for j in range(i+1, n):
        words_i = set(resumes_words[i])
        words_j = set(resumes_words[j])
        common_words = words_i & words_j
        match_ratio = len(common_words) / len(words_i)
        if match_ratio >= 0.8:
            print(i, j)
            found = True
if not found:
    print("No duplicates")