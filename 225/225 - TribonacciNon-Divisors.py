# Calculates the 124th odd number that does not divide any terms in the Tribonacci sequence

cache = {1:1,2:1,3:1}

def tribonacci(n):
    if n not in cache:
        cache[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return cache[n]

for i in range(1,101):
	tribonacci(230*i)

odds = [n for n in range(27,6670,2)]

count = 0
divide = False
for o in odds:
	for n in cache.values():
		if n%o == 0:
			divide = True
			break
	if not divide:
		count += 1
	if count == 124:
		break
	divide = False
print(o)