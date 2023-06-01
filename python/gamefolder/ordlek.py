#Libraries and wordlist
import random
from words import wordlist

#Maximum allowed guesses
ALLOWED_GUESSES = 6

#Gets word from wordlist
def get_random_word():
    return random.choice(wordlist)

#Gets the letter the player guesses
def get_user_word():
    user_word = input("Write a word with 4 letters: \n").upper()
    if len(user_word) != 4:
        print("The word must have 4 letters.")
        return get_user_word()
    return user_word

#Gets a hint
def get_hint(chosen_word, user_word):
    hint = ""
    for i in range(4):
        if user_word[i] == chosen_word[i]: #If a letter is correct placed prints the letter
            hint += user_word[i]
        else: #If letter is not correct prints * for incorrect
            hint += "*"
    for i in range(4): #Checks if letter is placed incorrectly
        if user_word[i] != chosen_word[i] and user_word[i] in chosen_word:
            hint = hint[:i] + "+" + hint[i+1:]
    return hint

#Makes you choose if you would like to play again or end the game
def endgame():
    print("\nWhat would you like to do now\n")
    end_Choice = input("Press 1 to play again\nPress 2 to quit the game:\n")
    if end_Choice == "1":
        play_game()
    elif end_Choice == "2":
        exit()
    elif end_Choice != 1 or end_Choice != 2:
        endgame()

#Plays the game
def play_game():
    chosen_word = get_random_word()
    for i in range(ALLOWED_GUESSES):
        user_word = get_user_word()
        if user_word == chosen_word: #Checks if everything is correct
            print("You guessed correctly. The word was", chosen_word)
            endgame()
        else: #If the word is incorrect i launch get_hint function
            hint = get_hint(chosen_word, user_word)
            print("Incorrect. Here's a hint:", hint)
    #If allowed guesses has been spent you lose and gets sent to engame
    print("You have exceeded the maximum number of allowed guesses. The word was", chosen_word)
    endgame()

#Tutorial of game
def tutorial():
    print("\nWELCOME TO MY WORD GUESSING GAME \n")
    print("The rules are simple \n")
    print("You have six guesses to guess a word, the word is four letters no more no less and you get hints for each guess")
    print("Letters that are in the word and correctly placed will be shown with the letter")
    print("Letters that are in the word but wrongly placed will be marked as a +")
    print("Letters which are not in the word will be marked with a * \n")
    choice()

#Makes you type 1 and press enter before you can start to guess. That way you can get a chance to read the tutorial before you start.
def choice():
    meny_Choice = input("Please type 1 and press enter to continue \n")
    if meny_Choice == "1":
        play_game()
    else:
        print("Incorrect input")
        choice()

#Starts the game
if __name__ == "__main__":
    tutorial()
