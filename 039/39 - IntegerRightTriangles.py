# Calculates the perimeter length that produces the maximum number of integer right triangles

from math import sqrt

def is_square(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

# Generate Pythagorean Triples whose sum is less than the upperBound
array = []
N = 481
upperBound = 1000
for a in range(1,N):
	for b in range(a+1,N):
		c = sqrt(a**2 + b**2)
		if is_square(c**2) and a + b + int(c) <= upperBound:
			array.append([a,b,int(c)])

# Sum perimeter of each triple, count the number of solutions, and determine new maximum
countarray = []
number = 12
maximum = 0
while number <= upperBound:
	currentcount = 0
	for i in array:
		if sum(i) == number:
			currentcount += 1
		if currentcount > maximum:
			maximum = currentcount
			countarray.append(i)
	number += 1
print(sum(countarray[-1]))