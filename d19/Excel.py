import openpyxl
import mysql.connector as mysql
path = "students.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active


mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="student_data"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
