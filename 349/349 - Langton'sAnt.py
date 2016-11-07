# Calculates the number of squares that are black after 10^18 moves of Langton's Ant

n = 9984
current = (0,0)
direction = 'up'
d = {}
for m in range(n):
	try:
		# White
		if d[current] == 0:
			d[current] = 1
			if direction == 'up':
				direction = 'right'
				current = (current[0]+1,current[1])
			elif direction == 'right':
				direction = 'down'
				current = (current[0],current[1]-1)
			elif direction == 'down':
				direction = 'left'
				current = (current[0]-1,current[1])
			else:
				direction = 'up'
				current = (current[0],current[1]+1)
		# Black
		else:
			d[current] = 0
			if direction == 'up':
				direction = 'left'
				current = (current[0]-1,current[1])
			elif direction == 'right':
				direction = 'up'
				current = (current[0],current[1]+1)
			elif direction == 'down':
				direction = 'right'
				current = (current[0]+1,current[1])
			else:
				direction = 'down'
				current = (current[0],current[1]-1)
	except:
		d[current] = 1
		if direction == 'up':
			direction = 'right'
			current = (current[0]+1,current[1])
		elif direction == 'right':
			direction = 'down'
			current = (current[0],current[1]-1)
		elif direction == 'down':
			direction = 'left'
			current = (current[0]-1,current[1])
		else:
			direction = 'up'
			current = (current[0],current[1]+1)
print(int(sum(d.values()) + (10**18-n)/104*12) - 8)