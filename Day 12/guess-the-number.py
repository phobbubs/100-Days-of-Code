from art import logo
import random
print(logo)

game_end = False
correct_num = random.randint(1,100)
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
print(f"Psst the correct answer is {correct_num}.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

lives = 10
if difficulty == "easy":
    lives -= 0
elif difficulty == "hard":
    lives -= 5

while not game_end:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == correct_num:
        game_end = True
        print(f"YOU GOT IT! The answer was {correct_num}.")
    elif guess > correct_num:
        print("Too HIGH.")
        lives -= 1
    elif guess < correct_num:
        print("Too LOW.")
        lives -= 1
    
    if lives == 0:
        game_end = True
        print("You've run out of guesses, you LOSE.")
    
