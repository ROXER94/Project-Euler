# Calculates the sum of numbers under 1,000,000 that are palindromes in both decimal and binary

Range = 1000000

# Determines if a number is palindromic
def palindrome(number):
    if str(number) == str(number)[::-1]: 
        return True
    return False

# Generate numbers in the range
numbers = []
for i in range(1,Range+1):
	numbers.append(i)

# Generates the decimal palindromic numbers 
palindromes = []
for i in numbers:
	if palindrome(i):
		palindromes.append(i)

# Converts to binary
binarytemp = []
binary = []
for i in palindromes:
	binarytemp.append(int(bin(i)[2:]))
for i in binarytemp:
	if str(i)[0] != "0":
		binary.append(i)

tempfinal = []
final = []

# Generates the binary palindromic numbers
for i in binary:
	if palindrome(i):
		tempfinal.append(i)

# Coverts back to decimal
for i in tempfinal:
	final.append(int(str(i),2))

# Prints sum of palindromic binary/decimal numbers
print(sum(final))