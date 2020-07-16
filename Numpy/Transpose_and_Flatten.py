import numpy

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

my_array = numpy.array(arr)


print(my_array.T)
print(my_array.flatten())
