# Calculates the number of Sundays that fell on the first of the month between January 1st, 1901 and December 31, 2000

from datetime import date

day = int(1900*365.2422)+1
date = date.fromordinal(day)

count = 0
while str(date) != "2000-12-31":
	day += 1
	date = date.fromordinal(day)
	if date.weekday() == 6 and str(date)[8:] == "01":
		count += 1
print(count)