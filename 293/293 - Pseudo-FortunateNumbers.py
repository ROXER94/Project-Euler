# Calculates the sum of all distinct pseudo-Fortunate numbers for admissible numbers less than 10^9

from time import time
start = time()

from math import log
max = 10**9
def primes(n):
	P = {2:True}
	sieve = [True] * n
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
	for i in range(3,n,2):
		if sieve[i]:
			P[i] = True
	return P

P = primes(max)

n = max
array = []
for a in range(int(log(n,2))+1):
	for b in range(int(log(n//2,3))+1):
		if 2**a*3**b < n:
			for c in range(int(log(n//2,5))+1):
				if 2**a*3**b*5**c < n:
					for d in range(int(log(n//2,7))+1):
						if 2**a*3**b*5**c*7**d < n:
							for e in range(int(log(n//2,11))+1):
								if 2**a*3**b*5**c*7**d*11**e < n:
									for f in range(int(log(n//2,13))+1):
										if 2**a*3**b*5**c*7**d*11**e*13**f < n:
											for g in range(int(log(n//2,17))+1):
												if 2**a*3**b*5**c*7**d*11**e*13**f*17**g < n:
													for h in range(int(log(n//2,19))+1):
														if 2**a*3**b*5**c*7**d*11**e*13**f*17**g*19**h < n:
															for i in range(int(log(n//2,23))+1):
																if 2**a*3**b*5**c*7**d*11**e*13**f*17**g*19**h*23**i < n:
																	if a > 0 and b == c == d == e == f == g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c == d == e == f == g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d == e == f == g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d > 0 and e == f == g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f == g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0 and g == h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0 and g > 0 and h == i == 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
																	if a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0 and g > 0 and h > 0:
																		value = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i
																		if value < n:
																			array.append(value)
S = set()
for N in array:
	M = 3
	test = False
	while not test:
		try:
			if P[N+M]:
				test = True
		except:
			M += 2
	S.add(M)
print(sum(S))
print(time()-start)