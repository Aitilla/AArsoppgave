import mysql.connector

mydb = mysql.connector.connect(
    host="10.226.248.5",
    port=3306,
    user="rar",
    password="raring",
    database="aarsoppgave"
)


mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM engToMorse")

myresult = mycursor.fetchall()

print(myresult)

for i in myresult:
    print(i)