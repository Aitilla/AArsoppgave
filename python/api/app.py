#Libraies and imports from other files
from morEng_translator import translateEnglish, translateMorse
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import time
import pandas as pd

#Database connection
mydb = mysql.connector.connect(
    host="10.2.1.211",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)

mycursor = mydb.cursor()

#Get everthing from engToMorse table in database
mycursor.execute("Select * from engToMorse")

myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=['time', 'text', 'translated'])
print(df) #print all from engToMorse table

#Removes CORS protection for my api so i can send information between files on a webpage
app = Flask('Translator')
CORS(app)

#Get info from webpage sends to translator and sends result back
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

#Get info from webpage sends to translator and sends result back
@app.route('/morseToEng', methods=['POST'])
def morseToEng():
    unix = time.time()
    textInput = request.get_data(as_text=True)
    print(textInput)
    translatedMorse = translateMorse(inputValueMorse=textInput)
    print(translatedMorse)

    sql = "INSERT INTO morseToEng (time, morseCode, translated) VALUES (%s, %s, %s)"
    val = (unix, textInput, translatedMorse)
    mycursor.execute(sql, val)
    mydb.commit()

    return translatedMorse

#Calls the program and start the program
if __name__ == '__main__':
    app.run(debug=True)