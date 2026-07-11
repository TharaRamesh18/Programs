import random

words = ["apple", "tiger", "house", "river", "chair"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_attempts:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()
   
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Attempts left:", max_attempts - incorrect_guesses)

else:
    print("\nGame Over!")
    print("The word was:", word)