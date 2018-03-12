# Calculates the total of the digital sums of the first one hundred decimal digits for all irrational square roots

from decimal import *
from math import sqrt
getcontext().prec = 102

def isSquare(n):
    return int(sqrt(n)+.5)**2 == n

total = 0
for i in range(1,101):
	if not isSquare(i):
		root = str(Decimal(i).sqrt())
		for j in root[:101]:
			if j != ".":
				total += int(j)
print(total)
