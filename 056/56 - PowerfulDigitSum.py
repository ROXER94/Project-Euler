# Calculates the maximum digital sum of natural numbers of the form a^b for a,b < 100

maximum = 0
for a in range(1,100):
	for b in range(1,100):
		maximum = max(maximum,sum(int(i) for i in str(a**b)))
print(maximum)
