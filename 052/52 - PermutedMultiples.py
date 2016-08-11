# Calculates the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

def permute(n):
	if len(str(2*n)) == len(str(3*n)) == len(str(4*n)) == len(str(5*n)) == len(str(6*n)):
		double = 2*n
		triple = 3*n
		quadruple = 4*n
		quintuple = 5*n
		sextuple = 6*n
		if match(double,triple) and match(triple,quadruple) and match(quadruple,quintuple) and match(quintuple,sextuple):
			return True
	return False

def match(n1,n2):
    for i in str(n1):
        if i in str(n2):
            continue
        else:
            return False
    return True

number = 1
while True:
	if permute(number):
		print(number)
		break
	else:
		number += 1