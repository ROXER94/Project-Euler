# Calculates the number of n-digit positive integers which are also an nth power

print(len([i for i in range(1,10) for j in range(1,25) if len(str(i**j)) == j]))