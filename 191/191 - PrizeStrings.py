# Calculates the number of prize strings that exist over a 30-day period

cache = {}

def PrizeString(string,numD,numA,D):
	if D == 30:
		return 1
	if numD == 1:
		if numA == 2:
			if (numD,numA,D) not in cache:
				cache[(numD,numA,D)] = PrizeString(string+"O",numD,0,D+1)
			return cache[(numD,numA,D)]
		else:
			if (numD,0,D+1) not in cache:
				cache[numD,0,D+1] = PrizeString(string+"O",numD,0,D+1)
			if (numD,numA+1,D+1) not in cache:
				cache[numD,numA+1,D+1] = PrizeString(string+"A",numD,numA+1,D+1)
			return cache[numD,0,D+1] + cache[numD,numA+1,D+1]
	else:
		if numA == 2:
			if (numD,0,D+1) not in cache:
				cache[numD,0,D+1] = PrizeString(string+"O",numD,0,D+1)
			if (numD+1,0,D+1) not in cache:
				cache[numD+1,0,D+1] = PrizeString(string+"A",numD+1,0,D+1)
			return cache[numD,0,D+1] + cache[numD+1,0,D+1]
		else:
			if (numD,0,D+1) not in cache:
				cache[numD,0,D+1] = PrizeString(string+"O",numD,0,D+1)
			if (numD,numA+1,D+1) not in cache:
				cache[numD,numA+1,D+1] = PrizeString(string+"O",numD,numA+1,D+1)
			if (numD+1,0,D+1) not in cache:
				cache[numD+1,0,D+1] = PrizeString(string+"O",numD+1,0,D+1)
			return cache[numD,0,D+1] + cache[numD,numA+1,D+1] + cache[numD+1,0,D+1]

print(PrizeString("",0,0,0))