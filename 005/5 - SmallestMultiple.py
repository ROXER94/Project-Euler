# Calculates the smallest positive number that is evenly divisible by all numbers from 1 to 20

from math import gcd
from functools import reduce

# Return lowest common denominator of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Return lowest common denominator of multiple numbers
def lcmm(*args):
    return reduce(lcm, args)

print(lcmm(*range(1,20)))
