# Calculates the number of ways 10^25 can be expressed as a sum of powers of two using each power no more than twice

def fusc(n):
	a = 1
	b = 0
	while n > 0:
		if n % 2 == 0:
			a += b
		else:
			b += a
		n //= 2
	return b

print(fusc(10**25+1))
