n = int(input())  #Reads number of resumes (n)
all_resumes = []  # store processed resumes

# Function to convert resume text into a set of valid words
def make_word_set(text):
    text = text.lower()
    final_text = ""

    # Remove punctuation manually
    for ch in text:
        if ('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch == " ":
            final_text += ch
        else:
            final_text += " "   # replace punctuation with space

    words = final_text.split() # Converts sentence into list of words
    return set(words) # Set removes duplicates.

# Read resumes
for _ in range(n):
    resume_line = input()
    all_resumes.append(make_word_set(resume_line)) #Now each resume becomes a set of words.

found = False

# Compare each resume with every other resume
for i in range(n):
    for j in range(i + 1, n):

        common_words = all_resumes[i] & all_resumes[j]
        total_words = all_resumes[i] | all_resumes[j]

        similarity = (len(common_words) / len(total_words)) * 100

        if similarity >= 80:
            print(i, j)
            found = True

# If no twin resumes found
if not found:
    print("No duplicates")
