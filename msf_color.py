import mysql.connector
from database_connection import db_connection_execute,db_connection_fetch

# zig_zag_box=False
# zig_zag_list=[]

def colour_finding(msf,first,second,last_colour,zig_zag_box,zig_zag_list):

	ch=''
	if not zig_zag_box:
		
		if msf>first and msf>second:
			ch='G'
		
		elif msf<first and msf<second:
			ch='R'
		
		elif first < msf < second or first > msf > second:
			#print('zig-zig')
			if last_colour=='G':
					ch='Z_G'
			elif last_colour=='R':
					ch='Z_R' 
			zig_zag_box=True
			zig_zag_list=[first,second]
		
		query="""UPDATE martha.nifty50 set Colour = %s where MSF = %s"""
		value=(ch,msf)
		# print('msf = ',msf,' ch = ',ch,' last color = ',last_colour)
		db_connection_execute("localhost", "root", "root", "martha", query, values = value)
		
		return zig_zag_box,zig_zag_list

	else:
		first,second=zig_zag_list[0],zig_zag_list[1]
		print('elif : first and second = ',first,' ',second)
		if msf>first and msf>second:
			ch='G'
			zig_zag_box=False
			zig_zag_list=[]
		
		elif msf<first and msf<second:
			ch='R'
			zig_zag_box=False
			zig_zag_list=[]
		
		elif first < msf < second or first > msf > second:
			
			if last_colour=='G' or last_colour=='Z_G':
					ch='Z_G'
			elif last_colour=='R' or last_colour=='Z_R':
					ch='Z_R' 
		
		query="""UPDATE martha.nifty50 set Colour = %s where MSF = %s"""
		value=(ch,msf)
		# print('msf = ',msf,' ch = ',ch,' last color = ',last_colour)
		db_connection_execute("localhost", "root", "root", "martha", query, values = value)

		return zig_zag_box,zig_zag_list

# def msf_c(i):
	
# 	# print(result)
# 	global zig_zag_box,zig_zag_list
	
# 	if i[0]==1 or i[0]==2:
# 		query = """UPDATE martha.nifty50 SET Colour = 'NA' where Sr={}""".format(i[0])
# 		db_connection_execute("localhost", "root", "root", "martha", query)

# 	else:
# 		query = """SELECT Colour from nifty50 where Sr={}""".format((i[0])-1)
# 		last_colour=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 1)
# 		last_colour=last_colour[0]

# 		query="SELECT MSF from nifty50 where Sr between {} and {} ".format((i[0])-2,(i[0]))
# 		last_tow_msf= db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
# 		first,second,current_msf=last_tow_msf[0][0],last_tow_msf[1][0],last_tow_msf[2][0]
# 		#print('first = ',first,' second = ',second,' current msf = ',current_msf)
# 		print('zig_zag_box = ',zig_zag_box)
# 		print('zig_zag_list = ',zig_zag_list)
# 		zig_zag_box,zig_zag_list = colour_finding(current_msf,first,second,last_colour,zig_zag_box,zig_zag_list)

# query="""SELECT Sr FROM nifty50 """

# result=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
# print(result)
# for i in result:
# 	msf_c(i)