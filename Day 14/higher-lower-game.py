from art import logo
from art import vs
from game_data import data
from sys import exit
import random

print(logo)

choice_a = random.choice(data)
user_score = 0
game_end = False

def check_score():
    if user_choice == 'A':
        if choice_a['follower_count'] > choice_b['follower_count']:
            return user_score + 1
        elif choice_a['follower_count'] < choice_b['follower_count']:
            game_end = True
            return user_score
    elif user_choice == 'B':
        if choice_b['follower_count'] > choice_a['follower_count']:
            return user_score + 1
        elif choice_b['follower_count'] < choice_a['follower_count']:
            game_end = True
            return user_score

while game_end == False:
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(vs)
    choice_b = random.choice(data)
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    new_user_score = check_score()
    if new_user_score == user_score:
        game_end = True
        exit()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {user_score}")
    else:
        exit()
        print(logo)
        user_score = new_user_score
        print(f"You're right! Current score: {user_score}")
        choice_a = choice_b
