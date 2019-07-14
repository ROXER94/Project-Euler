# Calculates the smallest cube for which exactly five permutations of its digits are cube

from collections import Counter

def fivePermutations(dictionary,n):
     values = list(dictionary.values())
     keys = list(dictionary.keys())
     return keys[values.index(n)]

cubes = [n**3 for n in range(1,8400)]

array = []
for c in cubes:
	array.append(tuple(sorted(list(i for i in str(c)))))

L = Counter()
for i in array:
	L[i] += 1

value = fivePermutations(L,5)
for c in cubes:
	if tuple(sorted(list(i for i in str(c)))) == value:
		print(c)
		break