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
    global userWord
    userWord = input("Write a word with 4 letters: \n").upper()
    if(userWord == chosenWord):
        print("You guessed correctly. Come back tomorrow for a new word. The word was", colored(chosenWord, 'green'))
    else:
        for letters in userWord:
            if letters[0] == chosenWord[1] or chosenWord[2] or chosenWord[3]:
                print(letters[0])

callChosen()
checkWord()

#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin