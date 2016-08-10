# Calculates the next Triangle, Pentagonal, and Hexagonal number after 40755

def triangle(n):
	return int(n * (n+1)/2)

def pentagonal(n):
	return int(n * (3 * n - 1)/2)
# Every pentagonal number is also a triangle number

def hexagonal(n):
	return n * (2 * n - 1)

# Array of Pentagonal numbers
parray = []

# Array of Hexagonal numbers
harray = []

for i in range(144,50000):
	harray.append(hexagonal(i))
	if pentagonal(i) in harray:
		print(pentagonal(i))
		break