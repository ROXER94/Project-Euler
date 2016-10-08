# Calculates the number of paths through an n x n grid using arrays

array = []

n = 20

for i in range(1,n+1):
	array.append(i)

def Matrix(array):
	result = [1]
	for i in array:
		if array.index(i) != n-1:
			if array.index(i) == 0:
				result.append(i+array[array.index(i)+1])
			else:
				result.append(array[array.index(i)+1]+result[array.index(i)])
	return result

j=1
while j != n:
	array = Matrix(array)
	j += 1
print(array[n-1]*2)
#(40 choose 20)
