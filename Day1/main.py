#A basic program that demonstrates working with the print function, 
#variables and string manipulation

#print function
print("Welcome to Name My Band!")

#variables
cityname = input("What's the name of the city you grew up in?\n")
petname = input("What is the name of your pet or any pet name?\n")

#string manipulation
print("This is your Band Name: " + cityname + " " + petname)

#bonus: return the total lenth of the Band Name
print("And your Band Name is " + str(len(cityname) + len(petname)) + " characters long")