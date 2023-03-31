#Hangman Game 
import random

# Define the list of words
words = ['technical']

# Select a random word
word = random.choice(words)

# Initialize the game
guesses = []
max_guesses = 6
secret_word = ['_'] * len(word)

while True:
    # Display the secret word
    print(' '.join(secret_word))

    # Get the user's guess
    guess = input('Enter a letter: ').lower()

    # Check if the guess is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                secret_word[i] = guess
        print('Correct!')
        print('--------------------------------------------')
    else:
        guesses.append(guess)
        print('Incorrect.')
        print('--------------------------------------------')
        print(f'Guesses remaining: {max_guesses - len(guesses)}')

    # Check if the game is over
    if '_' not in secret_word:
        print('Congratulations! You guessed the word.')
        print('--------------------------------------------')
        print(f'The word was {word}.')
        break
    elif len(guesses) >= max_guesses:
        print('Game over. You ran out of guesses.')
        print('--------------------------------------------')
        print(f'The word was {word}.')
        break
