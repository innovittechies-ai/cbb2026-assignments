n = int(input())

arr = list(map(int,input().split()))

evens = [x for x in arr if x % 2 == 0]
odds = [x for x in arr if x % 2 != 0]

result = []

i = j = 0

#decides which group start

evens_turns = len(evens) and j >= len(odds)

while i < len(evens) or j < len(odds):

    if evens_turns and i < len(evens):
        result.append(evens[i])
        i += 1
        

    elif not evens_turns and j < len(odds):
        result.append(odds[j])
        j += 1
    evens_turns = True 

#append remaining elements

result.extend(evens[i:])
result.extend(odds[j:])

print(*result)