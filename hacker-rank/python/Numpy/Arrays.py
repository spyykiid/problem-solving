import numpy


def arrays(arr):
    ar = numpy.array(arr, float)
    return numpy.flip(ar, 0)


arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
