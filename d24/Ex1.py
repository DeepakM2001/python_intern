
import json
json_data=[
    {'name':"deepak",'age':21,'Permanent_staff':True,'salary':22.00,'dept_desgn':'md'},
     {'name':"chadru",'age':35,'Permanent_staff':False,'salary':36.00,'dept_desgn':"ceo"}]
    

res =json.dumps(json_data)


import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="json"
)

dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)
