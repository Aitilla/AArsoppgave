from morEng_translator import translateEnglish, translateMorse
from flask import Flask, request
from flask_cors import CORS

app = Flask('Translator')
CORS(app)
# Route should accept POST request type

@app.route('/englishToMorse', methods=['POST'])
def engToMorse():
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedEng = translateEnglish(inputValueEng=textInput)
    print(translatedEng)
    return translatedEng

@app.route('/morseToEng', methods=['POST'])
def morseToEng():
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedMorse = translateMorse(inputValueMorse=textInput)
    print(translatedMorse)
    return translatedMorse


if __name__ == '__main__':
    app.run(debug=True)