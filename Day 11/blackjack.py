import random
from art import logo
from sys import exit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    print(logo)
    user_cards = []
    com_cards = []
    game_over = False

    def user_draw_card():
        """user draws 1 card"""
        user_cards.append(random.choice(cards))
    
    def com_draw_card():
        """computer draws 1 card"""
        com_cards.append(random.choice(cards))
        
    user_draw_card()
    user_draw_card()
    com_draw_card()
    com_draw_card()
        
    while game_over == False:
        user_score = sum(user_cards)
        com_score = sum(com_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {com_cards[0]}")
        if user_score == 21:
            cont_game = False
        elif com_score == 21:
            cont_game = False
        else:
            if user_score > 21:
                if 11 not in user_cards:
                    game_over = True
                elif 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
                    user_score = sum(user_cards)
                    if user_score > 21:
                        game_over = True
            else:
                next_card = input("Do you want another card? Type 'y' or 'n': ")
                if next_card == 'y':
                    user_draw_card()
                elif next_card == 'n':
                    game_over = True
    
    while com_score < 17:
        com_draw_card()
        com_score = sum(com_cards)
                    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Your Computer's final hand: {com_cards}, final score: {com_score}")
    if com_score == 21:
        print("You lose, opponent has a Blackjack.")
    elif user_score == 21:
        print("You win, you got a Blackjack!")
    elif user_score > 21:
        print("You went over. You lose.")
    elif com_score > 21:
        print("Your opponent went over. You win!")
    else:
        if com_score > user_score:
            print("You lose.")
        elif com_score < user_score:
            print("You win!")
        elif com_score == user_score:
            print("It's a draw.")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    exit()
    play_game()
