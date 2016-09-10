# Calculates the shortest possible secret passcode using the keylog information in the text file

from itertools import permutations

passcodes = sorted([''.join(p) for p in permutations(str(12367890))])

file = open("keylog.txt")
array = []
for line in file:
	i = line.replace("\n","")
	if i not in array:
		array.append(i)

for i in passcodes:
	for j in array:
		if i.index(j[0]) < i.index(j[1]) < i.index(j[2]):
			if j == array[-1]:
				print(i)
		else:
			break
