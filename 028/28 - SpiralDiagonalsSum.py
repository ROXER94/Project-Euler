# Calculates the sum of the numbers on the diagonals in an n x n spiral

n = 1001
sum = 1
for i in range(3,n+1,2):
	sum += 4 * i**2 - 6 * i + 6
print(sum)