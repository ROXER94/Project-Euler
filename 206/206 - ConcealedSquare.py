# Calculates the only positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0

def Concealed(n):
	n = str(n)
	return n[0] == "1" and n[2] == "2" and n[4] == "3" and n[6] == "4" and n[8] == "5" and n[10] == "6" and n[12] == "7" and n[14] == "8" and n[16] == "9" and n[18] == "0"

n = (10**9+10**7+10**5+10**3+10**1+20)
b = True
while not Concealed(n**2):
	if b:
		n += 40
	else:
		n += 60
	b = not b
print(n)
