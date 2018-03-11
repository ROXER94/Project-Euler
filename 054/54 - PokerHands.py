# Calculates the number of Poker hands that Player 1 wins

RoyalFlush = ["T","J","Q","K","A"]
def evaluateHand(array):
	numbers = sorted([evaluateDigit(str(array[0])[0]),evaluateDigit(str(array[1])[0]),evaluateDigit(str(array[2])[0]),evaluateDigit(str(array[3])[0]),evaluateDigit(str(array[4])[0])])
	# Same Suit
	if str(array[0])[1] == str(array[1])[1] == str(array[2])[1] == str(array[3])[1] == str(array[4])[1]:
		# Royal Flush
		if str(array[0])[0] in RoyalFlush and str(array[1])[0] in RoyalFlush and str(array[2])[0] in RoyalFlush and str(array[3])[0] in RoyalFlush and str(array[4])[0] in RoyalFlush:
			return (10,10)
		# Straight Flush
		if numbers[0] + 4 == numbers[1] + 3 == numbers[2] + 2 == numbers[3] + 1 == numbers[4]:
			return (9,numbers[-1])
		# Flush
		else:
			return (6,numbers[-1])
	if len(list(set(numbers))) == 2:
		# Full House
		if numbers.count(numbers[0]) == 2 or numbers.count(numbers[0]) == 3:
			return (7,numbers[2])
		# Four of a Kind
		else:
			return (8,numbers[2])
	# Straight
	if numbers[0] + 4 == numbers[1] + 3 == numbers[2] + 2 == numbers[3] + 1 == numbers[4]:
		return (5,numbers[-1])
	if len(list(set(numbers))) == 3:
		# Three of a Kind
		if numbers.count(numbers[0]) == 3 or numbers.count(numbers[2]) == 3 or numbers.count(numbers[4]) == 3:
			return (4,numbers[2])
		# Two Pairs
		if numbers.count(numbers[0]) == 2 and numbers.count(numbers[2]) == 2 or numbers.count(numbers[0]) == 2 and numbers.count(numbers[4]) == 2 or numbers.count(numbers[2]) == 2 and numbers.count(numbers[4]) == 2:
			return (3,max(numbers[1],numbers[3]))
	# One Pair
	if len(list(set(numbers))) == 4:
		return (2,most_common(numbers))
	# High Card
	else:
		return (1,numbers[-1])

def evaluateDigit(string):
	if string.isdigit():
		return int(string)
	else:
		return RoyalFlush.index(string) + 10

def most_common(array):
    return max(set(array),key=array.count)

with open('poker.txt') as file:
	hands = [[digit for digit in line.split()] for line in file]
print(len([i for i in hands if evaluateHand(i[:5])[0] > evaluateHand(i[5:])[0] or evaluateHand(i[:5])[0] == evaluateHand(i[5:])[0] and evaluateHand(i[:5])[1] > evaluateHand(i[5:])[1]]))
