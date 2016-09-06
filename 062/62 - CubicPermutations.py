# Calculates the smallest cube for which exactly five permutations of its digits are cube

def fivePermutations(dictionary):
     values = list(dictionary.values())
     keys = list(dictionary.keys())
     return keys[values.index(5)]

cubes = [n**3 for n in range(1,8400)]

array = []
for c in cubes:
	array.append(tuple(sorted(list(i for i in str(c)))))

cache = {}	
for i in array:
    if i not in cache:
        cache[i] = 1
    else:
        cache[i] += 1

value = fivePermutations(cache)
for c in cubes:
	if tuple(sorted(list(i for i in str(c)))) == value:
		print(c)
		break