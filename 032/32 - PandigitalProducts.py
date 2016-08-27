# Calculates the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

from itertools import permutations
array = [''.join(p) for p in permutations(str(987654321))]

newarray = []
for i in array:
	if int(i[0]) * int(i[1:5]) == int(i[5:]) or int(i[:2]) * int(i[2:5]) == int(i[5:]):
		newarray.append(int(i[5:]))
print(sum(list(set(newarray))))