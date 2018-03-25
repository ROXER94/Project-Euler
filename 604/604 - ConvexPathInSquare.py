# Calculates the maximum number of lattice points in an axis-aligned N×N square that the graph of a single strictly convex increasing function can pass through for N = 10^18

from math import pi

def totients(n):
	phi = [0]*(n+1)
	phi[1] = 1
	for i in range(1,n+1):
		if phi[i] == 0:
			phi[i] = i - 1
			for j in range(2,n//i+1):
				if phi[j] != 0:
					q = j
					f = i - 1
					while q % i == 0:
						f *= i
						q //= i
					phi[i*j] = f * phi[q]
		yield phi[i]

points = 0
n = 10**18
k = int((n*pi**2)**(1/3))
phi = list(totients(k))
for i in range(1,k):
	n -= i * phi[i-1] // 2
	points += phi[i-1]
points += 2 * n // k
print(points)