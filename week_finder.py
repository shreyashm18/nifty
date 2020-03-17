from database_connection import db_connection_execute,db_connection_fetch
import mysql.connector

day_list=[]
date_list=[]
open_list=[]
close_list=[]
highest_of_week=0
lowest_of_week=1000000000

query="""SELECT Sr FROM nifty50 """

result=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
for i in range(1,50):
	query='SELECT `Date`, `Day`, Open, High, Low, Close from martha.nifty50 where Sr= {}'.format(i)
	day=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 1)
	# print(day[1])
	if day[1] not in day_list:

		if float(day[3])>highest_of_week:
			highest_of_week=float(day[3])
		
		if float(day[4])<lowest_of_week:
			lowest_of_week=float(day[4])
		
		day_list.append(day[1])
		date_list.append(day[0])
		open_list.append(day[2])
		close_list.append(day[5])
	
	else:
		for days in range(len(day_list)):
			print(day_list[days]+' '+str(date_list[days]))
		print('Week high = ',highest_of_week,' Week low = ',lowest_of_week)
		print('Week open = ',float(open_list[0]),' Week close = ',float(close_list[-1]))
		print('\n')
		day_list=[]
		date_list=[]
		open_list=[]
		close_list=[]
		highest_of_week=0
		lowest_of_week=1000000000
		day_list.append(day[1])
		date_list.append(day[0])
		open_list.append(day[2])
		close_list.append(day[5])
		if float(day[3])>highest_of_week:
			highest_of_week=float(day[3])
		
		if float(day[4])<lowest_of_week:
			lowest_of_week=float(day[4])