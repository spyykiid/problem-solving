import numpy as np

N = int(raw_input())
arr_ = np.array([map(float, raw_input().split()) for _ in range(N)])

print np.linalg.det(arr_)
