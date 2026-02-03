#Find the first non-repeating character in a string 
str = "hello world"
freq ={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for char, freq in freq.items():
   if freq == 1:
      print("The first non-repeating character is", char)
      break