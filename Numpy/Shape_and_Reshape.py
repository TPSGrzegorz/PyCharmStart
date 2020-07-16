import numpy

ar = numpy.array([number for number in map(int, input().strip().split())])
ar = ar.reshape(3, 3)

print(ar)
