# Calculates the sum of all the numbers less than 100,000,000 that are both palindromic and can be written as the sum of consecutive squares

array = [n**2 for n in range(1,7075)]

squarePalindromes = [i for i in array if str(i) == str(i)[::-1]]
palindromes = []
index = 0
while index != len(array):
	value = 0
	for i in array[index:]:
		if value + i < 100000000:
			value += i
			if str(value) == str(value)[::-1]:
				palindromes.append(value)
	index += 1

print(sum(list(set(palindromes)))-sum(squarePalindromes))
