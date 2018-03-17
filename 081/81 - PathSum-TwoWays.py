# Calculates the minimal path sum from the top left to the bottom right of the matrix by only moving right and down

matrix = []
file = open("matrix.txt", "r")
for line in file.split('\n'):
	matrix.append([int(i) for i in line.split(",")])
for i in range(1,80):
	matrix[0][i] += matrix[0][i-1]
for j in range(1,80):
	matrix[j][0] += matrix[j-1][0]
for i in range(1,80):
	for j in range(1,80):
		matrix[i][j] += min(matrix[i][j-1],matrix[i-1][j])
print(matrix[-1][-1])
