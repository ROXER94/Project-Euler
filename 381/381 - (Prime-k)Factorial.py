# Calculates the sum of all positive integers n below 100,000,000 such that the sum of each pair of factors of n is prime

def egcd(a, b):
    if a == 0:
        return (b,0,1)
    else:
        g, y, x = egcd(b%a,a)
        return (g,x-(b//a)*y,y)

def ModInverse(a, m):
	g,x,y = egcd(a,m)
	return x % m

max = 100000000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
primes.remove(2)
primes.remove(3)
Sum = 0
for p in primes:
	modInv = -3 * ModInverse(8,p)
	Sum += modInv - p*(modInv//p)
print(Sum)
