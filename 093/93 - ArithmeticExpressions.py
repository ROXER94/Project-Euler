# Calculates the set of four distinct digits for which the longest set of consecutive positive integers from 1 to n can be obtained

from itertools import permutations

def RPN(array):
    newarray = []
    for i in array:
        if i == "+":
            newarray.append(newarray[-1] + newarray[-2])
            del newarray[-2]
            del newarray[-2]
        elif i == "-":
            newarray.append(newarray[-1] - newarray[-2])
            del newarray[-2]
            del newarray[-2]
        elif i == "*":
            newarray.append(newarray[-1] * newarray[-2])
            del newarray[-2]
            del newarray[-2]
        elif i == "/":
            newarray.append(newarray[-1] / newarray[-2])
            del newarray[-2]
            del newarray[-2]
        else:
            newarray.append(i)
    return newarray[0]
    
def f(array):
	newarray = []
	for i in list(permutations(array)):
		try:
			value = RPN(i)
			if value%1==0 and value > 0:
				newarray.append(value)
		except IndexError:
			continue
		except ZeroDivisionError:
			continue
	return newarray

consecutive = 0
n = 10
for a in range(1,n):
	for b in range(a+1,n):
		for c in range(b+1,n):
			for d in range(c+1,n):
				array = []
				array.append(RPN([a,b,c,d,"+","+","+"]))
				array.append(RPN([a,b,c,d,"*","*","*"]))
				array += f([a,b,c,d,"-","+","+"])
				array += f([a,b,c,d,"*","+","+"])
				array += f([a,b,c,d,"/","+","+"])
				array += f([a,b,c,d,"-","*","*"])
				array += f([a,b,c,d,"+","*","*"])
				array += f([a,b,c,d,"/","*","*"])
				array += f([a,b,c,d,"+","-","-"])
				array += f([a,b,c,d,"*","-","-"])
				array += f([a,b,c,d,"/","-","-"])
				array += f([a,b,c,d,"-","/","/"])
				array += f([a,b,c,d,"*","/","/"])
				array += f([a,b,c,d,"+","/","/"])
				array += f([a,b,c,d,"-","*","+"])
				array += f([a,b,c,d,"-","/","+"])
				array += f([a,b,c,d,"+","*","/"])
				array += f([a,b,c,d,"-","*","/"])
				array = sorted(list(set(array)))
				count = 0
				for i in range(len(array)):
					if array[i] + 1 == array[i+1]:
						count += 1
					else:
						break
				if count > consecutive:
					consecutive = count
					w = a
					x = b
					y = c
					z = d
print(str(w)+str(x)+str(y)+str(z))
