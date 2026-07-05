import random

def play_hangman():
    # 1. Create a list of 5 predefined words
    word_list = ['python', 'intern', 'coding', 'alpha', 'script']
    
    # 2. Let the computer pick a random word from the list
    secret_word = random.choice(word_list)
    
    # 3. Create a list of underscores to represent the hidden letters
    # Example: If the word is "python", this creates ['_', '_', '_', '_', '_', '_']
    guessed_word = ['_'] * len(secret_word)
    
    incorrect_guesses = 0
    max_attempts = 6
    guessed_letters = [] # To keep track of letters the user has already tried

    print("Welcome to the CodeAlpha Hangman Game!")

    # 4. The game loop runs as long as they have attempts left AND there are still hidden letters
    while incorrect_guesses < max_attempts and '_' in guessed_word:
        # Display the current state of the word
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        # Get the user's guess
        guess = input("Guess a single letter: ").lower()

        # Input validation: check if it's a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
            continue

        # Add the valid guess to our tracked list
        guessed_letters.append(guess)

        # 5. Check if the guess is in the secret word
        if guess in secret_word:
            print("Great guess!")
            # Update the underscores with the correctly guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

    # 6. End of game conditions (Win or Lose)
    if '_' not in guessed_word:
        print(f"\nCongratulations! You successfully guessed the word: {secret_word}")
    else:
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")

# Run the game
play_hangman()