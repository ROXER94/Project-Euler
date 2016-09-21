# Calculates the number of characters saved by writing each line of the text file in its minimal Roman Numeral form

def RomanReplace(string):
	count = 0
	while "IIII" in string:
		string = string.replace("IIII","IV")
		count += 2
	while "VIV" in string:
		string = string.replace("VIV","IX")
		count += 1
	while "XXXX" in string:
		string = string.replace("XXXX","XL")
		count += 2
	while "LXL" in string:
		string = string.replace("LXL","XC")
		count += 1
	while "CCCC" in string:
		string = string.replace("CCCC","CD")
		count += 2
	while "DCD" in string:
		string = string.replace("DCD","CM")
		count += 1
	return count

print(sum(RomanReplace(line.replace("\n","")) for line in open("roman.txt")))