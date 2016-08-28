# Calculates the number of semiprimes below 100,000,000

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = [2] + [p for p in range(3,9974,2) if isPrime(p)]
cache = {1:0,2:1,3:2,4:2,5:3,1030927:80767,1123595:87418,1204819:93267,1265822:97595,1369863:104960,1408450:107695,1492537:113642,1639344:123896,1694915:127775,1886792:141116,2127659:157710,2325581:171224,2439024:178920,2702702:196821,3225806:231959,3448275:246788,4347826:305944,5263157:365522,5882352:405279,7692307:520415,9090909:608113,14285714:927432,20000000:1270607,33333333:2050943,50000000:3001134}

for n in range(6,990100):
	if n%2==0:
		cache[n] = cache[n-1]
	elif n%5==0:
		cache[n] = cache[n-1]
	else:
		if isPrime(n):
			cache[n] = cache[n-1] + 1
		else:
			cache[n] = cache[n-1]

total = 0
for k in range(1,1230):
	total += cache[int(100000000/primes[k-1])] - k + 1
print(total)