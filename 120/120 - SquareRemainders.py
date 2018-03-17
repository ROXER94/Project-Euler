# Calculates the sum of the maximum remainders of ((a−1)^n + (a+1)^n) / a^2 for 3 ≤ a ≤ 1000

print(sum((i + i % 2 - 2) * i for i in range(3,1001)))
