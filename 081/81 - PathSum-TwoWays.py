# Calculates the minimal path sum from the top left to the bottom right of the matrix by only moving right and down

matrix = []
file = open("matrix.txt", "r")
for line in file:
	matrix.append([int(i) for i in line.split(",")])

distinct = []
for i in matrix:
	for j in i:
		distinct.append(j)
distinct = list(set(distinct))

a = 1
for i in matrix:
	for j in i:
		if j in distinct:
			i[i.index(j)] += .000001 * a
			a += 1

array = [[] for i in range(2*len(matrix) - 1)]

for x in matrix:
	for y in x:
		sum = matrix.index(x) + x.index(y)
		array[sum].append(y)
matrix = array

for i in range(len(matrix)):
	if i >= int(len(matrix)/2):
		length = len(matrix[i])
		missing = i + 1 - length
		for j in range(int(missing/2)):
			matrix[i] = [10000] + matrix[i]
			matrix[i].append(10000)

t = matrix[-1]
for i in range(len(matrix) - 2, -1, -1):
    t = [min(matrix[i][j] + t[j], matrix[i][j] + t[j+1]) for j in range(len(matrix[i]))]
print(int(t[0]))