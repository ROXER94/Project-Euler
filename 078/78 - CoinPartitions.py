# Calculates the smallest value of n for which p(n) is divisible by one million

n = 60000
ways = [0] * (n+1)
ways[0] = 1

for i in range (1,n+1):
    for j in range(i, n+1):
        ways[j] = ways[j] + ways[j - i]
    if ways[i] % 1000000 == 0:
    	print(i)
    	break