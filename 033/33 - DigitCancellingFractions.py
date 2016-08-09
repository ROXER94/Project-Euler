# Calculates the simplified denominator of the product of all two-digit digit-cancelled fractions

from fractions import Fraction

numerator = [numerator for numerator in range(11,99)]
denominator = [denominator for denominator in range(12,100)]

answer = 1
for n in numerator:
	for d in denominator:
		if n < d and str(d)[1] != "0":
			value = n/d
			if str(n)[0] == str(d)[0] and int(str(n)[1])/int(str(d)[1]) == value:
				answer *= Fraction(n,d)
			elif str(n)[0] == str(d)[1] and int(str(n)[1])/int(str(d)[0]) == value:
				answer *= Fraction(n,d)
			elif str(n)[1] == str(d)[0] and int(str(n)[0])/int(str(d)[1]) == value:
				answer *= Fraction(n,d)
			elif str(n)[1] == str(d)[1] and int(str(n)[0])/int(str(d)[0]) == value:
				answer *= Fraction(n,d)
print(answer.denominator)