# Calculates the number of right triangles that can be formed with integer coordinates in a given range and joined at the origin

def right(x1,y1,x2,y2,x3,y3):
	s1 = distance(x1,y1,x2,y2)
	s2 = distance(x2,y2,x3,y3)
	s3 = distance(x1,y1,x3,y3)
	array = sorted([s1,s2,s3])
	return round(array[0]**2 + array[1]**2,1) == round(array[2]**2,1)

def distance(x1,y1,x2,y2):
	return ((x2-x1) ** 2 + (y2-y1) ** 2) ** .5

n = 50
s = []
count = 0
for x1 in range(1,n+1):
	for y1 in range(0,n+1):
		for x2 in range(0,n+1):
			for y2 in range(1,n+1):
				if right(0,0,x1,y1,x2,y2) and ((x1,y1),(x2,y2)) not in s and ((x2,y2),(x1,y1)) not in s:
					s.append(((x1,y1),(x2,y2)))
					count += 1
print(count-n**2)
