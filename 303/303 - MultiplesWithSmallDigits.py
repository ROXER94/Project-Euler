# Calculates the sum of the multipliers k for which the least positive multiple n*k, written in base 10, uses only digits ≤ 2, from 1 to 10,000

def SmallDigitMultiple(n):
	for i in multiples:
		if i % n == 0:
			return i
	return 0

multiples = set()
for a in range(3):
	for b in range(3):
		for c in range(3):
			for d in range(3):
				for e in range(3):
					for f in range(3):
						for g in range(3):
							for h in range(3):
								for i in range(3):
									for j in range(3):
										for k in range(3):
											for l in range(3):
												for m in range(3):
													for n in range(3):
														for o in range(3):
															for p in range(3):
																multiples.add(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)))
multiples.remove(0)
dict = {}
Sum = 0
for n in range(1,9999):
	if n not in dict.keys():
		dict[n] = SmallDigitMultiple(n)
	dict[10*n] = 10*dict[n]
	Sum += dict[n]//n
print(Sum + 11112222222222222222//9999 + 1)
