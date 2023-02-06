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
    if allowed_guesses <= 1:
        print("Try again tomorrow. The word was", colored(chosenWord, 'green'))
        exit()
    elif(userWord == chosenWord):
            print("You guessed correctly. Come back tomorrow for a new word. The word was", colored(chosenWord, 'green'))
    else:   
        for x in userWord:
            for i in chosenWord:
                if(i == x):
                    print(colored(x, 'green'))
                else:
                    print(x)



callChosen()
checkWord()

#OBS alt i denne filen er hvordan jeg skal starte på aarsoppgaven min andre termin