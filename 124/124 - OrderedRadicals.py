# Calculates the value of n in the 10,000th row of the sorted column of rad(n) for 1 ≤ n ≤ 100,000
# The radical of n, rad(n), is the product of the distinct prime factors of n

def radical(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    product = 1
    for i in list(set(factors)):
    	product *= i
    return product

array = []
k = 10000
for i in range(1,100001):
	array.append((radical(i),i))
print(sorted(array)[k-1][1])