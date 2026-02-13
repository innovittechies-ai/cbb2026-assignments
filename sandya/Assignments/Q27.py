#The Cyber Attack Window

n, k, s = map(int, input().split()) # input number of elements , window size, threshold
arr = list(map(int, input().split()))

window_sum = sum(arr[:k])

if window_sum > s:
    print("YES")
else:
    for i in range(k, n):
        window_sum += arr[i]      # add new element
        window_sum -= arr[i - k]  # remove old element

        if window_sum > s:
            print("YES")
            break
    else:
        print("NO")
