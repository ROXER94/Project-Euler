# Calculates the sum of the score of each name in the text file

import string

lettertonumber=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))

names = sorted(''.join(open("names.txt").read()).replace('"', '').strip().split(','))

print(sum(sum(lettertonumber[j] for j in str(i)) * (names.index(i)+1) for i in names))
