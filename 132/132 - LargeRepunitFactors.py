# Calculates the sum of the first forty prime factors of R(10^9)

# Returns a^b % n 
def powermod(a, b, n):
	r = 1
	while b > 0:
		if b & 1 == 1:
			r = r * a % n
		b //= 2
		a = a * a % n
	return r


max = 200000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

sum = 0
count = 0
for p in primes:
	if count == 40:
		break
	if powermod(10,10**9,9*p) == 1:
		sum += p
		count += 1
print(sum)