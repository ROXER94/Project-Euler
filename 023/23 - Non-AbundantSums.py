# Calculates the sum of all the positive integers which cannot be written as the sum of two abundant numbers

def isAbundant(n):
	factors = []
	for i in range(1,n//2+1):
		if n%i == 0:
			factors.append(i)
	return sum(factors) > n

abundants = [n for n in range(1,28124) if isAbundant(n)]
sums = set()
for i in abundants:
	for j in abundants:
		if j >= i:
			sums.add(i+j)
print(sum(n for n in range(1,28124) if n not in sums))
