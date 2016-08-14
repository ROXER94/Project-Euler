# Calculates the number of quadrilaterals that contain a square number of lattice points for a given range of coordinates

Range = 100

from math import sin, acos, sqrt
from fractions import gcd

array = []

# Generate the points of the quadrilaterals
for a in range(1,Range+1):
	for b in range(1,Range+1):
		for c in range(1,Range+1):
			for d in range(1,Range+1):
				array.append([a,b,-c,-d])

# Determine if a number is square
def is_square(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

# Calculate the distance between two points
def distance(x1,y1,x2,y2):
	return ((x2-x1) ** 2 + (y2-y1) ** 2) ** .5

# Calculate angle BCD
def angleLeft(a,b,c,d):
	CB = distance(0,b,c,0)
	CD = distance(c,0,0,d)
	BD = distance(0,b,0,d)
	return acos((CB ** 2 + CD ** 2 - BD ** 2) / (2 * CB * CD))

# Calculate angle BAD
def angleRight(a,b,c,d):
	AB = distance(a,0,0,b)
	AD = distance(a,0,0,d)
	BD = distance(0,b,0,d)
	return acos((AB ** 2 + AD ** 2 - BD ** 2) / (2 * AB * AD))

# Calculate the area of a quadrilateral
def area(a,b,c,d):
	AB = distance(a,0,0,b)
	BC = distance(0,b,c,0)
	CD = distance(c,0,0,d)
	DA = distance(0,d,a,0)
	Left = angleLeft(a,b,c,d)
	Right = angleRight(a,b,c,d)
	return round(.5 * BC * CD * sin(Left) + .5 * AB * DA * sin(Right),1)

# Calculate the number of exterior lattice points of the quadrilateral
def exterior(a,b,c,d):
	LatticePoints_AB = gcd(a,b)
	LatticePoints_BC = gcd(b,c) * -1
	LatticePoints_CD = gcd(c,d) * -1
	LatticePoints_DA = gcd(d,a)
	return LatticePoints_AB + LatticePoints_BC + LatticePoints_CD + LatticePoints_DA

count = 0
for i in array:
	AREA = area(i[0],i[1],i[2],i[3])
	EXTERIOR = exterior(i[0],i[1],i[2],i[3])
	# Pick's Theorem
	INTERIOR = AREA - EXTERIOR/2 + 1
	if is_square(INTERIOR):
		count += 1
print(count)