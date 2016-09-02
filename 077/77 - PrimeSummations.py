# Calculates the first number which can be written as the sum of primes in over 5000 different ways

max = 100
primes = []
sieve = [True] * max
for i in range(2, max):
    if sieve[i]:
        primes.append(i)
        for j in range(i * i, max, i):
            sieve[j] = False

cache = {}
i = 1
for p in primes:
	cache[i] = p
	i += 1

n = 1
result = 1
while result <= 5000:
	n += 1
	ways = [0] * (n+1)
	ways[0] = 1
	for i in range(1,len(cache)+1):
		for j in range(cache[i],n+1):
			ways[j] = ways [j] + ways [j - cache[i]]
	result = ways[n]
print(n)