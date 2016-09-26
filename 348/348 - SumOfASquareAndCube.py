# Calculates the sum of the five smallest palindromic numbers that are the sum of square and a cube

from collections import Counter

def isPanlindrome(n):
	return str(n) == str(n)[::-1]

palindromes = Counter()
for s in range(2,30000):
	for c in range(2,1000):
		value = s**2 + c**3
		if isPanlindrome(value):
			palindromes[value] += 1
print(sum(i[0] for i in palindromes.most_common(5)))