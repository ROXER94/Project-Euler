# Calculates the number of generalised Hamming numbers of type 100 which don't exceed 10^9

max = 100
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

def smooth(index, value):
	global count
	if index == len(primes):
		count += 1
		return
	p = primes[index]
	while value <= 10**9:
		smooth(index+1, value)
		value *= p

count = 0
smooth(0,1)
print(count)