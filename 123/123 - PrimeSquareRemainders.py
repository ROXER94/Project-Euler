# Calculates the smallest value of n for which the remainder first exceeds 10^10 in the equation (p(n)-1)^n + (p(n)+1)^n % p(n)^2

max = 300000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

n = 7037
while 2*(n+1)*primes[n] < 10000000000:
	n += 2
print(n+2)
