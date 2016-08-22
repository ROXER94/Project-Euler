# Calculates the number of starting numbers below 1,000,000 that produce a digit factorial chain of exactly sixty non-repeating terms

cache = {}

def fact(n):
	if n not in cache.keys():
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
    if n == 0 : return 1
    else :
        return n*fact(n-1)

count = 0
for i in range(1000000):
	array = []
	match = False
	while not match:
		array.append(i)
		value = 0
		for j in str(i):
			value += fact(int(j))
		if value in array:
			match = True
		i = value
	distance = len(array)
	if distance == 60:
		count += 1
print(count)