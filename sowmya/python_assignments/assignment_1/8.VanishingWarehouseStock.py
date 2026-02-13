N=int(input())
stock_map={}
voilated_products=[]
for _ in range(N):
    line=input().split()
    prod_id=line[0]
    change=int(line[1])
    if prod_id not in stock_map:
        stock_map[prod_id]=0
    stock_map[prod_id] += change
    if stock_map[prod_id]<0:
        voilated_products.append(prod_id)
if voilated_products:
    for pid in voilated_products:
        print(pid)
else:
    print('No voilation')