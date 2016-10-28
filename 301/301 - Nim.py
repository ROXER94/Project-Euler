# Calculates the number of positive integers n ≤ 2^30 for which X(n,2n,3n) = 0 

print(len([i for i in range(1,2**30+1) if not i^2*i^3*i]))