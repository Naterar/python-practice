import random


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

game_images = [rock, paper, scissors]

user_pick = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print(game_images[user_pick])

computer_pick = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_pick])

if user_pick == computer_pick:
    print("Tied, go again!")
elif (user_pick == 0 and computer_pick == 2) or \
     (user_pick == 1 and computer_pick == 0) or \
     (user_pick == 2 and computer_pick == 1):
    print("You win!")
else:
    print("You lose!")
