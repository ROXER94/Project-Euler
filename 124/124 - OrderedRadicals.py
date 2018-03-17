# Calculates the value of n in the 10,000th row of the sorted column of rad(n) for 1 ≤ n ≤ 100,000
# The radical of n, rad(n), is the product of the distinct prime factors of n

N = 100000
rad = [1]*N
for i in range(2,N):
	if rad[i] == 1:
		for j in range(i,N,i):
			rad[j] *= i
array = []
for i in range(N):
	array.append((rad[i],i))
array = sorted(array)
print(array[9999][1])
