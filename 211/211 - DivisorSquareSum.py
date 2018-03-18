# Calculates the sum of all positive numbers n below 64,000,000 such that σ2(n) is a perfect square

from math import sqrt

def isSquare(n):
    return int(sqrt(n)+.5)**2 == n

Sum = 0
n = 64000000
o2 = [1]*n
for i in range(2,n):
	for j in range(i,n,i):
		o2[j] += i**2
	if isSquare(o2[i]):
		Sum += i
print(Sum+1)
