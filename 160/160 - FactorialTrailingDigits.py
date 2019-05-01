# Calculates the last five non-zero digits in 1,000,000,000,000!

def FactorialLastDigits(n,e):
	a = 1
	b = 1
	c = 10**e
	mod = max(n,c)
	for i in range(1,n+1):
		if i % 2 == 0: current = b*i
		else: current = a*i
		while current % 10 == 0: current //= 10
		if i % 2 == 0: a = current % mod
		else: b = current % mod
	if n % 2 == 0: return a % c
	else: return b % c

n = 10**12
print(FactorialLastDigits(n//5**7,5))