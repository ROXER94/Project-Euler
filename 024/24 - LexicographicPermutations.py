# Calculates the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

from itertools import permutations
print(sorted([''.join(p) for p in permutations(str(9876543210))])[999999])