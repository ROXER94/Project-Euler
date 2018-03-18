# Calculates the number below 1000 which contains the longest recurring cycle in its decimal fraction part

max = 1000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

for p in primes[::-1]:
	t = 1
	while (10**t)%p != 1:
		t += 1
	if t == p - 1:
		break
print(p)
