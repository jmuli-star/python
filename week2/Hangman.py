import random

# List of words for the Hangman game
words = ["python", "hangman", "developer", "programming", "challenge", "keyboard"]

# Select a random word
word_to_guess = random.choice(words).lower()
word_display = ["_"] * len(word_to_guess)  # Convert word to dashes
attempts_left = 6
guessed_letters = set()

print("Welcome to Hangman! Try to guess the word.")

# Game loop
while attempts_left > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    # Add guess to guessed letters set
    guessed_letters.add(guess)

    # Check if the guessed letter is in the word
    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Oops! '{guess}' is not in the word.")
        attempts_left -= 1

# Final game outcome
if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)
