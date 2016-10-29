# Calculates the sum of the ASCII values in the original message of the text file

array = [int(i) for i in open('cipher.txt', 'r').read().split(',')]
for p1 in range(97,123):
	for p2 in range(97,123):
		for p3 in range(97,123):
			current = zip([chr(i^p1) for i in [j for j in array[::3]]],[chr(i^p2) for i in [j for j in array[1::3]]],[chr(i^p3) for i in [j for j in array[2::3]]])
			text = ''.join([x for a in current for x in a])
			if " the " in text:
				print(sum(ord(c) for c in text) + (array[-1]^p1))
				quit()