#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin

import random
from python.words import wordlist
from termcolor import colored


allowed_guesses = 6

def callChosen():
    global chosenWord
    chosenWord = random.choice(wordlist)
    print(chosenWord)

def checkWord():
    global userWord
    userWord = input("Skriv et ord på 4 bokstaver").upper()
    for letters in userWord:
        print(letters)

callChosen()
checkWord()

#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin