import random

print("Welcome to HANGMAN!!!,\nTry not to get HANGED!!!")
words = ["television", "capital", "jupiter", "crop", "nigeria"]

def guess():
    lives = 5
    word_to_guess = random.choice(words)
    word_letters = list(word_to_guess)
    guessed = "_" * len(word_to_guess)
    print(word_to_guess)
    guessed_letters = []
    correctly_guessed_letters = list(guessed)
    while "_" in guessed and lives > 0:
        print(guessed)
        player_guess = input("Guess a letter:")
        if player_guess in word_letters:
            for letter in word_letters:
                letter_index = word_letters.index(letter)
                if player_guess == letter:
                    correctly_guessed_letters[letter_index] = player_guess
                    word_letters[letter_index] = "_"
                    guessed ="".join(correctly_guessed_letters)
            guessed_letters.append(player_guess)
        elif player_guess in guessed_letters:
            print("you already guessed this letter, Try another letter")
            guessed_letters.append(player_guess)
        else:
            lives -= 1
            if lives > 0:
                print(f"oops!! You are {lives} wrong guesses away from being hanged")
            else:
                print("You have been hanged, OLODO!!!")
                restart = input("Continue playing?: y or n:").lower()
                if restart == "y":
                    guess()
            guessed_letters.append(player_guess)

guess()






