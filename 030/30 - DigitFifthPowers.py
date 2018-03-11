# Calculates the sum of all the numbers that can be written as the sum of fifth powers of their digits

print(sum(i for i in range(2,6*9**5) if sum(int(j)**5 for j in str(i)) == i))
