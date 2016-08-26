# Calculates the maximum total from top to bottom of the triangle

with open('triangle.txt') as file:
	matrix = [[int(digit) for digit in line.split()] for line in file]

t = matrix[-1]
for i in range(len(matrix) - 2, -1, -1):
    t = [max(matrix[i][j] + t[j], matrix[i][j] + t[j+1]) for j in range(len(matrix[i]))]
print(t[0])