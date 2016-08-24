# Calculates the sum of the maximum remainders of ((a−1)^n + (a+1)^n) / a^2 for 3 ≤ a ≤ 1000

sum = 0
for a in range(3,1001):
	max = 0
	for n in range(1,1500):
		current = ((a-1)**n + (a+1)**n) % a**2
		if current > max:
			max = current
	sum += max
print(sum)