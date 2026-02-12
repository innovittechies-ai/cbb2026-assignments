# The Delivery Van Marathon
 
n = int(input("Number of delivery trips: ")) #input number of trips


distances_travelled = list(map(int, input("Enter distances: ").split())) #input distances travelled for each trip

total_distance = sum(distances_travelled) #calculate total distance by summing up the distances_traveled

print("Total distance :", total_distance) #print the total distance traveled.
     
 
