# Calculates the sum of factorions greater than two
# A factorion is an integer which is equal to the sum of factorials of its digits

cache_fact = {}

def fact(n):
	if n not in cache_fact.keys():
		cache_fact[n] = factorial_uncached(n)
	return cache_fact[n]
	
def factorial_uncached(n):
    if n == 0 : return 1
    else :
        return n*fact(n-1)
		
array = []
for i in range(10,50000):
	Sum = 0
	for j in str(i):
		Sum += fact(int(j))
	if Sum == i:
		array.append(i)
print(sum(array))