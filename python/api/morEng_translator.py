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

def translateEnglish(inputValueEng: str):
    englishLetter = inputValueEng.lower()
    engMorse = getMorse()
    morse = ''
    for i in englishLetter:
        morse += engMorse[i] + ' '
    return morse

def translateMorse(inputValueMorse: str):
    morseLetter = inputValueMorse.lower().split()
    morseEng = getEnglish()
    english = ''
    for i in morseLetter:
        english += morseEng[i]
    return english