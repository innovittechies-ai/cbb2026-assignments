n= int(input("number of students"))
watch_percentage= vehicles = list(map(int, input("Enter watch_percentage of students:").split()))
results = []
for p in watch_percentage:
   if p>=80:
       results.append("High")
      
   elif p>=65:
      results.append("medium")
   else:
       results.append("Low")
print(results)
