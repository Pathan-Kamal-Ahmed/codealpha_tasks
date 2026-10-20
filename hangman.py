
import random

# List of 5 predefined words
words = ["python", "computer", "developer", "program", "hangman"]

# Select one random word
secret_word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Count incorrect guesses
incorrect_guesses = 0
max_incorrect_guesses = 6

print("===== WELCOME TO HANGMAN =====")
print("Guess the hidden word one letter at a time!")
print("You can make only 6 incorrect guesses.")

while incorrect_guesses < max_incorrect_guesses:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check whether the player has guessed the whole word
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    # Ask the player to guess a letter
    guess = input("Enter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the letter exists in the word
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses,
              "/", max_incorrect_guesses)

# Display the result if all incorrect guesses are used
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame over! You lost.")
    print("The correct word was:", secret_word)
