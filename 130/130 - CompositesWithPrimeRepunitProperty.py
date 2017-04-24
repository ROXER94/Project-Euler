# Calculates the sum of the first 25 composite values of n for which GCD(n, 10) = 1 and n − 1 is divisible by A(n)

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

max = 15000
primes = {}
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes[i] = True
		for j in range(i * i, max, i):
			sieve[j] = False
			primes[j] = False

S = 0
count = 0
n = 91
while count != 25:
	if gcd(n,10) == 1 and gcd(n,3) == 1:
		k = 1
		while powermod(10,k,n) != 1:
			k += 1
		if (n-1)%k==0 and not primes[n] and int("1"*k)%n==0:
			S += n
			count += 1
	n += 2
print(S)