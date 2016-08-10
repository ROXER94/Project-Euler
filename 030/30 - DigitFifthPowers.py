# Calculates the sum of all the numbers that can be written as the sum of fifth powers of their digits

sum = 0
for i in range(2,6*9**5):
	total = 0
	for j in str(i):
		total += int(j)**5
	if total == i:
		sum += i
print(sum)