# Calculates the maximum 16-digit string for a magic 5-gon ring

from itertools import permutations

array = permutations([1,2,3,4,5,6,7,8,9,10])
for i in array:
	value = [i[0],i[1],i[2],i[3],i[2],i[4],i[5],i[4],i[6],i[7],i[6],i[8],i[9],i[8],i[1]]
	if i[0] + i[1] + i[2] == i[3] + i[2] + i[4] == i[5] + i[4] + i[6] == i[7] + i[6] + i[8] == i[9] + i[8] +  i[1] and len(str(i[0])+str(i[1])+str(i[2])+str(i[3])+str(i[2])+str(i[4])+str(i[5])+str(i[4])+str(i[6])+str(i[7])+str(i[6])+str(i[8])+str(i[9])+str(i[8])+str(i[1])) == 16:
		if value[0] < value[3] and value[0] < value[6] and value[0] < value[9] and value[0] < value[12]:
			answer = value
print(''.join(map(str, answer)))