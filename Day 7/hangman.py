import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print (logo)
#testing code
#print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}, try another letter.")
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word, you lose one life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
