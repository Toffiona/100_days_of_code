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

#Write your code below this line 👇
import random
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0,2)

if your_choice >= 3:
    print("You type an invalid number, you loose")
    
elif your_choice == 0:
    print(rock)
    if computer_choice == 0:
        print(f"Computer chose:\n{rock}")
        print("It's a draw")
    elif computer_choice == 1:
        print(f"Computer chose: \n{paper}")
        print("You win")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors}")
        print("Computer win")

elif your_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(f"Computer chose:\n{rock}")
        print("You win")
    elif computer_choice == 1:
        print(f"Computer chose: \n{paper}")
        print("It's a draw")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors}")
        print("Computer win")

elif your_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print(f"Computer chose:\n{rock}")
        print("Computer win")
    elif computer_choice == 1:
        print(f"Computer chose: \n{paper}")
        print("You win")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors}")
        print("It's a draw")


