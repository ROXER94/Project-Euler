# Calculates the least value of n for which the number of distinct solutions of the equation x^-1 + y^-1 = n^-1 exceeds 1000

def Factors(n):
	count = 0
	for x in range(1, int(n**.5) + 1):
		if n % x == 0:
			count += 2
	return count - 1

n = 10
while Factors(n**2) < 2000:
	n += 10
print(n)
