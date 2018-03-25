# Calculates the number of prize strings that exist over a 30-day period

cache = {}

def PrizeString(string,numL,numA,D):
	if D == 30:
		return 1
	if numL == 1:
		if numA == 2:
			if (numL,numA,D) not in cache:
				cache[(numL,numA,D)] = PrizeString(string+"O",numL,0,D+1)
			return cache[(numL,numA,D)]
		else:
			if (numL,0,D+1) not in cache:
				cache[numL,0,D+1] = PrizeString(string+"O",numL,0,D+1)
			if (numL,numA+1,D+1) not in cache:
				cache[numL,numA+1,D+1] = PrizeString(string+"A",numL,numA+1,D+1)
			return cache[numL,0,D+1] + cache[numL,numA+1,D+1]
	else:
		if numA == 2:
			if (numL,0,D+1) not in cache:
				cache[numL,0,D+1] = PrizeString(string+"O",numL,0,D+1)
			if (numL+1,0,D+1) not in cache:
				cache[numL+1,0,D+1] = PrizeString(string+"A",numL+1,0,D+1)
			return cache[numL,0,D+1] + cache[numL+1,0,D+1]
		else:
			if (numL,0,D+1) not in cache:
				cache[numL,0,D+1] = PrizeString(string+"O",numL,0,D+1)
			if (numL,numA+1,D+1) not in cache:
				cache[numL,numA+1,D+1] = PrizeString(string+"O",numL,numA+1,D+1)
			if (numL+1,0,D+1) not in cache:
				cache[numL+1,0,D+1] = PrizeString(string+"O",numL+1,0,D+1)
			return cache[numL,0,D+1] + cache[numL,numA+1,D+1] + cache[numL+1,0,D+1]

print(PrizeString("",0,0,0))
