# Calculates the sum of the number of t ≤ 1000000 such that t is type L(n) for 1 ≤ n ≤ 10

from collections import Counter

n = 1000000
L = Counter()
for l in range(3,n//4 + 2):
	for s in range(l-2,0,-2):
		value = l**2 - s**2
		if value <= n:
			L[value] += 1
		else:
			break
print(sum(1 for i in L.values() if i in {1,2,3,4,5,6,7,8,9,10}))