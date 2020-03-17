from math import ceil,floor
from database_connection import db_connection_execute,db_connection_fetch

def JGD_JWD_finder(number,decimal,high,low,sr_no):
	jgd = decimal*ceil((high-number)/decimal)
	jwd = decimal*floor((low+number)/decimal)
	# print('jgd = ',jgd,' jwd = ',jwd)
	query="""UPDATE martha.nifty50 set JGD = %s,JWD = %s where Sr = %s"""
	value=(jgd,jwd,sr_no)
	db_connection_execute("localhost", "root", "root", "martha", query, values = value)
	# print('sr_no = ',sr_no)
	if sr_no==1:
		query="""UPDATE martha.nifty50 set `Director Pattern` = '2+2' where Sr = {}""".format(sr_no)
		db_connection_execute("localhost", "root", "root", "martha", query)
	else:
		get_query="""SELECT JGD, JWD from nifty50 where Sr = {}""".format(sr_no-1)
		prev_data=db_connection_fetch("localhost", "root", "root", "martha", get_query, fetch_type = 1)
		print()
		prev_jgd,prev_jwd=prev_data[0],prev_data[1]
		# print(f'prev_jgd = {prev_jgd} prev_jwd = {prev_jwd}')

		if jgd > prev_jwd and jwd > prev_jwd:
			query="""UPDATE martha.nifty50 set `Director Pattern` = '2+2' where Sr = {}""".format(sr_no)
			db_connection_execute("localhost", "root", "root", "martha", query)

		elif jgd > prev_jwd and jwd < prev_jwd:
			query="""UPDATE martha.nifty50 set `Director Pattern` = '2+1' where Sr = {}""".format(sr_no)
			db_connection_execute("localhost", "root", "root", "martha", query)

		elif jgd < prev_jwd and jwd < prev_jwd:
			query="""UPDATE martha.nifty50 set `Director Pattern` = '3+1' where Sr = {}""".format(sr_no)
			db_connection_execute("localhost", "root", "root", "martha", query)




# def pattern_finder(i):
# 	query = """SELECT `RANGE (HIGH - LOW)`, High, Low from nifty50 where Sr={}""".format(i[0])
# 	value=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type=1)
# 	print(value)
# 	number=value[0]
# 	high=float(value[1])
# 	low=float(value[2])
# 	JGD_JWD_finder(number*(38.2/100),0.05,high,low,i[0])

# query="""SELECT Sr FROM nifty50 """

# result=db_connection_fetch("localhost", "root", "root", "martha", query, fetch_type = 2)
# #print(result)
# for i in result:
# 	pattern_finder(i)