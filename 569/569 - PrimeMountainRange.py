# Calculates the number of peaks that are visible looking back from the kth mountain for 1 ≤ k ≤ 2500000

def calculateSlope(x1,y1,x2,y2):
	return (y2 - y1) / (x2 - x1)

def P(n):
	D[n] = [n-1]
	currentMinSlope = calculateSlope(peaks[n-1][0],peaks[n-1][1],peaks[n][0],peaks[n][1])
	potentiallyVisible = set(D[n-1])
	while len(potentiallyVisible) != 0:
		thisPeak = max(potentiallyVisible)
		currentSlope = calculateSlope(peaks[thisPeak][0],peaks[thisPeak][1],peaks[n][0],peaks[n][1])
		if currentSlope < currentMinSlope:
			currentMinSlope = currentSlope
			D[n] += [thisPeak]
			potentiallyVisible.update(D[thisPeak])
		potentiallyVisible.remove(thisPeak)
	return len(D[n])


Max = 90000000
primes = []
sieve = [True] * Max
for i in range(2, Max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, Max, i):
			sieve[j] = False

x = y = 0
peaks = [(x,y)]
D = {1:[]}
for (p,q) in zip(primes[::2],primes[1:][::2]):
	x += p
	y += p
	peaks.append((x,y))
	x += q
	y -= q
print(sum(P(i) for i in range(2,2500001)))