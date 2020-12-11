import numpy as np

N, M, P = map(int, raw_input().strip().split(' '))
arr_1 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])
arr_2 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(M)])

print np.concatenate((arr_1, arr_2), axis=0)
