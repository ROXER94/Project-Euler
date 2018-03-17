# Calculates the smallest number greater than 10^15 that has a specific modified Collatz sequence

def D(n):
	return 3*n

def U(n):
	return (3*n-2)/4

def d(n):
	return (3*n+1)/2

string = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"[::-1]
n = 1
while True:
	original = n
	for i in string:
		if i =="D":
			n = D(n)
			if n % 1 != 0:
				break
		elif i == "U":
			n = U(n)
			if n % 1 != 0:
				break
		else:
			n = d(n)
			if n % 1 != 0:
				break
	if n % 1==0 and n > 10**15:
		break
	n = original+69
print(int(n))
