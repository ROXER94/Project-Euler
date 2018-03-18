# Calculates the number of Circular Primes below 1,000,000

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
	
def isCircularPrime(n):
	n = str(n)
	if len(n) == 1:
		return True
	elif len(n) == 2 and isPrime(int(n[1:]+n[0])):
		return True
	elif len(n) == 3 and isPrime(int(n[1:]+n[0])) and isPrime(int(n[2:]+n[:2])):
		return True
	elif len(n) == 4 and isPrime(int(n[1:]+n[0])) and isPrime(int(n[2:]+n[:2])) and isPrime(int(n[3:]+n[:3])):
		return True
	elif len(n) == 5 and isPrime(int(n[1:]+n[0])) and isPrime(int(n[2:]+n[:2])) and isPrime(int(n[3:]+n[:3])) and isPrime(int(n[4:]+n[:4])):
		return True
	elif len(n) == 6 and isPrime(int(n[1:]+n[0])) and isPrime(int(n[2:]+n[:2])) and isPrime(int(n[3:]+n[:3])) and isPrime(int(n[4:]+n[:4])) and isPrime(int(n[5:]+n[:5])):
		return True
	else:
		return False

array = []
for i in range(1,1000000):
	if "2" not in str(i) and "5" not in str(i) and isPrime(i):
		array.append(i)
print(sum(1 for i in array if isCircularPrime(i))+2)
