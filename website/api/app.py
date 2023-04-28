from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd
import re

mydb = mysql.connector.connect(
    host="10.2.1.211",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)

mycursor = mydb.cursor()

mycursor.execute("Select * from users")

myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=['time', 'text', 'translated'])
print(df)

app = Flask(__name__)
CORS(app)

@app.route('/createUser', methods=['POST'])
def create():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    result = mycursor.fetchone()
    if result:
        return "Username already exists."

    # Check if password contains at least one number and one character
    if not (re.search(r'\d', password) and re.search(r'[a-zA-Z]', password)):
        return "Password must contain at least one number and one character."

    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify({'message': 'User created'})


if __name__ == '__main__':
    app.run(debug=True)
