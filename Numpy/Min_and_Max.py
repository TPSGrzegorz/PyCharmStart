import numpy
N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)],int)
min = numpy.min(my_array, axis = 1)
result = numpy.max(min)
print(result)