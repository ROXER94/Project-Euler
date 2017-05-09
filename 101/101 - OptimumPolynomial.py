# Calculates the sum of the FITs for the BOPs

def U(n):
	return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def TransposeMatrix(m):
	t = []
	for r in range(len(m)):
		tRow = []
		for c in range(len(m[r])):
			if c == r:
				tRow.append(m[r][c])
			else:
				tRow.append(m[c][r])
		t.append(tRow)
	return t

def MatrixMinor(m,i,j):
	return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def MatrixDeternminant(m):
	if len(m) == 2:
		return m[0][0]*m[1][1]-m[0][1]*m[1][0]
	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c)*m[0][c]*MatrixDeternminant(MatrixMinor(m,0,c))
	return determinant

def MatrixInverse(m):
	determinant = MatrixDeternminant(m)
	if len(m) == 2:
		return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]]
	cofactors = []
	for r in range(len(m)):
		cofactorRow = []
		for c in range(len(m)):
			minor = MatrixMinor(m,r,c)
			cofactorRow.append(((-1)**(r+c)) * MatrixDeternminant(minor))
		cofactors.append(cofactorRow)
	cofactors = TransposeMatrix(cofactors)
	for r in range(len(cofactors)):
		for c in range(len(cofactors)):
			cofactors[r][c] = cofactors[r][c]/determinant
	return cofactors

def MatrixMultiplication(a,b):
	zip_b = zip(*b)
	zip_b = list(zip_b)
	return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a][::-1]

S = 0
array = [[U(i)] for i in range(1,11)]
for index in range(2,len(array)+1):
	y = array[:index]
	x = [[i**x for x in range(len(y))][::-1] for i in range(1,len(y)+1)]
	subarray = [a for b in MatrixMultiplication(MatrixInverse(x),y) for a in b]
	S += round(sum(subarray[i]*(len(subarray)+1)**i for i in range(len(subarray))))
print(S+1)
