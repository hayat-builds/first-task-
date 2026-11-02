himport random

def play_hangman():
    # 1. Predefined list of 5 words (as required by CodeAlpha)
    words = ["python", "developer", "internship", "github", "code"]
    secret_word = random.choice(words).lower()
    
    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    print("--- CodeAlpha Hangman Game ---")
    print("Guess the word one letter at a time.\n")

    # Game loop
    while incorrect_guesses < max_attempts:
        # Build current state of the guessed word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"Word: {display_word.strip()}")
        print(f"Incorrect guesses remaining: {max_attempts - incorrect_guesses}")
        
        # Check for win condition
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            return

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try again!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # If lost
    print(f"\nGame Over! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()