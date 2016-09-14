# Calculates the number of different square laminae that can be formed using up to 1,000,000 tiles

n = 1000000
count = 0
for l in range(3,n//4 + 2):
	for s in range(l-2,0,-2):
		if l**2 - s**2 <= n:
			count += 1
		else:
			break
print(count)
