import random
from termcolor import colored

def play_game():
    wordlist = ["APPLE", "BALL", "CAT", "DOG", "EGGS"]
    allowed_guesses = 6
    chosen_word = random.choice(wordlist)
    user_word = ""
    
    while allowed_guesses > 0 and user_word != chosen_word:
        user_word = input("Enter a 4 letter word: ").upper()
        if len(user_word) != 4:
            print("Please enter a 4 letter word.")
            continue
        
        correct_positions = 0
        for i in range(4):
            if user_word[i] == chosen_word[i]:
                correct_positions += 1
        
        if correct_positions == 4:
            print(f"You won! The word was {colored(chosen_word, 'green')}")
            break
        else:
            print(f"{correct_positions}/4 letters are in the correct position.")
            allowed_guesses -= 1
    
    if allowed_guesses == 0:
        print(f"You lost! The word was {colored(chosen_word, 'green')}")

if __name__ == "__main__":
    play_game()
