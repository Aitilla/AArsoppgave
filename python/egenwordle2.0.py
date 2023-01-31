#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin

import random
from words import wordlist
from termcolor import colored
from threading import Timer


allowed_guesses = 6

def callChosen():
    global chosenWord
    chosenWord = random.choice(wordlist)
    print(chosenWord)
    Timer(20, callChosen).start()
    Timer(20, checkWord).start()

def checkWord(): 
    global allowed_guesses
    global userWord
    userWord = input("Write a word with 4 letters: \n").upper()
    if(userWord == chosenWord):
        print("You guessed correctly. Come back tomorrow for a new word. The word was", colored(chosenWord, 'green'))
    else:
        if allowed_guesses <= 1:
            print("Try again tomorrow. The word was", colored(chosenWord, 'green'))
            exit()
        else:    
            for letter in userWord:
                if letter == chosenWord[0] or letter == chosenWord[1] or letter == chosenWord[2] or letter == chosenWord[3]:
                    print(letter)
                    allowed_guesses = allowed_guesses -1
                    print("You have", allowed_guesses, "guesses left.")
                    checkWord()
                else:
                    print(colored(userWord, 'red'))
                    allowed_guesses = allowed_guesses -1
                    print("You have", allowed_guesses, "guesses left.")
                    checkWord()


callChosen()
checkWord()

#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin