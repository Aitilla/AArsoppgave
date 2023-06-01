#Libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd
import re

#Connects to database
mydb = mysql.connector.connect(
    host="10.2.1.211",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)

mycursor = mydb.cursor()

mycursor.execute("Select * from users")

#Gets information from database prints startup
myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=['ID', 'username', 'password'])
print(df)

#Removes CORS protection for my api so i can send information between files on a webpage
app = Flask(__name__)
CORS(app)

#Gets information from website and creates a user if met criteria
@app.route('/createUser', methods=['POST'])
def create():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    result = mycursor.fetchone()
    if result:
        return ("Username already exists.")

    # Check if password contains at least one number and one character
    if not (re.search(r'\d', password) and re.search(r'[a-zA-Z]', password)):
        return ("Password must contain at least one number and one character.")

    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify({'message': 'User created'})

#Gets information from website and authorieses user for login
@app.route('/loginUser', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    mycursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
    user = mycursor.fetchone()

    if user:
        # User exists, login successful
        return {'message': 'Login successful'}
    else:
        # User does not exist or invalid credentials
        return {'error': 'Wrong username or password'}

#Starts the script
if __name__ == '__main__':
    app.run(debug=True, port=5001)
