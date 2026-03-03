import random

def guess_the_word_game():
    words = ["python", "developer", "coding", "challenge", "game"]
    word = random.choice(words)
    guessed_letters = ["_" for _ in word]
    attempts = 6
    guessed_correctly = False

    print("Welcome to Guess the Word Game!")

    while attempts > 0 and "_" in guessed_letters:
        print("\nWord: ", " ".join(guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower() # Ensure input is lowercase

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in [l for l in word if l in guessed_letters]:
            print(f"You already guessed '{guess}'.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Incorrect! '{guess}' is not in the word.")

    print("\n--- Game Over ---")
    if "_" not in guessed_letters:
        print("Congrats! You found the word:", word)
    else:
        print("You ran out of attempts! The word was:", word)

# Run the game
if __name__ == "__main__":
    guess_the_word_game()
