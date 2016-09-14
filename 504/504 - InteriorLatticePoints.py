# Calculates the number of quadrilaterals that contain a square number of lattice points for a given range of coordinates

Range = 100

from math import sqrt
from fractions import gcd

array = []
cacheArea = {}
cacheExterior = {}

# Generate the points of the quadrilaterals
for a in range(1,Range+1):
	for b in range(1,Range+1):
		for c in range(1,Range+1):
			for d in range(1,Range+1):
				array.append([a,b,-c,-d])

# Determine if a number is square
def isSquare(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

# Calculate the distance between two points
def distance(x1,y1,x2,y2):
	return ((x2-x1) ** 2 + (y2-y1) ** 2) ** .5

# Calculate the area of a quadrilateral
def area_uncached(a,b,c,d):
	return (a * b + b * -c + -c * -d + -d * a) / 2

def area(a,b,c,d):
	if (b,-c,d,-a) in cacheArea.keys():
		return cacheArea[(b,-c,d,-a)]
	if (-c,-d,-a,-b) in cacheArea.keys():
		return cacheArea[(-c,-d,-a,-b)]
	if (-d,a,-b,c) in cacheArea.keys():
		return cacheArea[(-d,a,-b,c)]
	value = area_uncached(a,b,c,d)
	cacheArea[(a,b,c,d)] = value
	return value

# Calculate the number of exterior lattice points of the quadrilateral
def exterior_uncached(a,b,c,d):
	LatticePoints_AB = gcd(a,b)
	LatticePoints_BC = gcd(b,c) * -1
	LatticePoints_CD = gcd(c,d) * -1
	LatticePoints_DA = gcd(d,a)
	return LatticePoints_AB + LatticePoints_BC + LatticePoints_CD + LatticePoints_DA

def exterior(a,b,c,d):
	if (b,-c,d,-a) in cacheExterior.keys():
		return cacheExterior[(b,-c,d,-a)]
	if (-c,-d,-a,-b) in cacheExterior.keys():
		return cacheExterior[(-c,-d,-a,-b)]
	if (-d,a,-b,c) in cacheExterior.keys():
		return cacheExterior[(-d,a,-b,c)]
	value = exterior_uncached(a,b,c,d)
	cacheExterior[(a,b,c,d)] = value
	return value
	
count = 0
for i in array:
	AREA = area(i[0],i[1],i[2],i[3])
	EXTERIOR = exterior(i[0],i[1],i[2],i[3])
	# Pick's Theorem
	INTERIOR = AREA - EXTERIOR/2 + 1
	if isSquare(INTERIOR):
		count += 1
print(count)
