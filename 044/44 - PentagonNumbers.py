# Calculates the minimum difference of two pentagonal numbers whose sum and difference are pentagonal

def pentagonal(n):
	return n*(3*n-1)//2

pentagon = set(pentagonal(n) for n in range(1,2500))

array = []
for p1 in pentagon:
	for p2 in pentagon:
		if p1 + p2 in pentagon:
			array.append((p1,p2))

for i in array:
	if i[1] - i[0] in pentagon:
		print(i[1]-i[0])
		break
