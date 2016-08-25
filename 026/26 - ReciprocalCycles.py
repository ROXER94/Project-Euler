# Calculates the number below 1000 which contains the longest recurring cycle in its decimal fraction part

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
	
primes = [p for p in range(3,1000,2) if isPrime(p)][::-1] + [2]

for p in primes:
	t = 1
	while (10**t)%p != 1:
		t += 1
	if t == p - 1:
		break
print(p)