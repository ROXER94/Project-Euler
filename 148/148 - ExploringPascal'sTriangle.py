# Calculates the number of entries which are not divisible by 7 in the first 1,000,000,000 rows of Pascal's triangle

def add(n):
	result = 1
	for i in str(n):
		result *= int(i)+1
	return result

def triangle(n):
    return n * (n+1) / 2

def Base7(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 7))
        n /= 7
    base7 = ""
    for i in digits[::-1]:
    	base7 += str(i)
    return int(base7.strip("0"))

n = 1000000000
n7 = Base7(n)

sum = 0
for i in range(0,11):
    if len(str(n7)[:i]) == 0:
        value = 1
    else:
        value = add(int(str(n7)[:i]))
    sum += (value) * triangle(int(str(n7)[i])) * 28**(len(str(n7))-i-1)
print(int(sum))