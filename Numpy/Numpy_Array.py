import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    ar = numpy.array(arr, float)
    return numpy.flip(ar)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
