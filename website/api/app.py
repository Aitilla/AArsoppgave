from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="10.2.1.211",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)

mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

mycursor.execute("Select * from users")

myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=['userID', 'username', 'password'])
print(df)

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    username = data['username']
    password = data['password']
    print(username)
    print(password)

    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    response = jsonify({"message": "User created"})
    return response

if __name__ == '__main__':
    app.run(debug=True)
