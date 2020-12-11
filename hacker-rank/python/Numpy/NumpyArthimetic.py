import numpy as np

N, M = map(int, raw_input().strip().split())
array_1 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])
array_2 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])

print array_1 + array_2
print array_1 - array_2
print array_1 * array_2
print array_1 / array_2
print np.mod(array_1, array_2)
print np.power(array_1, array_2)
