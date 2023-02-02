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

def play_game():
    chosen_word = get_random_word()
    for i in range(ALLOWED_GUESSES):
        user_word = get_user_word()
        if user_word == chosen_word:
            print("You guessed correctly. The word was", chosen_word)
            return
        else:
            print("Incorrect. Try again.")
    print("You have exceeded the maximum number of allowed guesses. The word was", chosen_word)

if __name__ == "__main__":
    play_game()