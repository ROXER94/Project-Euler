# Calculates the number of pairs of consecutive integers which have the same number of divisors

n = 10000000
count = 0
divisors = [1]*n
for i in range(2,n):
	for j in range(i+i,n,i):
		divisors[j] += 1
	if divisors[i] == divisors[i-1]:
		count += 1
print(count-1)