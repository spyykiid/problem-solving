import numpy as np

arr_ = np.array(map(float, raw_input().split()))
x = int(raw_input())

print np.polyval(arr_, x)
