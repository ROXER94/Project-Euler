# Calculates the number of Circular Primes below 1,000,000

def isPrime(n):
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

count = 0
for i in array:
	if isCircularPrime(i):
		count += 1
print(count)