# Calculates the sum of all the positive integers which cannot be written as the sum of two abundant numbers

cache = {}
def isAbundant(n):
	factors_array = []
	for x in range(1, n//2 + 1):
	    if n % x == 0:
	        value = int(n/x)
	        if value in cache:
	            return cache[value]
	        factors_array.append(x)
	if sum(factors_array) > n:
		cache[n] = True
		return True
	return False

abundant = []
for i in range(12,28124):
	if isAbundant(i):
		abundant.append(i)

sums = []
for i in range(len(abundant)):
	for j in range(i,len(abundant)):
		value = abundant[i]+abundant[j]
		sums.append(value)
sums = list(set(sums))

sum = 0
for i in range(1,28124):
	if i not in sums:
		sum += i
print(sum)