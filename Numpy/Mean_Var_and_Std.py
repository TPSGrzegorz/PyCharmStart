import numpy
N, M = map(int, input().split())
numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')
my_array = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))

print(numpy.std(my_array))
