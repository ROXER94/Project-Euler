# Calculates the sum of all unique De Bruijn sequences of length 32

binary = []
for i in range(32):
	binary.append(bin(i)[2:].zfill(5))

sum = 0
array = []
for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for f in range(2):
						for g in range(2):
							for h in range(2):
								for i in range(2):
									for j in range(2):
										for k in range(2):
											for l in range(2):
												for m in range(2):
													for n in range(2):
														for o in range(2):
															for p in range(2):
																for q in range(2):
																	for r in range(2):
																		for s in range(2):
																			for t in range(2):
																				value = "000001"+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)+str(s)+str(t)
																				if value.count("0") <= 15 and value.count("1") <= 14:
																					array.append(value)
for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for i in array:
						value = i+str(a)+str(b)+str(c)+str(d)+str(e)+"1"
						if value.count("0") == 16:
							valid = True
							for j in binary:
								if j in value:
									continue
								elif j in value[-4:]+value[:4]:
    									continue
								else:
									valid = False
									break
							if valid:
								sum += int(value,2)
print(sum)
