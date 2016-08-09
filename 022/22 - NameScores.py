# Calculates the sum of the score of each name in the text file

import string

lettertonumber=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))

names = sorted(''.join(open("names.txt").read()).replace('"', '').strip().split(','))

totalscore = 0

for i in names:
	score = 0
	for j in str(i):
		score += lettertonumber[j]
	totalscore += score * (names.index(i) + 1)
print(totalscore)