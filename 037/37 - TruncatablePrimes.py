# Calculates the sum of every two-sided truncatable prime

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncateLeft(number):
	array = []
	while len(str(number)) > 1:
		array.append(number)
		number = int(str(number)[1:])
	return array + [int(str(number)[-1])]

def truncateRight(number):
	array = []
	while len(str(number)) > 1:
		array.append(number)
		number = int(str(number)[:-1])
	return array + [int(str(number)[-1])]

sum = 0
array = []
for i in range(11,750000,2):
	if "5" not in str(i) and isPrime(i):
		array.append(i)
for i in array:
	test = truncateLeft(i) + truncateRight(i)
	success = True
	for t in test:
		if not isPrime(t):
			success = False
			break
	if success:
		sum += i
print(sum+53)
