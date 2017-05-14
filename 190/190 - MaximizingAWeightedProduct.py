# Calculates Σ[Pm] for 2 ≤ m ≤ 15

from functools import reduce
from operator import mul

print(sum(int(reduce(mul,[(2*i*n/(n*(n+1)))**i for i in range(1,n+1)],1)) for n in range(2,16)))