def learning_progress_cheacker():
    N = int(input('Enter Your Number of session:-'))
    watch = list(map(int, input().split()))
    
    result = []
    
    for w in watch:
        if w >= 80:
            result.append("HIGH")
        elif w >= 50:
            result.append("MEDIUM")
        else:
            result.append("LOW")
    
    return (" ".join(result))

print(learning_progress_cheacker())