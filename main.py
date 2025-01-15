import random

# Predefined list of five-letter words
WORD_LIST = ["apple", "table", "plant", "chair", "stone", "grape", "beach", "track", "fence", "world"]

def choose_word():
    return random.choice(WORD_LIST)

def check_guess(guess, secret):
    feedback = []
    secret_letters = list(secret)
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback.append("🟩")  # Correct letter in the correct position
            secret_letters[i] = None  # Mark this letter as used
        elif guess[i] in secret_letters:
            feedback.append("🟨")  # Correct letter in the wrong position
            secret_letters[secret_letters.index(guess[i])] = None
        else:
            feedback.append("⬛")  # Letter not in the word
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
