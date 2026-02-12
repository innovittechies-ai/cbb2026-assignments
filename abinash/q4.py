def green_time():
    L = int(input('Enter Your Lane:-'))
    vheicle = list(map(int,input().split(',')))
    total_vheicals = sum(vheicle)
    green_times = []
    for v in vheicle:
        green_time = (v*120)//total_vheicals
        green_times.append(green_time)
    for i in range(len(green_times)):
        if i != len(green_times)-1:
            print(green_times[i],end = " ")
        else:
            return green_times[i]
print(green_time())