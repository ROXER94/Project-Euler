# Calculates the number of triangle words in the text file

import string

def triangle(n):
	return int(n * (n+1)/2)

lettertonumber=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))
words = sorted(''.join(open("words.txt").read()).replace('"', '').strip().split(','))

triangles = []
for i in range(30):
	triangles.append(triangle(i))

count = 0
for i in words:
	value = 0
	for j in str(i):
		value += lettertonumber[j]
	if value in triangles:
		count += 1
print(count)