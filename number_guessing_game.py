import random
logo =  r"""
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""

def game():
    print(logo)
    print("Welcome to Number Guessing Game.")
    num = random.randint(1,100)
    print("I am thinking a number between 1 and 100.")
    difficulty_level = input("Choose easy or hard : ").lower()
    num_chance = 0
    if difficulty_level == "easy":
        num_chance = 10
    elif difficulty_level == "hard":
        num_chance = 5
    else:
        print("Invalid choice. Defaulting to hard mode.")
        num_chance = 5
    while num_chance != 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == num :
            print(f"You got it right.The right answer was {num}")
            break
        elif user_guess < num:
            print("Too Low")
            print("Guess again")
            num_chance -= 1
        elif user_guess > num:
            print("Too High")
            print("Guess again")
            num_chance -= 1
        print(f"You have {num_chance} attempts remaining to guess the number.")
        if num_chance == 0:
            print(f"You ran out of chances. The correct answer was {num}")

game()
