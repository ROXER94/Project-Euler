# Calculates the number of ways 10^25 can be expressed as a sum of powers of two using each power no more than twice

def fusc(n):
	k = n
	a = 1
	b = 0
	while k > 0:
		if k%2 == 0:
			k //= 2
			a += b
		else:
			k = (k-1)//2
			b += a
	return b

print(fusc(10**25+1))