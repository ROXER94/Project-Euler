# Calculates the smallest member of the longest amicable chain with no element exceeding 1,000,000

def factors(n):
	array = []
	for x in range(1, n//2 + 1):
		if n % x == 0:
			array.append(x)
	return sum(array)

def cycle(n):
	array = []
	while n not in array:
		array.append(n)
		n = factors(n)
	return min(array)

cache = []
max = 0
for i in range(2,6000,2):
	if i not in cache:
		array = []
		while i not in array:
			array.append(i)
			i = factors(i)
			cache.append(i)
			if i%2==1 or i > 1000000 or i < 220:
				array = []
				break
		current = len(array)
		if current > max:
			max = current
			values = sorted(array)
print(cycle(values[-1]))