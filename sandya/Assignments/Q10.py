#The Morning Call Center Rush

n = int(input("Enter number of calls: ")) #input number of calls
call_duration = list(map(int, input("Enter call durations in minutes: ").split()))

if len(call_duration) == n: #check if number of duration matches call_duration entries
    total_duration = sum(call_duration) #calculating total_duration
    average_duration = total_duration/n #calculating average_duration
    print("Average call duration:", average_duration)
else:
    print("Error: Number of durations entered does not match number of calls")