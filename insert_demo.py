import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="martha",
  #auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
n='carry'
#empid,name,surname,age=45,'kk','ok',26
# sql = "INSERT INTO employee (name) VALUES (%s)"
# values='&n';
# mycursor.execute(sql,values)
# mydb.commit()

sql = "UPDATE employee set age= %s where name= %s"
values=(30,n)
mycursor.execute(sql,values)
mydb.commit()
