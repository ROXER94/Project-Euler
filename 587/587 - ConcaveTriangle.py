# Calculates the least value of n for which the concave triangle occupies less than 0.1% of the L-section

from math import pi,sqrt

def func(x):
	return 1 - (1-x**2)**.5
    
def quadratic(a,b,c):
	return round((-b - sqrt((b * b) - 4 * a * c)) / (2 * a),8)

def trapezoid(n):
	return 1 - (1-n**2)**.5

n = 0
blue = 1 - pi/4
while True:
	y = quadratic(n**2 + 1,-(2*n+2),1)
	x = y * n
	dx = (1-x)/50
	area = sum(dx*(trapezoid((i-1)*dx) + trapezoid(i*dx)) / 2 for i in range(1,int((1-x)/dx)+1))
	if (area+x*y/2)/blue < .001: break
	n += 1
print(n)