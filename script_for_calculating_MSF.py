import mysql.connector
from database_connection import db_connection_execute,db_connection_fetch
from msf_color import colour_finding
from director_pattern import JGD_JWD_finder

zig_zag_box=False
zig_zag_list=[]


def pattern_finder(i):
	print('in pattern_finder')
	query = """SELECT `RANGE (HIGH - LOW)`, High, Low from nifty50 where Sr={}""".format(i[0])
	value=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type=1)
	#print(value)
	number=value[0]
	high=float(value[1])
	low=float(value[2])
	JGD_JWD_finder(number*(38.2/100),0.05,high,low,i[0])

def range_calculation(i):
	print("in range_cal")
	query = """	UPDATE martha.nifty50
				SET `RANGE (HIGH - LOW)` =High-Low
				WHERE Sr = {};""".format(i[0])
	db_connection_execute("localhost", "root", "root", "martha", query)

def msf_c(i):
	global zig_zag_box,zig_zag_list
	
	print("in msf_c")
	# print(result)
	
	if i[0]==1 or i[0]==2:
		query = """UPDATE martha.nifty50 SET Colour = 'NA' where Sr={}""".format(i[0])
		db_connection_execute("localhost", "root", "root", "martha", query)
		range_calculation(i)

	else:
		query = """SELECT Colour from nifty50 where Sr={}""".format((i[0])-1)
		last_colour=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 1)
		last_colour=last_colour[0]

		query="SELECT MSF from nifty50 where Sr between {} and {} ".format((i[0])-2,(i[0]))
		last_tow_msf= db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
		first,second,current_msf=last_tow_msf[0][0],last_tow_msf[1][0],last_tow_msf[2][0]
		#print('first = ',first,' second = ',second,' current msf = ',current_msf)

		zig_zag_box,zig_zag_list = colour_finding(current_msf,first,second,last_colour,zig_zag_box,zig_zag_list)
		range_calculation(i)

def msf_f():
	print("in msf_f")
	query = """UPDATE martha.nifty50
							SET MSF = ( @msf := CASE WHEN msf IS NULL and Sr = 1
							THEN Close
							When msf IS NULL and Sr > 1
							THEN (Close - @msf) * 0.33 + @msf
							ELSE msf
							END )
							ORDER BY Sr;""" 

	db_connection_execute("localhost", "root", "root", "martha", query)

	# query="""SELECT count(Open) FROM nifty50"""

	# row_num=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
		
	query="""SELECT Sr FROM nifty50 """

	result=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
	# print(result)
	for i in result:
		msf_c(i)
		pattern_finder(i)















