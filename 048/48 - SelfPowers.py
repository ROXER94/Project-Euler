# Calculates the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

sequence = 0
for i in range(1,1000):
	sequence += i**i
print(str(sequence)[-10:])