# Calculates the smallest m for which P(m) < 1/12345

from math import log

i = 1
while True:
	if int(log(i+1,2))/i < 1/12345:
		print(i*(i+1))
		break
	i += 1