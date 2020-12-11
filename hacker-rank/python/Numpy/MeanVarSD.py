import numpy

N, M = map(int, raw_input().strip().split())
arr_ = numpy.array([map(int, raw_input().strip().split(' ')) for _ in range(N)])

print numpy.mean(arr_, axis=1)
print numpy.var(arr_, axis=0)
print numpy.std(arr_, axis=None)
