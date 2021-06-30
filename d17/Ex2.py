import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="internship"
)
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
