from morEng_translator import translateEnglish, translateMorse
from flask import Flask, request

app = Flask('Translator')

# Route should accept POST request type

@app.route('/englishToMorse', methods=['POST'])
def engToMorse():
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedEng = translateEnglish(inputValueEng=textInput)
    print(translatedEng)
    return {'output': translatedEng}

@app.route('/morseToEng', methods=['POST'])
def morseToEng():
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedMorse = translateMorse(inputValueMorse=textInput)
    print(translatedMorse)
    return {'output': translatedMorse}


if __name__ == '__main__':
    app.run(debug=True)