import datetime
from datetime import datetime, timedelta
import mysql.connector
# from database_queries import update_database
import random
import string

mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password='root',
		database="martha"
		)

cursor = mydb.cursor()

week_con = 7
# for i in range(0, 7):
# 	today = datetime.today().date()
# 	over_days = week_con + today.weekday()
# 	last_mon = today - timedelta(days=over_days)
# 	last_week = last_mon + timedelta(days=i)
# 	print(last_week)

# print('\n')

# current_weekday = datetime.today().weekday() + 3
# for i in range(0, current_weekday):

# 	today = datetime.today().date() + timedelta(days=3)

# 	mon = today - timedelta(days=current_weekday)

# 	week_data = mon + timedelta(days=i)

# 	print(week_data)

from database_connection import db_connection_execute,db_connection_fetch

# today=datetime.today().date()
today=datetime(2011,4,11).date()
first_date=datetime(2011,1,3).date()
diff_date=today-first_date
open_list=close_list=[]
high,low=0,10000000000
query='SELECT `Date` from martha.nifty50'
dss=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
prev_day=0

for i in range(0,diff_date.days):
	
	date_to_print=first_date+timedelta(i)

	for j in dss:
		if date_to_print == j[0]:

			sql='SELECT Open, High, Low, Close from martha.nifty50 where `Date`= %s'
			value=(str(date_to_print),)
			cursor.execute(sql,value)
			vals=cursor.fetchone()
			date_weekday=date_to_print.weekday()
			# print(vals[0],vals[1],vals[2],vals[3],)


			if (prev_day==4 or prev_day==5 or prev_day==6) and date_weekday==0:

				print('Week high = ',high,' Week low = ',low)
				print('Week open = ',open_list[0],' Week close = ',close_list[-1])

				open_list=close_list=[]
				high,low=0,100000000000000

				print('open = ',open_list)
				print('close = ',close_list)
				print('high = ',high)
				print('low = ',low)
				
				open_list.append(vals[0])
				close_list.append(vals[3])
				
				if float(vals[1])>high:
					high=float(vals[1])
				
				if float(vals[2])<low:
					low=float(vals[2])
				
				print('\n')
				
			open_list.append(vals[0])
			close_list.append(vals[3])
			
			if float(vals[1])>high:
				high=float(vals[1])
			
			if float(vals[2])<low:
				low=float(vals[2])

			


				
			print('day = ',date_to_print)
			prev_day=date_weekday

			