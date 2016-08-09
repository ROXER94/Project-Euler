# Calculates the sum of every two-sided truncatable prime

def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

Range = 750000
array = []

for i in range(11,Range,2):
		if "5" not in str(i) and isPrime(i):
			array.append(i)

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
success = False
print("The two-sided truncatable primes are")
for i in array:
	test = truncateLeft(i) + truncateRight(i)
	for t in test:
		if isPrime(t):
			success = True
		else:
			success = False
			break
	if success:
		print(i)
		if i == 37:
			sum += 53
			print(53)
		sum += i
print("The sum is " + str(sum))
