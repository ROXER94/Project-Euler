# Calculates the largest palindrome made from the product of two 3-digit numbers

# Determines if a number is palindromic
def palindrome(number):
    if str(number) == str(number)[::-1]: 
        return True
    return False

# Determines if a number is the product of two 3-digit numbers
def threedigitprod(n):
	for i in range(100,999):
		if n%i==0 and len(str(int(n/i))) == 3:
			return True
	return False

number = 0
for i in range(998001,10000,-1):
	if palindrome(i) and threedigitprod(i):
		if i > number:
			number = i
print(number)