# Calculates the maximum digital sum of natural numbers of the form a^b for a,b < 100

maximum = 0

for a in range(1,100):
	for b in range(1,100):
		current = 0
		for x in str(a**b):
			current += int(x)
		if current > maximum:
			maximum = current
print(maximum)