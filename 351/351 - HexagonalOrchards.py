# Calculates the number of points hidden from the center in a hexagonal orchard of order 100,000,000

import operator as op
from functools import reduce

def totient_gen(limit):
	phi = (limit+1)*[0]
	phi[1] = 1
	yield 1
	for n in range(2,limit):
		if phi[n] == 0:
			phi[n] = n - 1
			for j in range(2,int(limit/n)):
				if phi[j] != 0:
					q = j
					f = n - 1
					while q % n == 0:
						f *= n
						q //= n
					phi[n * j] = f * phi[q]
		yield phi[n]

def ncr(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	numerator = reduce(op.mul, range(n, n-r, -1))
	denominator = reduce(op.mul, range(1, r+1))
	return numerator//denominator     

def H(n):
	return 6 * (ncr(n+1,2) - sum(list(totient_gen(int(1.5*n)))[:n]))

print(H(100000000))