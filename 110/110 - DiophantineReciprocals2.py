# Calculates the least value of n for which the number of distinct solutions of the equation x^-1 + y^-1 = n^-1 exceeds 4,000,000

from math import log, ceil
from functools import reduce

n = 8000000
maximum = 50
primes = []
sieve = [True] * maximum
for i in range(2, maximum):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, maximum, i):
			sieve[j] = False
primes = primes[:ceil(log(n,3))]

limit = reduce(lambda x, y: x*y, primes)
for a in range(10):
	if 3**a > limit:
		break
	for b in range(5):
		if 3**a * 5**b > limit:
			break
		for c in range(5):
			if 3**a * 5**b * 7**c > limit:
				break
			for d in range(5):
				if 3**a * 5**b * 7**c * 9**d > limit:
					break
				for e in range(5):
					current = 3**a * 5**b * 7**c * 9**d * 11**e
					if current > limit:
						break
					elif current > n:
						limit = 3**a * 5**b * 7**c * 9**d * 11**e
						e1,e2,e3,e4,e5 = a,b,c,d,e

array = [e1,e2,e3,e4,e5][::-1]
while 0 in array:
	array.remove(0)
exponents = [1,2,3,4,5][:len(array)][::-1]
number,index = 1,0
for i in array:
	for j in primes[:i]:
		number *= j**exponents[index]
	primes = primes[i:]
	index += 1
print(number)