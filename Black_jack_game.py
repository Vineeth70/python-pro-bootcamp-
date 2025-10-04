import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score :
        return "It's a Draw!"
    elif c_score == 0:
        return "You lose! opponent has blackJack!"
    elif u_score == 0:
        return "You win!"
    elif u_score > 21:
        return "You Lose!"
    elif c_score > 21:
        return "You Win!"
    elif u_score>c_score:
        return "You win!"
    else:
        return "You lose!"

def play():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards {user_cards}, score = {user_score}")
    print(f"computer's first card is {computer_cards[0]}")
    game_over = False
    while not game_over:
        if user_score == 0:
            game_over = True
        elif computer_score == 0:
            game_over = True
        elif user_score > 21 :
            game_over = True
        user_choice = input("want to draw another Card ? (y/n): ").lower()
        if user_choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    result = compare(user_score,computer_score)
    print(result)
    print(f"your cards {user_cards}, score = {user_score}")
    print(f"Computer cards {computer_cards}, score = {computer_score}")

while input(" want to play another game ? (y/n) :").lower() == 'y':
        print("\n"*100)
        play()
