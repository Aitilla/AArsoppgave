import random
from termcolor import colored

def play_game():
    wordlist = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY"]
    allowed_guesses = 6
    chosen_word = random.choice(wordlist)
    user_word = ""
    
    while allowed_guesses > 0 and user_word != chosen_word:
        user_word = input("Enter a word with 4 letters: ").upper()
        hints = ""
        for i in range(4):
            if user_word[i] == chosen_word[i]:
                hints += colored(user_word[i], "green")
            elif user_word[i] in chosen_word:
                hints += colored(user_word[i], "yellow")
            else:
                hints += colored(user_word[i], "red")
        print(hints)
        allowed_guesses -= 1
        
    if user_word == chosen_word:
        print(f"You guessed correctly. The word was {colored(chosen_word, 'green')}")
    else:
        print(f"Try again tomorrow. The word was {colored(chosen_word, 'green')}")
        
if __name__ == "__main__":
    play_game()
