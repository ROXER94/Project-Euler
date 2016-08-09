# Calculates the maximum total from top to bottom of the triangle

array = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

max = 0
for aa in array[0]:
	for a in array[1]:
		for b in array[2]:
		    if -1 < array[2].index(b)-array[1].index(a) < 2:
			    for c in array[3]:
			        if -1 < array[3].index(c)-array[2].index(b) < 2:
				        for d in array[4]:
				            if -1 < array[4].index(d)-array[3].index(c) < 2:
					            for e in array[5]:
					                if -1 < array[5].index(e)-array[4].index(d) < 2:
						                for f in array[6]:
						                    if -1 < array[6].index(f)-array[5].index(e) < 2:
							                    for g in array[7]:
							                        if -1 < array[7].index(g)-array[6].index(f) < 2:
								                        for h in array[8]:
								                            if -1 < array[8].index(h)-array[7].index(g) < 2:
									                            for i in array[9]:
									                                if -1 < array[9].index(i)-array[8].index(h) < 2:
										                                for j in array[10]:
										                                    if -1 < array[10].index(j)-array[9].index(i) < 2:
											                                    for k in array[11]:
											                                        if -1 < array[11].index(k)-array[10].index(j) < 2:
												                                        for l in array[12]:
												                                            if -1 < array[12].index(l)-array[11].index(k) < 2:
													                                            for m in array[13]:
													                                                if -1 < array[13].index(m)-array[12].index(l) < 2:
														                                                for n in array[14]:
														                                                    if -1 < array[14].index(n)-array[13].index(m) < 2:
															                                                    if aa + a + b + c + d + e + f + g + h + i + j + k + l + m + n > max:
																                                                    max = aa + a + b + c + d + e + f + g + h + i + j + k + l + m + n
print(max)