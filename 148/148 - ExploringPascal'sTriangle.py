# Calculates the number of entries which are not divisible by 7 in the first 1,000,000,000 rows of Pascal's triangle

def Base7(n):
	if n == 0:
		return 0
	digits = []
	while n:
		digits.append(int(n % 7))
		n /= 7
	return int(''.join(str(i) for i in digits[::-1]))

def Pascal(n,b = False):
	if (n < 7): return n * (n+1) // 2
	b7 = n
	if b:
		b7 = Base7(n)
	n1 = int(str(b7)[0])
	n2 = int(str(b7)[1:])
	return n1 * (n1+1) // 2 * 28**(len(str(b7))-1) + (n1+1) * Pascal(n2)

print(Pascal(1000000000,True))
