# Calculates the least value of n for which the number of distinct solutions of the equation x^-1 + y^-1 = n^-1 exceeds 1000

def factors(n):
	count = 0
	for x in range(1, int(n**0.5) + 1):
		if n % x == 0:
			count += 2
	return count - 1

n = 10
while True:
	if factors(n**2) > 2000:
		print(n)
		break
	n += 10