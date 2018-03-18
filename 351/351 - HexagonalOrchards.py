# Calculates the number of points hidden from the center in a hexagonal orchard of order 100,000,000

import operator as op
from functools import reduce

def totients(n):
	phi = [0]*(n+1)
	phi[1] = 1
	for i in range(1,n+1):
		if phi[i] == 0:
			phi[i] = i - 1
			for j in range(2,n//i+1):
				if phi[j] != 0:
					q = j
					f = i - 1
					while q % i == 0:
						f *= i
						q //= i
					phi[i*j] = f * phi[q]
		yield phi[i]

def ncr(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	numerator = reduce(op.mul, range(n, n-r, -1))
	denominator = reduce(op.mul, range(1, r+1))
	return numerator//denominator     

def H(n):
	return 6 * (ncr(n+1,2) - sum(list(totients(n))))

print(H(100000000))
