import numpy as np

shape = tuple(map(int, raw_input().strip().split()))

print np.zeros(shape, dtype=int)
print np.ones(shape, dtype=int)
