from morEng_translator import translateEnglish, translateMorse
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import time
import pandas as pd

mydb = mysql.connector.connect(
    host="10.226.248.5",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)

mycursor = mydb.cursor()


mycursor.execute("Select * from engToMorse")

myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=['time', 'text', 'translated'])
print(df)

app = Flask('Translator')
CORS(app)

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

    sql = "INSERT INTO morseToEng (time, morseCode, translated) VALUES (%s, %s, %s)"
    val = (unix, textInput, translatedMorse)
    mycursor.execute(sql, val)
    mydb.commit()

    return translatedMorse


if __name__ == '__main__':
    app.run(debug=True)


    
# try:
#     mydb = mysql.connector.connect(host="10.226.248.5", port=3306, database = 'aarsoppgave',user="rar", passwd="raring")
#     query = "Select * from studentdetails;"
#     result_dataFrame = pd.read_sql(query,mydb)
#     mydb.close() #close the connection
# except Exception as e:
#     mydb.close()
#     print(str(e))
