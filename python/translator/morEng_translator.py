def getMorse():
    engMorse={    
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",    
        "e": ".", "f": "..-.", "g": "--.", "h": "....",   
        "i": "..", "j": ".---", "k": "-.-", "l": ".-..",    
        "m": "--", "n": "-.", "o": "---", "p": ".--.",    
        "q": "--.-", "r": ".-.", "s": "...", "t": "-",    
        "u": "..-", "v": "...-", "w": ".--", "x": "-..-",    
        "y": "-.--", "z": "--..", "1": ".----", "2": "..---",    
        "3": "...--", "4": "....-", "5": ".....", "6": "-....",    
        "7": "--...", "8": "---..", "9": "----.", "0": "-----",
        " ": "/"
        }
    return engMorse 

def getEnglish():
    morseEng={
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d",
        ".": "e", "..-.": "f", "--.": "g", "....": "h",
        "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
        "--": "m", "-.": "n", "---": "o", ".--.": "p", 
        "--.-": "q", ".-.": "r", "...": "s", "-": "t", 
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x", 
        "-.--": "y", "--..": "z", "-----": "0", ".----": "1", 
        "..---": "2", "...--": "3", "....-": "4", ".....": "5", 
        "-....": "6", "--...": "7", "---..": "8", "----.": "9", 
        "/": " ", " ": ""
    }
    return morseEng

def translateEnglish():
    englishLetter = input('Please type what you would like to translate in English\n')
    engMorse = getMorse()
    for i in englishLetter:
        print(engMorse[i].__add__(' '), end = '')

def translateMorse():
    morseLetter = input('Please type what you would like to translate in Morse code\n').split()
    morseEng = getEnglish()
    for i in morseLetter:
        print(morseEng[i], end = '')


while True:
    translatorChoice = input('\nType 1 if you would like to translate from English to Morse code\n'
                             'Type 2 if you would like to translate from Morse code to English\n')

    if translatorChoice == '1':
        translateEnglish()
    elif translatorChoice == '2':
        translateMorse()















# def getMorse():
#     engMorse={    
#         "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",    
#         "e": ".", "f": "..-.", "g": "--.", "h": "....",   
#         "i": "..", "j": ".---", "k": "-.-", "l": ".-..",    
#         "m": "--", "n": "-.", "o": "---", "p": ".--.",    
#         "q": "--.-", "r": ".-.", "s": "...", "t": "-",    
#         "u": "..-", "v": "...-", "w": ".--", "x": "-..-",    
#         "y": "-.--", "z": "--..", "1": ".----", "2": "..---",    
#         "3": "...--", "4": "....-", "5": ".....", "6": "-....",    
#         "7": "--...", "8": "---..", "9": "----.", "0": "-----",
#         " ": "/"
#         }
#     return engMorse 

# def getEnglish():
#     morseEng={}
#     morseEng = getMorse()
#     for key in morseEng:
#         val = morseEng[key]
#         morseEng[val] = key
#     return morseEng

# def translateMorse():
#     morseEng = getEnglish()

#     for i in userWord:
#         print(morseEng[i], end = '')

# def translateEng():
#     engMorse = getMorse()

#     for i in userWord:
#         print(engMorse[i].__add__(' '), end = '')

# userWord = input('\nPlease type what you want to translate\n')
# engMorse = getMorse()

# if userWord[0] in engMorse.values():
#     translateMorse()
# else:
#     translateEng()





# morseMor={
#     ".- ": "a", "-... ": "b", "-.-. ": "c", "-.. ": "d",
#     ". ": "e", "..-. ": "f", "--. ": "g", ".... ": "h",
#     ".. ": "i", ".--- ": "j", "-.- ": "k", ".-.. ": "l",
#     "-- ": "m", "-. ": "n", "--- ": "o", ".--. ": "p", 
#     "--.- ": "q", ".-. ": "r", "... ": "s", "- ": "t", 
#     "..- ": "u", "...- ": "v", ".-- ": "w", "-..- ": "x", 
#     "-.-- ": "y", "--.. ": "z", "----- ": "0", ".---- ": "1", 
#     "..--- ": "2", "...-- ": "3", "....- ": "4", "..... ": "5", 
#     "-.... ": "6", "--... ": "7", "---.. ": "8", "----. ": "9", 
#     "/ ": " "
# }