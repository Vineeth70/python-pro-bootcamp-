import random as rd
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images =[rock,paper,scissor]
user_input = int(input("*** Welcome to rock ,paper and scissor Game ***\nGame Rules:  \n 0 for rock \n 1 for paper \n 2 for Scissors\n"))
if user_input >= 0 and user_input <=2:
    print(images[user_input])
computer_choice = rd.randint(0,2)
print("computer choose :")
print(images[computer_choice])
if user_input < 0 or user_input > 2:
    print("You typed wrong number. please try again!")
else:
    if user_input == 0 and computer_choice == 2:
        print("You win!")
    elif user_input == 2 and computer_choice == 0:
        print("You lose!")  
    elif user_input > computer_choice:
        print("You win!")    
    elif computer_choice > user_input:
        print("You lose!")
    elif user_input == computer_choice :
        print("It's draw!")   
     