# Calculates the difference between the sum of the squares of the first one hundred numbers and the square of the sum

print(sum((x for x in range(1,101)))**2-sum((x**2 for x in range(1,101))))
