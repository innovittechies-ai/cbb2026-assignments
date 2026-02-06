def find_resume_twins():
    N = int(input())
    resumes = []
    for i in range(N):
        resumes.append(input())
    
    # Function to clean text and get words
    def clean_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation and split into words
        words = []
        word = ""
        for char in text:
            if char.isalpha():
                word += char
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)
        return words
    
    twins_found = []
    
    # Compare each pair of resumes
    for i in range(N):
        for j in range(i + 1, N):
            words1 = clean_text(resumes[i])
            words2 = clean_text(resumes[j])
            
            # Count matching words
            matching_words = 0
            for word in words1:
                if word in words2:
                    matching_words += 1
            
            # Calculate total unique words
            all_words = words1 + words2
            unique_words = []
            for word in all_words:
                if word not in unique_words:
                    unique_words.append(word)
            
            total_unique = len(unique_words)
            
            # Check if 80% or more words match
            if matching_words / total_unique >= 0.8:
                twins_found.append((i, j))
    
    # Print results
    if twins_found:
        for i, j in twins_found:
            print(i, j)
    else:
        print("No duplicates")

find_resume_twins()