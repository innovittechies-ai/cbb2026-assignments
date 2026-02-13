N=int(input())
fine=0
delay_days=list(map(int,input().split()))
for days in delay_days:
    each_book_fine=days*2
    fine += each_book_fine
print(fine)