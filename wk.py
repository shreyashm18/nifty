import datetime
from datetime import datetime, timedelta

today=datetime(2011,4,11).date()
first_date=datetime(2011,1,3).date()
diff_date=today-first_date


for i in range(0,diff_date.days):
	date_to_print=first_date+timedelta(i)

	date_weekday=date_to_print.weekday()

	if date_weekday==0:
		
		print('\n')


	print('day = ',date_to_print)