# Calculates the number of triangles in the text file for which the interior contains the origin

def Area(x0,y0,x1,y1,x2,y2):
	return .5 * (-y1 * x2 + y0 * (-x1 + x2) + x0 * (y1 - y2) + x1 * y2)

def S(x0,y0,x1,y1,x2,y2):
	return 1 / (2 * Area(x0,y0,x1,y1,x2,y2)) * (y0 * x2 - x0 * y2)

def T(x0,y0,x1,y1,x2,y2):
	return 1 / (2 * Area(x0,y0,x1,y1,x2,y2)) * (x0 * y1 - y0 * x1)

count = 0
with open("triangles.txt") as file:
	for line in file:
		(x0,y0,x1,y1,x2,y2) = line.split(",")
		(x0,y0,x1,y1,x2,y2) = (int(x0),int(y0),int(x1),int(y1),int(x2),int(y2))
		s = S(x0,y0,x1,y1,x2,y2)
		t = T(x0,y0,x1,y1,x2,y2)
		if s > 0 and t > 0 and 1 - s - t > 0:
			count += 1
print(count)