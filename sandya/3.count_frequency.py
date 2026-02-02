#Count the frequency of each character in a string 
str = "hello world"
freq ={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("Character frequency:", freq)
