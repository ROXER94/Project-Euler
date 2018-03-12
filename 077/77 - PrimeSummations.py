# Calculates the first number which can be written as the sum of primes in over 5000 different ways

max = 100
primes = []
P = {}
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		P[len(primes)] = i
		for j in range(i * i, max, i):
			sieve[j] = False

n = 0
result = 0
while result <= 5000:
	n += 1
	ways = [0] * (n+1)
	ways[0] = 1
	for i in range(1,len(P)+1):
		for j in range(P[i],n+1):
			ways[j] = ways [j] + ways[j-P[i]]
	result = ways[n]
print(n)
