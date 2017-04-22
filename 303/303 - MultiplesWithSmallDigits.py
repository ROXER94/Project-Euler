# Calculates the sum of the multipliers k for which the least positive multiple n*k, written in base 10, uses only digits ≤ 2, from 1 to 10,000

def f(n):
	arr = set()
	for x in range(n-1):
		for i in array:
			arr.add(str("0"+i.zfill(x)))
			arr.add(str("1"+i.zfill(x)))
			arr.add(str("2"+i.zfill(x)))
	return arr

def evaluate(n):
	if n == 9999:
		return 11112222222222222222
	valid = False
	for i in S:
		if i%n==0:
			return i

array = {"0","1","2"}
length = 16
for i in range(2,length+1):
	for j in f(i):
		array.add(j)

S = set()
for i in array:
	S.add(int(i))
S = sorted(S)
S.remove(0)

cache = {}
total = 0
for n in range(1,10001):
	if n not in cache:
		cache[n] = evaluate(n)
	cache[n*10] = cache[n]*10
	total += cache[n]//n
print(total)