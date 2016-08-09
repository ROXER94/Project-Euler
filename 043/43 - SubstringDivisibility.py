# Calculates the sum of 10-digit pandigital numbers with a unique property

from itertools import permutations

sum = 0
number = 9876543210
perms = [''.join(p) for p in permutations(str(number))]

for i in perms:
	if int(i[1]+i[2]+i[3])%2==0 and int(i[2]+i[3]+i[4])%3==0 and int(i[3]+i[4]+i[5])%5==0 and int(i[4]+i[5]+i[6])%7==0 and int(i[5]+i[6]+i[7])%11==0 and int(i[6]+i[7]+i[8])%13==0 and int(i[7]+i[8]+i[9])%17==0:
		sum += int(i)
print(sum)