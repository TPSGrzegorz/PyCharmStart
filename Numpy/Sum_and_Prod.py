import numpy
N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(my_array, axis=0), axis=0))
