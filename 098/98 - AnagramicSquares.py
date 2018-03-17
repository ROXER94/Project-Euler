# Calculates the largest square number formed by any member of a pair of anagramic squares in the text file

def isAnagam(word1,word2):
	return sorted(word1) == sorted(word2)

array = ''.join(open("words.txt").read()).replace('"', '').strip().split(',')
anagrams = []
for i in range(len(array)-1):
	for j in range(i+1,len(array)):
		if isAnagam(array[i],array[j]):
			if len(set(array[i])) == len(array[i]):
				anagrams.append((array[i],array[j]))

squares3 = [n**2 for n in range(10,32)]
squares3anagrams = []
for i in range(len(squares3)-1):
	for j in range(i+1,len(squares3)):
		if isAnagam(str(squares3[i]),str(squares3[j])):
			if len(set(str(squares3[i]))) == len(str(squares3[i])):
				squares3anagrams.append((squares3[i],squares3[j]))
			
squares4 = [n**2 for n in range(32,100)]
squares4anagrams = []
for i in range(len(squares4)-1):
	for j in range(i+1,len(squares4)):
		if isAnagam(str(squares4[i]),str(squares4[j])):
			if len(set(str(squares4[i]))) == len(str(squares4[i])):
				squares4anagrams.append((squares4[i],squares4[j]))

squares5 = [n**2 for n in range(100,316)]
squares5anagrams = []
for i in range(len(squares5)-1):
	for j in range(i+1,len(squares5)):
		if isAnagam(str(squares5[i]),str(squares5[j])):
			if len(set(str(squares5[i]))) == len(str(squares5[i])):
				squares5anagrams.append((squares5[i],squares5[j]))

squares6 = [n**2 for n in range(316,1000)]
squares6anagrams = []
for i in range(len(squares6)-1):
	for j in range(i+1,len(squares6)):
		if isAnagam(str(squares6[i]),str(squares6[j])):
			if len(set(str(squares6[i]))) == len(str(squares6[i])):
				squares6anagrams.append((squares6[i],squares6[j]))

anagramicSquares = []
for i in anagrams:
	if len(i[0]+i[1])//2 == 3:
		a = i[1].index(i[0][0])
		b = i[1].index(i[0][1])
		c = i[1].index(i[0][2])
		for j in squares3anagrams:
			if a == str(j[1]).index(str(j[0])[0]) and b == str(j[1]).index(str(j[0])[1]) and c == str(j[1]).index(str(j[0])[2]):
				anagramicSquares.append(j[1])
	if len(i[0]+i[1])//2 == 4:
		a = i[1].index(i[0][0])
		b = i[1].index(i[0][1])
		c = i[1].index(i[0][2])
		d = i[1].index(i[0][3])
		for j in squares4anagrams:
			if a == str(j[1]).index(str(j[0])[0]) and b == str(j[1]).index(str(j[0])[1]) and c == str(j[1]).index(str(j[0])[2]) and d == str(j[1]).index(str(j[0])[3]):
				anagramicSquares.append(j[1])
	if len(i[0]+i[1])//2 == 5:
		a = i[1].index(i[0][0])
		b = i[1].index(i[0][1])
		c = i[1].index(i[0][2])
		d = i[1].index(i[0][3])
		e = i[1].index(i[0][4])
		for j in squares5anagrams:
			if a == str(j[1]).index(str(j[0])[0]) and b == str(j[1]).index(str(j[0])[1]) and c == str(j[1]).index(str(j[0])[2]) and d == str(j[1]).index(str(j[0])[3]) and e == str(j[1]).index(str(j[0])[4]):
				anagramicSquares.append(j[1])
	if len(i[0]+i[1])//2 == 6:
		a = i[1].index(i[0][0])
		b = i[1].index(i[0][1])
		c = i[1].index(i[0][2])
		d = i[1].index(i[0][3])
		e = i[1].index(i[0][4])
		f = i[1].index(i[0][5])
		for j in squares6anagrams:
			if a == str(j[1]).index(str(j[0])[0]) and b == str(j[1]).index(str(j[0])[1]) and c == str(j[1]).index(str(j[0])[2]) and d == str(j[1]).index(str(j[0])[3]) and e == str(j[1]).index(str(j[0])[4]) and f == str(j[1]).index(str(j[0])[5]):
				anagramicSquares.append(j[1])
print(max(anagramicSquares))
