# Calculates the number of non-bouncy numbers under a googol

cache = {}
def fact(n):
	if n not in cache:
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
	if n == 0 : return 1
	else :
		return n*fact(n-1

def nCr(n,r):
	return fact(n) // (fact(r) * fact(n-r))

def bouncy(n):
	if n < 3:
		return 0
	return 10**n - nCr(9+n,n) - sum(nCr(9+i,i) for i in range(1,n+1)) + 10*n

print(10**100 - bouncy(100)-1)