from art import logo
import random
print(logo)

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def check_answer(guess, correct_num, lives):
    """Check guess against correct_num. Returns number of lives remaining."""
    if guess == correct_num:
        print(f"YOU GOT IT! The answer was {correct_num}.")
    elif guess > correct_num:
        print("Too HIGH.")
        return lives - 1
    elif guess < correct_num:
        print("Too LOW.")
        return lives - 1

def set_difficulty():
    global lives
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_LIVES
    elif difficulty == "hard":
        return HARD_LEVEL_LIVES

def game():
    correct_num = random.randint(1,100)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    #print(f"Psst the correct answer is {correct_num}.")
    
    lives = set_difficulty()
    
    guess = 0
    
    while guess != correct_num:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, correct_num, lives)
        if lives == 0:
            print("You've run out of guesses, you LOSE.")
            return #exit and end function
        elif guess != correct_num:
            print("Guess again.")
            
game()
