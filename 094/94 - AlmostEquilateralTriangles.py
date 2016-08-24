# Calculates the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed 1,000,000,000

previous = 1
s = 5
t = -1
sum = 0
while s < 333333334:
	sum += 3*s - t
	p = s
	s = 4*s - previous + 2*t
	t *= -1
	previous = p
print(sum)