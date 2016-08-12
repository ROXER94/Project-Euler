# Calculates the number of different ways £2 can be made using 1p, 2p, 5p, 10p, 20p, 50p, £1 and £2

count = 1
for pound in range(3):
	for pence50 in range(5):
		if 100 * pound + 50 * pence50 > 200:
			break
		for pence20 in range(11):
			if 100 * pound + 50 * pence50 + 20 * pence20 > 200:
				break
			for pence10 in range(21):
				if 100 * pound + 50 * pence50 + 20 * pence20 + 10 * pence10 > 200:
					break
				for pence5 in range(41):
					if 100 * pound + 50 * pence50 + 20 * pence20 + 10 * pence10 + 5 * pence5 > 200:
						break
					for pence2 in range(101):
						if 100 * pound + 50 * pence50 + 20 * pence20 + 10 * pence10 + 5 * pence5 + 2 * pence2 > 200:
							break
						for pence in range(201):
							if 100 * pound + 50 * pence50 + 20 * pence20 + 10 * pence10 + 5 * pence5 + 2 * pence2 + pence > 200:
								break
							count += 1
							break
print(count)