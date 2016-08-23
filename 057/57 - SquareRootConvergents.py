# Calculates the number of fractions that contain a numerator with more digits than denominator in the first 1000 expansions of the continued fraction of √2

count = 0
n = 3
d = 2
iteration = 1
while iteration != 1001:
	if len(str(n)) > len(str(d)):
		count += 1
	n2 = 2*d + n
	d2 = n + d
	n,d = n2,d2
	iteration += 1
print(count)