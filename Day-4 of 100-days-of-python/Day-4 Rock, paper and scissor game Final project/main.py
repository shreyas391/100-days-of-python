#Day-4 Rock, paper and scissor game Final project
import random
user_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

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

Game = [rock, paper, scissors]
user_selected = Game[user_int]
print(user_selected)

random_int = random.randint(0, 2)
com_selected = Game[random_int]
print(com_selected)

if (user_int == 0 and random_int == 1) or (user_int == 2 and random_int == 0) or (user_int == 1 and random_int == 2):
  print("Computer wins!")
elif (user_int == 1 and random_int == 0) or (user_int == 0 and random_int == 2) or (user_int == 2 and random_int == 1):
  print("You win!")
else:
  print("It's Draw!")

# if you can't understand the above if, else statement then
# you can use the below code
# if user_int == 0 and random_int == 1:
#   print("Computer wins!")
# elif user_int == 1 and random_int == 0:
#   print("You win!")
# elif user_int == 2 and random_int == 0:
#   print("computer wins!")
# elif user_int == 0 and random_int == 2:
#   print("You win!")
# elif user_int == 1 and random_int == 2:
#   print("computer wins!")
# elif user_int == 2 and random_int == 1:
#   print("You win!")
# else:
#   print("It's Draw!")

