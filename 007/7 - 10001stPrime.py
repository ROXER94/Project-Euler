# Calculates 10,001st prime number

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

primeArray = [2]
number = 3
while len(primeArray) < 10001:
	if isPrime(number):
		primeArray.append(number)
	number += 2
print(primeArray[-1])