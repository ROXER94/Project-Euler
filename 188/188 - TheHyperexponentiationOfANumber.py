# Calculates the last 8 digits of 1777↑↑1855

a = 1777
b = 1855
e = a
for i in range(b):
	e = pow(a,e,10**8)
print(e)