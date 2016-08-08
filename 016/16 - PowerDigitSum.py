# Calculates the sum of the digits of the number 2^1000

sum = 0
number = 2**1000
for i in str(number):
	sum += int(i)
print(sum)