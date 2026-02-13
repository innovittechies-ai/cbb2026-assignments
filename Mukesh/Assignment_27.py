n , k , s = map ( int, input().split(()))

arr = list( map ( int, input().split() ))

window_sum = sum(arr[:k])

if window_sum > s:
    print ("YES")

else:
    found = False
    for i in range (k , n):
        window_sum = window_sum - arr[i-k] + arr[i]
        if window_sum > s:
            print("YES")
            found = True
            break
    print("YES" if found else "NO")        


            
