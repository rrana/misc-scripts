#!/usr/bin/python


import datetime
from calendar import monthrange

payday_is = 25

current_year = int(datetime.date.today().strftime("%Y"))
current_month = int(datetime.date.today().strftime("%m"))

today = int(datetime.date.today().strftime("%d"))

end_of_this_month = monthrange(current_year, current_month)[1]

if today < 25:
	days_until_money = payday_is - today
	print "Wait %d more days for MONEY bith!" % days_until_money

elif today == 25:
	print "It's PAYDAY bitch!"

elif today > 25 and today <= end_of_this_month:
	remaining_days_this_month = end_of_this_month - today
	days_until_next_months_payday = remaining_days_this_month + payday_is

	print "Wait for next month. Still %d more days to go!" % days_until_next_months_payday

else:
	print "Something went wrong in logic! And you still expect payment!"
