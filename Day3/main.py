print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input("You're at a crossroads.  Where do you want to go? Type \"left\" or \"right\" ").lower()


if (choice1 == "left"): #opening flow statement for choice1
  choice2 = input("You come to a lake.  There's an island in the middle of the lake. Type \"wait\" to wait for a boat.  Type \"swim\" to swim for a boat. ").lower()
  if (choice2 == "wait"): #opening flow statement for choice2
    choice3 = input("You arrived at the island unharmed.  There's a house with three doors.  One red, one yellow and one blue.  Which color do you choose? ").lower()
    if choice3 == "blue": #opening flow statement for choice3
      print("Eaten by beasts. Game Over")
    elif choice3 == "red":
      print("Burned by fire.  Game Over.")
    elif choice3 == "yellow":
      print("You Win!")
    else:
      print("Game Over") #closing flow statement for choice 3
  elif choice2 != "wait": #closing flow statement for choice 2
    print("Attacked by trout.  Game Over")
elif (choice1 != "left"): #closing flow statement for choice1
  print("You fell into a hole.  Game Over")





  


