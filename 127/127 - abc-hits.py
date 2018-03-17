# Calculates the sum of c less than 120,000 for abc-hits 

from math import gcd

N = 120000
rad = [1]*N
for i in range(2,N):
	if rad[i] == 1:
		for j in range(i,N,i):
			rad[j] *= i
value = 0
for c in range(2,N):
	if rad[c-1] * rad[c] < c:
		value += c
	if 6*rad[c] < c:
		for a in range(2,c//2):
			if rad[a] * rad[c] < c:
				if gcd(a,c) == 1:
					if rad[a] * rad[c-a] * rad[c] < c:
						value += c
print(value)
