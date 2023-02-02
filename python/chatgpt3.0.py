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

def play_game():
    chosen_word = get_random_word()
    for i in range(ALLOWED_GUESSES):
        user_word = get_user_word()
        if user_word == chosen_word:
            print("You guessed correctly. The word was", chosen_word)
            return
        else:
            hint = get_hint(chosen_word, user_word)
            print("Incorrect. Here's a hint:", hint)
    print("You have exceeded the maximum number of allowed guesses. The word was", chosen_word)

if __name__ == "__main__":
    play_game()
