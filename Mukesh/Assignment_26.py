n = int(input())

Response_time = [int(input()) for i in range(n)]

seen = set()

for i in Response_time:
    if i in seen:
        print(i)
        break

    seen.add(i)
else :
    print(-1)