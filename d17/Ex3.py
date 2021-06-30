import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="internship"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
