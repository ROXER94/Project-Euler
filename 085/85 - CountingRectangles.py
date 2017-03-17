# Calculates the area of the grid that contains nearly 2,000,000 rectangles

def rectCount(length,width):
	return length*width*(length+1)*(width+1)//4

difference = 100
for l in range(1,1000):
	for w in range(l,1000):
		current = rectCount(l,w)
		if abs(2000000-current) < difference:
			difference = abs(2000000-current)
			x = l
			y = w
print(x*y)z
