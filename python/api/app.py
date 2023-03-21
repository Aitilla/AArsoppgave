from morEng_translator import translateEnglish, translateMorse
from flask import Flask

app = Flask('Translator')

# Route should accept POST request type

# @app.route('/englishToMorse', methods=['POST'])
# def engToMorse():
#     # get text from request
#     # pass text to translate function
#     return translateEnglish()

@app.route('/englishToMorse', methods=['POST'])
def engToMorse():
    inputValue = request.form['input']
    morseLetter, time_taken = translateEnglish(inputValue)
    return {'output': morseLetter, 'time': time_taken}

# @app.route('/morseToEng', methods=['POST'])
# def morseToEng():
#     return translateMorse()

@app.route('/morseToEng', methods=['POST'])
def morseToEng():
    inputValue = request.form['input']
    englishLetter, time_taken = translateMorse(inputValue)
    return {'output': englishLetter, 'time': time_taken}


if __name__ == '__main__':
    app.run(debug=True)