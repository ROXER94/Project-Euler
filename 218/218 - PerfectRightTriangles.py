# Calculates the number of perfect right-angled triangles that are not super-perfect

import sys
sys.setrecursionlimit(10000)

from math import sqrt

def mm(A,B):
	array = []
	for i in range(3):
		temp = 0
		for j in range(3):
			temp += A[i][j] * B[j]
		array.append(temp)
	return array

def isSquare(n):
    return int(sqrt(n)+.5)**2 == n

A = [[1,-2,2],[2,-1,2],[2,-2,3]]
B = [[1,2,2],[2,1,2],[2,2,3]]
C = [[-1,2,2],[-2,1,2],[-2,2,3]]

def primitive(array):
	if array[2] > limit:
		return 0
	else:
		a = mm(A,array)
		b = mm(B,array)
		c = mm(C,array)
		area = array[0] * array[1] // 2
		if isSquare(array[2]) and area % 84 != 0:
			return 1 + primitive(a) + primitive(b) + primitive(c)
		return primitive(a) + primitive(b) + primitive(c)

limit = 10**16**(1/2)
print(primitive([3,4,5]))
