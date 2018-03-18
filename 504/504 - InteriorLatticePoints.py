# Calculates the number of quadrilaterals that contain a square number of lattice points for a given range of coordinates

from math import sqrt,gcd

def isSquare(n):
    return int(sqrt(n)+.5)**2 == n
	
print(sum(1 for a in range(1,101) for b in range(1,101) for c in range(1,101) for d in range(1,101) if isSquare((a*b + b*c + c*d + d*a - gcd(a, b) - gcd(b, c) - gcd(c, d) - gcd(d, a)) / 2 + 1)))
