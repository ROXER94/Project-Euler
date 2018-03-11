# Calculates the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

def permute(n):
	return len(str(2*n)) == len(str(3*n)) == len(str(4*n)) == len(str(5*n)) == len(str(6*n)) and match(2*n,3*n) and match(3*n,4*n) and match(4*n,5*n) and match(5*n,6*n)

def match(n1,n2):
    return sorted(str(n1)) == sorted(str(n2))

n = 1
while True:
	if permute(n):
		print(n)
		break
	else:
		n += 1
