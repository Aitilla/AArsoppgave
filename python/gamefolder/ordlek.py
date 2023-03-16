import random
from words import wordlist

ALLOWED_GUESSES = 6

def get_random_word():
    return random.choice(wordlist)

def get_user_word():
    user_word = input("Write a word with 4 letters: \n").upper()
    if len(user_word) != 4:
        print("The word must have 4 letters.")
        return get_user_word()
    return user_word

def get_hint(chosen_word, user_word):
    hint = ""
    for i in range(4):
        if user_word[i] == chosen_word[i]:
            hint += user_word[i]
        else:
            hint += "*"
    for i in range(4):
        if user_word[i] != chosen_word[i] and user_word[i] in chosen_word:
            hint = hint[:i] + "+" + hint[i+1:]
    return hint

def endgame():
    print("\nWhat would you like to do now\n")
    end_Choice = input("Press 1 to play again\nPress 2 to quit the game:\n")
    if end_Choice == "1":
        play_game()
    elif end_Choice == "2":
        exit()
    elif end_Choice != 1 or end_Choice != 2:
        endgame()

def play_game():
    chosen_word = get_random_word()
    for i in range(ALLOWED_GUESSES):
        user_word = get_user_word()
        if user_word == chosen_word:
            print("You guessed correctly. The word was", chosen_word)
            endgame()
        else:
            hint = get_hint(chosen_word, user_word)
            print("Incorrect. Here's a hint:", hint)
    print("You have exceeded the maximum number of allowed guesses. The word was", chosen_word)
    endgame()

def tutorial():
    print("\nWELCOME TO MY WORD GUESSING GAME \n")
    print("The rules are simple \n")
    print("You have six guesses to guess a word, the word is four letters no more no less and you get hints for each guess")
    print("Letters that are in the word and correctly placed will be shown with the letter")
    print("Letters that are in the word but wrongly placed will be marked as a +")
    print("Letters which are not in the word will be marked with a * \n")
    choice()

def choice():
    meny_Choice = input("Please type 1 and press enter to continue \n")
    if meny_Choice == "1":
        play_game()
    else:
        print("Incorrect input")
        choice()

if __name__ == "__main__":
    tutorial()
