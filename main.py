import random

# Predefined list of five-letter words
WORD_LIST = ["apple", "table", "plant", "chair", "stone", "grape", "beach", "track", "fence", "world", "blood"]

def choose_word():
    return random.choice(WORD_LIST)

def check_guess(guess, secret):
    feedback = ["⬛"] * len(guess)  # Default feedback
    secret_letters = list(secret)
    guess_used = [False] * len(guess)

    # First pass: Check for correct letters in the correct positions (🟩)
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback[i] = "🟩"
            secret_letters[i] = None  # Mark this letter as used in the secret
            guess_used[i] = True      # Mark this letter as used in the guess

    # Second pass: Check for correct letters in the wrong positions (🟨)
    for i in range(len(guess)):
        if not guess_used[i] and guess[i] in secret_letters:
            feedback[i] = "🟨"
            secret_letters[secret_letters.index(guess[i])] = None  # Mark as used

    return ''.join(feedback)
    
def wordle_game():
    secret_word = choose_word()
    attempts = 6
    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    print("🟩: Correct letter in the correct position.")
    print("🟨: Correct letter in the wrong position.")
    print("⬛: Letter not in the word.")
    print()

    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}/6: Enter your 5-letter guess: ").lower()
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue

        feedback = check_guess(guess, secret_word)
        print("Feedback:", feedback)

        if guess == secret_word:
            print("Congratulations! You guessed the word!")
            break

        attempts -= 1

    if attempts == 0 and guess != secret_word:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    wordle_game()
