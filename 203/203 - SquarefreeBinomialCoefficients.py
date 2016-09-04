# Calculates the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle

cache = {}

def fact(n):
	if n not in cache.keys():
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
	if n == 0 :
		return 1
	else:
		return n*fact(n-1)

def nCr(n,r):
	return int(fact(n) / (fact(r) * fact(n-r)))
	
	
def Pascal(n,r):
	return nCr(n-1,r) + nCr(n-1,r-1)

def isSquarefree(n):
	primesSquared = [x*x for x in [2, 3, 5, 7]]
	for i in primesSquared:
		if n%i==0:
			return False
	return True

n = 51
array = []
for i in range(2,n):
	for j in range(1,i):
		array.append(Pascal(i,j))

print(sum(i for i in list(set(array)) if isSquarefree(i)) + 1)
