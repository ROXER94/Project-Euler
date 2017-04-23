# Calculates the least value of n for which A(n) first exceeds 1,000,000

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def powermod(a, b, n):
	r = 1
	while b > 0:
		if b & 1 == 1:
			r = r * a % n
		b //= 2
		a = a * a % n
	return r

n = 1000013
while True:
	if gcd(n,10) == 1:
		k = 666681
		while powermod(10,k,n) != 1:
			k += 1
		if k > 1000000:
			print(n)
			break
	n += 2
