# Calculates the first triangle number to have over five hundred divisors

import math

def Factors(n):
	count = 0
	for x in range(1, math.ceil(n**0.5) + 1):
		if n % x == 0:
			count += 2
		if n % (n**0.5) == 0:
			count -= 1
	return count

def triangle(n):
	return int(n * (n+1)/2)

number = 1
while True:
	current = triangle(number)
	if Factors(current) > 500:
		print(current)
		break
	number += 1
