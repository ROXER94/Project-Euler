# Calculates the number of squarefree numbers below 2^50

from math import sqrt

def Moebius(max):
	Sqrt = int(sqrt(max))
	mu = [1] * (max+1)
	for i in range(2,Sqrt+1):
		if mu[i] == 1:
			for j in range(i,max+1,i):
				mu[j] *= -i
			for j in range(i*i,max+1,i*i):
				mu[j] = 0
	for i in range(2,max+1):
		if mu[i] == i:
			mu[i] = 1
		elif mu[i] == -i:
			mu[i] = -1
		elif mu[i] < 0:
			mu[i] = 1
		elif mu[i] > 0:
			mu[i] = -1
	return mu

N = 2**50
M = Moebius(int(sqrt(N)))
print(sum(M[i]*int(N/i**2) for i in range(1,int(sqrt(N))+1)))