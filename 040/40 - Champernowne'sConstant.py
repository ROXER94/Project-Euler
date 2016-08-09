# Calculates the product of the 1st, 10th, 100th, 1000th, 10,000th, 100,000th, and 1,000,000th digits in Champernowne's Constant

Champernowne = ""
number = 1
while len(Champernowne) < 1000000:
	Champernowne += str(number)
	number += 1
print(int(Champernowne[0])*int(Champernowne[9])*int(Champernowne[99])*int(Champernowne[999])*int(Champernowne[9999])*int(Champernowne[99999])*int(Champernowne[999999]))