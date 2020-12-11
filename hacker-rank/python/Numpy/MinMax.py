import numpy

N, M = map(int, raw_input().strip().split())
arr_ = numpy.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])

print numpy.max(numpy.min(arr_, axis=1))
