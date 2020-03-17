import mysql.connector
#import openpyxl

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="martha",
  #auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor(buffered=True)

sql="SELECT COUNT(Open) from nifty50"
mycursor.execute(sql)
result=mycursor.fetchall()
print(result)

def colour_finding(i,msf,zig_zag_box,zig_zag_list):
	sql="SELECT Colour from nifty50 where Sr={} ".format(i-1)
	mycursor.execute(sql)
	last_colour= mycursor.fetchone()
	#print('last_colour = ',last_colour[0])
	ch=''
	if not zig_zag_box:
		sql="SELECT MSF from nifty50 where Sr between {} and {} ".format(i-2,i-1)
		mycursor.execute(sql)
		last_tow_msf= mycursor.fetchall()
		#print(last_tow_msf[0][0],'\t',last_tow_msf[1][0],'\tmsf = ',msf)
		if msf>last_tow_msf[0][0] and msf>last_tow_msf[1][0]:
			ch='G'
		elif msf<last_tow_msf[0][0] and msf<last_tow_msf[1][0]:
			ch='R'
		elif last_tow_msf[0][0] < msf < last_tow_msf[1][0] or last_tow_msf[0][0] > msf > last_tow_msf[1][0]:
			#print('zig-zig')
			if last_colour[0]=='G':
					ch='Z_G'
			elif last_colour[0]=='R':
					ch='Z_R' 
			zig_zag_box=True
			zig_zag_list=[last_tow_msf[0][0],last_tow_msf[1][0]]
		sql="UPDATE nifty50 set Colour = %s where Sr = %s"
		value=(ch,i)
		mycursor.execute(sql,value)
		mydb.commit()
		# print(mycursor.rowcount," record inserted")
		# print('ch = ',ch)
		# print('zig_zag_box = ',zig_zag_box)
		# print('zig_zag_list = ',zig_zag_list)		
		return zig_zag_box,zig_zag_list
	else:
		#print('In zig_zag condition')
		first,second=zig_zag_list[0],zig_zag_list[1]
		if msf>first and msf>second:
			ch='G'
			zig_zag_box=False
			zig_zag_list=[]
		elif msf<first and msf<second:
			ch='R'
			zig_zag_box=False
			zig_zag_list=[]
		elif first < msf < second or first > msf > second:
			#print('zig-zig')
			if last_colour[0]=='G' or last_colour[0]=='Z_G':
					ch='Z_G'
			elif last_colour[0]=='R' or last_colour[0]=='Z_R':
					ch='Z_R' 
		sql="UPDATE nifty50 set Colour = %s where Sr = %s"
		value=(ch,i)
		mycursor.execute(sql,value)
		mydb.commit()
		# print(mycursor.rowcount," record inserted")
		# print('ch = ',ch)
		# print('zig_zag_box = ',zig_zag_box)
		# print('zig_zag_list = ',zig_zag_list)	
		return zig_zag_box,zig_zag_list

def range_calculation(i):
	sql='UPDATE nifty50 set `RANGE HIGH / LOW` = High-Low where Sr= %s'
	r=mycursor.execute(sql,(i,))
	
	mydb.commit()

def msf_calculation():
	zig_zag_box=False
	zig_zag_list=[]
	for i in range(2,(result[0][0])+1):
		sql="SELECT Close from nifty50 where Sr={}".format(i)
		mycursor.execute(sql)
		close= mycursor.fetchone()
		#print(close)

		sql="SELECT MSF from nifty50 where Sr={}".format(i-1)
		mycursor.execute(sql)
		prev_msf=mycursor.fetchone()
		#print(prev_msf)

		msf=round((float(close[0])-float(prev_msf[0]))*0.33+float(prev_msf[0]),2)
		#print(msf)
		sql="UPDATE nifty50 SET MSF={} where Sr={}".format(msf, i)
		mycursor.execute(sql)
		mydb.commit()
		if i>2:
			zig_zag_box,zig_zag_list=colour_finding(i,msf,zig_zag_box,zig_zag_list)

		range_calculation(i)




msf_calculation()
# range_calculation()