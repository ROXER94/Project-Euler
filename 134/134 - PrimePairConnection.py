# Calculates the sum of the prime pair connection for every pair of consecutive primes below 1,000,000

from math import gcd
from functools import reduce
from operator import mul

def egcd(a, b):
	if a == 0:
		return (b,0,1)
	else:
		g, y, x = egcd(b%a,a)
		return (g,x-(b//a)*y,y)

def ModInverse(a, m):
	g,x,y = egcd(a, m)
	if g != 1:
		raise Exception('Mod Inverse does not exist')
	else:
		return x%m

def ChineseRemainderTheorem(relativePrimes,remainders):
	assert len(relativePrimes) > 1,\
		"Length of array of relative primes must be greater than one"
	assert max([gcd(i,j) for i in relativePrimes for j in relativePrimes[relativePrimes.index(i)+1:]]) == 1,\
		"Array of relative primes is not a collection of pairwise relatively prime integers"
	assert len(relativePrimes) == len(remainders),\
		"Array of relative primes and array of remainders are not the same length"
	M = reduce(mul,relativePrimes,1)
	M_array = [M//i for i in relativePrimes]
	y_array = [ModInverse(M_array[relativePrimes.index(i)]%i,i) for i in relativePrimes]
	return sum([i*j*k for i,j,k in zip(remainders,M_array,y_array)])%M

Max = 1000004
primes = []
sieve = [True] * Max
for i in range(2, Max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, Max, i):
			sieve[j] = False
primes.remove(2)
primes.remove(3)

Sum = 0
for i in range(len(primes)-1):
	p1 = primes[i]
	p2 = primes[i+1]
	Sum += ChineseRemainderTheorem([p2,10**int(len(str(p1)))],[0,p1])
print(Sum)
