# Calculates the next Triangle, Pentagonal, and Hexagonal number after 40755

def triangle(n):
	return n*(n+1)//2

def pentagonal(n):
	return n*(3*n-1)//2
# Every pentagonal number is also a triangle number

def hexagonal(n):
	return n*(2*n-1)

hexagons = set()
for i in range(144,50000):
	hexagons.add(hexagonal(i))
	if pentagonal(i) in hexagons:
		print(pentagonal(i))
		break
