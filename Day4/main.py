import random

random.seed(2222234343)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]
player = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if player < 3 and player >= 0:
  print(game_image[int(player)])
else: 
  print("Didn't choose correct number. You lose")
computer = random.randint(0, 2)
print("Computer chose:")
print(game_image[int(computer)])

row1 = ["Tie","You Win","You Lose"]
row2 = ["You Lose","Tie","You Win"]
row3 = ["You Win","You Lose","Tie"]
map = [row1, row2, row3]

if player < 3 and player >= 0:
  print (map[int(computer)][int(player)])