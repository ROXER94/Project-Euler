# Calculates the largest palindrome made from the product of two 3-digit numbers

# Determines if a number is palindromic
def palindrome(n):
    return str(n) == str(n)[::-1]

# Determines if a number is the product of two 3-digit numbers
def threedigitprod(n):
	for i in range(100,999):
		if n%i==0 and len(str(n//i)) == 3:
			return True
	return False

for i in range(998001,10000,-1):
	if palindrome(i) and threedigitprod(i):
		print(i)
		break
