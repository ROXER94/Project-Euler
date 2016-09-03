# Calculates the number of ways a 4x4 grid can be filled with the digits d, 0 ≤ d ≤ 9 so that each row, column, and diagonal have the same sum

'''
a b c d
e f g h
i j k l
m n o p
'''

count = 0
for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				sum = a + b + c + d
				for e in range(10):
					for i in range(10):
						for m in range(10):
							if a + e + i + m == sum:
								for g in range(10):
									for j in range(10):
										if d + g + j + m == sum:
											for f in range(10):
												for h in range(10):
													if e + f + g + h == sum:
														for n in range(10):
															if b + f + j + n == sum:
																for k in range(10):
																	for p in range(10):
																		if a + f + k + p == sum:
																			for l in range(10):
																				if d + h + l + p == sum == i + j + k + l:
																					for o in range(10):
																						if c + g + k + o == sum == m + n + o + p:
																							count += 1
print(count)