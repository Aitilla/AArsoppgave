import random
from words import wordlist
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
