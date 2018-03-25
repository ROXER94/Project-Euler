# Calculates the sum of all indices n such that T(n) is 47-smooth

from math import sqrt

def _47Smooth(n):
	for p in primes:
		while n%p == 0:
			n //= p
	return n == 1

def squareFrees(maxpr, product, pindex):
	pr = primes[pindex]
	if pr < maxpr:
		for val in squareFrees(maxpr, product, pindex+1):
			yield val
		for val in squareFrees(maxpr, product*pr, pindex+1):
			yield val
	else:
		yield product
		yield product*maxpr

def findNextSolutions(x0,y0,D,L):
	x_current,y_current = x0,y0
	for k in range(0,L):
		yield (x_current,y_current)
		x_next = x0*x_current + D*y0*y_current
		y_next = y0*x_current + x0*y_current
		x_current = x_next
		y_current = y_next

def Lehmer(xi):
	x = (xi-1)//2
	y = (xi+1)//2
	if _47Smooth(x) and _47Smooth(y):
		return (True,(x,y))
	return (False,"")

def Pell(D):
	U_cur = 0
	V_cur = 1
	a0 = int(sqrt(D))
	a_cur = a0
	P_cur = a0
	Q_cur = 1

	P_prev = 1
	Q_prev = 0
	count = 0

	while a_cur <= a0:
		U_next = a_cur*V_cur - U_cur
		V_next = (D-U_next**2)//V_cur
		a_next = (a0+U_next)//V_next
		P_next = a_next*P_cur + P_prev
		Q_next = a_next*Q_cur + Q_prev

		P_prev = P_cur
		Q_prev = Q_cur
		U_cur = U_next
		V_cur = V_next
		a_cur = a_next
		P_cur = P_next
		Q_cur = Q_next

		count += 1

	if count%2 == 0:
		return (P_prev,Q_prev)
	else:
		return (P_prev**2 + D*Q_prev**2,2*P_prev*Q_prev)

n_smooth = 47
primes = []
sieve = [True] * (n_smooth+1)
for i in range(2, n_smooth+1):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, n_smooth+1, i):
			sieve[j] = False

S = 0
L = max(3,(n_smooth+1)//2)
sqfree = [1] + sorted(list(squareFrees(n_smooth,1,0)))[2:]
for q in sqfree:
	D = 2*q
	fundamental = Pell(D)
	if Lehmer(fundamental[0])[0]:
		solutions = list(findNextSolutions(fundamental[0],fundamental[1],D,L))
		for s in solutions:
			value = Lehmer(s[0])
			if value[0]:
				S += value[1][0]
print(S)