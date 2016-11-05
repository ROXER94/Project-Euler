# Calculates the number of blue discs in the arrangement for which the probability of taking two blue discs is 1/2 and the arrangement contains over 1,000,000,000,000 discs in total

x,y = 15,21
while y < 1000000000000:
	x,y = 3*x + 2*y - 2,4*x + 3*y - 3
print(x)