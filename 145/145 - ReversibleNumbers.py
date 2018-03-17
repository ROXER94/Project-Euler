# Calculates the number of reversible numbers below 1,000,000,000

def Reverse(n):
	if str(n)[-1] == "0":
		return False
	value = str(n + int(str(n)[::-1]))
	if "0" in value or "2" in value or "4" in value or "6" in value or "8" in value:
		return False
	return True

print(sum(1 for i in range(1,100000000) if Reverse(i)))
