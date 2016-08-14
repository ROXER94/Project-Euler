# Calculates the line number of the text file that has the greatest numerical value

import math

file = open("base_exp.txt")

array = []
for line in file:
	array.append(line.replace('\n', "").split(","))

max = 0
count = 1
for i in array:
	value = int(i[1]) * math.log(int(i[0]))
	if value > max:
		max = value
		result = count
	count += 1
print(result)