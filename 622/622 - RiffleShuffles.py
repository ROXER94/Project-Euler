from math import gcd,sqrt
from itertools import product

def Factors(n):
	factors = set()
	for i in range(1,int(sqrt(n))+1):
		if n % i == 0:
			factors.add(i)
			factors.add(n//i)
	return sorted(list(factors))

def MultiplicativeOrder(a,n):
	if gcd(a,n) != 1:
		return -1
	r = 1
	k = 1
	while k < n:
		r = r*a % n
		if r == 1:
			return k
		k += 1
	return -1

print(sum(i+1 for i in sorted(set([x*y for x,y in product(Factors(2**30+1),Factors(2**30-1))])) if MultiplicativeOrder(2,i) == 60))
