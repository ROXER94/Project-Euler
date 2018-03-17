# Calculates the set of four distinct digits for which the longest set of consecutive positive integers from 1 to n can be obtained using arithmetic operators

from itertools import permutations

def RPN(array):
	s = []
	for i in array:
		if i == "+":
			s.append(s.pop() + s.pop())
		elif i == "-":
			s.append(s.pop() - s.pop())
		elif i == "*":
			s.append(s.pop() * s.pop())
		elif i == "/":
			s.append(s.pop() / s.pop())
		else:
			s.append(i)
	return s[0]

limit = 10
maximum = 0
for a in range(1,limit):
	for b in range(a+1,limit):
		for c in range(b+1,limit):
			for d in range(c+1,limit):
				rpn = set()
				for op1 in ["+","-","*","/"]:
					for op2 in ["+","-","*","/"]:
						for op3 in ["+","-","*","/"]:
							for i in permutations([a,b,c,d]):
								try:
									rpn.add(RPN([i[0],i[1],i[2],op1,i[3],op2,op3]))
								except:
									continue
								try:
									rpn.add(RPN([i[0],i[1],i[2],i[3],op1,op2,op3]))
								except:
									continue
				rpn = sorted([int(i) for i in rpn if float(i) > 0 and float(i) % 1 == 0])
				current = 0
				for i in range(len(rpn)):
					if rpn[i]+1 == rpn[i+1]:
						current += 1
					else:
						break
				if current > maximum:
					maximum = current
					value = 1000*a + 100*b + 10*c + d
print(value)
