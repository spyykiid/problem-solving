import numpy

N, M = map(int, raw_input().strip().split(' '))

arr_ = []
for _ in range(N):
    arr_ += map(int, raw_input().strip().split(' '))
arr_ = numpy.array(arr_)
arr_.shape = (N, M)

print numpy.transpose(arr_)
print arr_.flatten()
