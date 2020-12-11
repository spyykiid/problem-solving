import numpy as np

array_ = np.array(map(float, raw_input().strip().split(' ')))

print np.floor(array_)
print np.ceil(array_)
print np.rint(array_)
