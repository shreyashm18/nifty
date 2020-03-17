import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="martha",
  #auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (empid int, name VARCHAR(255), address VARCHAR(255), salary int)")

sql = "INSERT INTO employee (id, name, surname, age) VALUES (15,'kishor', 'binwade', 23)"


mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount," record inserted")