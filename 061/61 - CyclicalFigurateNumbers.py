# Calculates the sum of the only set of six cyclic 4-digit numbers that contains a triangle, square, pentagonal, hexagonal, heptagonal, and octogonal number

from sys import exit
from itertools import permutations

def Triangle(n):
	return n*(n+1)//2

def Square(n):
	return n**2

def Pentagonal(n):
	return n*(3*n-1)//2

def Hexagonal(n):
	return n*(2*n-1)

def Heptagonal(n):
	return n*(5*n-3)//2

def Octogonal(n):
	return n*(3*n-2)

def isCyclic(n,m):
	return str(n)[2:] == str(m)[:2]

triangles = [Triangle(i) for i in range(45,141)]
squares = [Square(i) for i in range(32,100)]
pentagons = [Pentagonal(i) for i in range(26,82)]
hexagons = [Hexagonal(i) for i in range(23,71)]
heptagons = [Heptagonal(i) for i in range(21,64)]
octogons = [Octogonal(i) for i in range(19,59)]

array = list(permutations([triangles,squares,pentagons,hexagons,heptagons,octogons]))

for i in array:
	for a in i[0]:
		for b in i[1]:
			if isCyclic(a,b):
				for c in i[2]:
					if isCyclic(b,c):
						for d in i[3]:
							if isCyclic(c,d):
								for e in i[4]:
									if isCyclic(d,e):
										for f in i[5]:
											if isCyclic(e,f):
												if isCyclic(f,a):
													print(a+b+c+d+e+f)
													exit()
