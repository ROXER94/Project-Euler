# Calculates the number of distinct arrangements of the two cubes that allow for all of the square numbers to be displayed

total = 0
array = []
squares = ["01","04","09","16","25","36","49","64","81"]

for side1 in range(0,5):
	for side2 in range(side1+1,6):
		for side3 in range(side2+1,7):
			for side4 in range(side3+1,8):
				for side5 in range(side4+1,9):
					for side6 in range(side5+1,10):
						array.append([side1,side2,side3,side4,side5,side6])

for i in range(0,len(array)-1):
	for j in range(i+1,len(array)):
		die1 = array[i][:]
		die2 = array[j][:]
		if 6 in die1 and 9 not in die1:
			die1.append(9)
		elif 9 in die1 and 6 not in die1:
			die1.append(6)
		if 6 in die2 and 9 not in die2:
			die2.append(9)
		elif 9 in die2 and 6 not in die2:
			die2.append(6)
		sq = squares[:]
		for s1 in die1:
			for s2 in die2:
				pair1 = str(s1)+str(s2)
				pair2 = str(s2)+str(s1)
				if pair1 in sq:
					sq.remove(pair1)
				if pair2 in sq:
					sq.remove(pair2)
		if len(sq) == 0:
			total += 1

print(total)