import random

word_list = ["apple", "banana", "pineapple", "kiwi", "oranges"]

word = random.choice(word_list)

def check_guess(guess):
    letter = guess.lower()
    if letter in word:
        print(f"Good guess, {letter} is in the word.")
    else:
        print(f"Sorry {letter} is not in the word.")

def ask_for_input():
    while True:
        guess = input("guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()