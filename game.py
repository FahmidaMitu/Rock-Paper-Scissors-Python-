import random

print('ROCK PAPER SCISSORS Game Rules:\n')
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print(f"Rock vs Paper -> Paper wins \n{rock_art}\n{paper_art}")
print(f"Rock vs Scissors -> Rock wins \n{rock_art}\n{scissors_art}")
print(f"Paper vs Scissors -> Scissors wins \n{paper_art}\n{scissors_art}")

# Take input from user
print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
choice = int(input("Enter your choice: "))

# Validation
while choice > 3 or choice < 1:
    choice = int(input("Enter a valid choice please : "))

# Mapping user's choice 
if choice == 1:
    choice_name = 'Rock'
    print(rock_art)
elif choice == 2:
    choice_name = 'Paper'
    print(paper_art)
else:
    choice_name = 'Scissors'
    print(scissors_art)

# Print user's choice
print("User's choice is:", choice_name)

# Random choice for computer
comp_choice = random.randint(1, 3)

# Mapping computer's choice
if comp_choice == 1:
    comp_choice_name = 'Rock'
    print(rock_art)
elif comp_choice == 2:
    comp_choice_name = 'Paper'
    print(paper_art)
else:
    comp_choice_name = 'Scissors'
    print(scissors_art)

# Print computer choice
print("Computer's choice is:", comp_choice_name)

# Determine the winner
if choice == comp_choice:
    result = "DRAW"
elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
    result = 'Paper'
elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
    result = 'Rock'
elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
    result = 'Scissors'

# Print the result
if result == "DRAW":
    print("It's a tie")
elif result == choice_name:
    print("User wins")
else:
    print("Computer wins")

print("Thanks for playing!")
