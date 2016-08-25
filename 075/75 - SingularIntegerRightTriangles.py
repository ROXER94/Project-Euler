# Calculates the number of values of L ≤ 1,500,000 as a perimeter for which exactly one integer sided right angle triangle can be formed

from fractions import gcd

count = 0
for L in range(12,1500001,2):
	current = 0
	s = L
	s2 = s / 2
	mlimit = s2 ** .5 - 1
	for m in range(2,int(mlimit+1)+1):
		if s2 % m == 0: 
			sm = s2 / m
			while sm % 2 == 0:
				sm /= 2
			if m % 2 == 1:
				k = m + 2
			else:
				k = m + 1
			while k < 2*m and k <= sm:
				if sm % k == 0 and gcd(k,m) == 1:
					d = s2 / (k*m)
					n = k-m
					a = int(d * (m * m - n * n))
					b = int(2 * d * m * n)
					c = int(d * (m * m + n * n))
					current += 1
				k += 2
	if current == 1:
		count += 1
print(count)