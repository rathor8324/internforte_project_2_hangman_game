import random

# List of secret words with hints
word_list = [
    {"word": "apple", "hint": "A common fruit."},
    {"word": "banana", "hint": "Yellow and long."},
    {"word": "cherry", "hint": "Small and red."},
    {"word": "date", "hint": "Sweet and brown."},
    {"word": "fig", "hint": "Fruit with a unique texture."},
    {"word": "grape", "hint": "Comes in bunches."},
    {"word": "kiwi", "hint": "Fuzzy brown skin."},
    {"word": "lemon", "hint": "Sour and yellow."},
    {"word": "mango", "hint": "Tropical and sweet."},
    {"word": "orange", "hint": "A citrus fruit."},
]

# Function to choose a random word with a hint from the list
def choose_word(word_list):
    word_info = random.choice(word_list)
    return word_info["word"], word_info["hint"]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
def hangman():
    word_to_guess, hint = choose_word(word_list)
    guessed_letters = []
    max_attempts = len(word_to_guess) + 2
    attempts = 0

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")
    print(f"You have {max_attempts} chances to guess the word.")

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Good guess!")
            else:
                print("Incorrect guess. Try again.")
                attempts += 1

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Out of chances! The word was:", word_to_guess)

# Play the game in a loop
while True:
    hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
