import random
import string

from words import words
from diagrams_hanged import life_dictionary_visual

def get_valid_word(words):
    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hanged():
    print("======================")
    print(" Welcome to the game!")
    print("======================")

    word = get_valid_word(words)

    letters_to_guess = set(word)
    guessed_letters = set()
    abecedary = set(string.ascii_uppercase)


    hearts = 7

    while len(letters_to_guess) > 0 and hearts > 0:
        print(f"You have {hearts} hearts and you said this letters: {' '.join(guessed_letters)}")
        letters_shown = [letter if letter in guessed_letters
        else '-' for letter in word]
        print(life_dictionary_visual[hearts])
        print(f"word: {' '.join(letters_shown)}")

        user_letter = input("Say a letter: ").upper()
        if user_letter in abecedary - guessed_letters:
            guessed_letters.add(user_letter)

            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter)
                print('')
            else:
                hearts -= 1
                print(f"\nYour letter, {user_letter} isn't in the word")
        elif user_letter in guessed_letters:
            print("\nYou have already choose that letter. Please, choose another letter")
        else:
            print("\nThis letter isn't valid")


    if hearts == 0:
        print(life_dictionary_visual[hearts])
        print(f"Hanged! You lose. The word was: {word}")
    else:
        print(f"Nice! You guess the word {word}!")

hanged()