import mysql.connector

def db_connection_execute(Hostname, User, Pw, Db, query, values=0):
	mydb = mysql.connector.connect(
		host=Hostname,
		user=User,
		password=Pw,
		database=Db
		)
	# print('inside db_connection_execute')
	cursor = mydb.cursor()

	sql_query = query
	values = values

	if values == 0:
		cursor.execute(sql_query)

	else:
		cursor.execute(sql_query,values)

	mydb.commit()

def db_connection_fetch(Hostname, User, Pw, Db, query, fetch_type):
	mydb = mysql.connector.connect(
		host=Hostname,
		user=User,
		password=Pw,
		database=Db
		)

	cursor = mydb.cursor()

	sql_query=query

	cursor.execute(sql_query)

	if fetch_type == 1:
		result=cursor.fetchone()

	else:
		result=cursor.fetchall()		

	return result
