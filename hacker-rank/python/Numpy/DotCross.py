import numpy as np

N = int(raw_input())
arr_1 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])
arr_2 = np.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])

print np.dot(arr_1, arr_2)
