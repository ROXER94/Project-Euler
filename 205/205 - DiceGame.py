# Calculates the probability that Pyramidal Pete beats Cubic Colin

Colin = []
for a in range(1,7):
	for b in range(1,7):
		for c in range(1,7):
			for d in range(1,7):
				for e in range(1,7):
					for f in range(1,7):
						Colin.append(a+b+c+d+e+f)

Peter = []
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			for d in range(1,5):
				for e in range(1,5):
					for f in range(1,5):
						for g in range(1,5):
							for h in range(1,5):
								for i in range(1,5):
									Peter.append(a+b+c+d+e+f+g+h+i)

P = {}
C = {}
for i in range(6,37):
	P[i] = Peter.count(i)
	C[i] = Colin.count(i)

print(round(sum(C[c]*P[p] for c in range(6,36) for p in range(c+1,37))/(len(Peter)*len(Colin)),7))