#Edwin Corona
#10/15/24
#period 5-6


food = input("Hey did you order food delivery")

if food == "yes":
    print("Great!")
    cost = int(input("What is the cost of the food you ordered: "))
    people = int(input("how many people are splitting the order: "))
    total = cost / people 
    print("The cost per person isG " , total)
else:
    print("NO?! So who is cooking?")
