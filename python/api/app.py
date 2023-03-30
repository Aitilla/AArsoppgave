from morEng_translator import translateEnglish, translateMorse
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="10.226.248.5",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)


mycursor = mydb.cursor()


app = Flask('Translator')
CORS(app)
# Route should accept POST request type

@app.route('/englishToMorse', methods=['POST'])
def engToMorse():
    unix = time.time()
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedEng = translateEnglish(inputValueEng=textInput)
    print(translatedEng)

    sql = "INSERT INTO engToMorse (time, text, translated) VALUES (%s, %s, %s)"
    val = (unix, textInput, translatedEng)
    mycursor.execute(sql, val)
    mydb.commit()

    return translatedEng

@app.route('/morseToEng', methods=['POST'])
def morseToEng():
    unix = time.time()
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedMorse = translateMorse(inputValueMorse=textInput)
    print(translatedMorse)

    sql = "INSERT INTO MorseToEng (time, morseCode, translated) VALUES (%s, %s, %s)"
    val = (unix, textInput, translatedMorse)
    mycursor.execute(sql, val)
    mydb.commit()

    return translatedMorse


if __name__ == '__main__':
    app.run(debug=True)