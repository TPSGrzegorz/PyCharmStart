from itertools import product

A: list = list(map(int, input().split()))
B: list = list(map(int, input().split()))

cartesian_product = product(A, B)
print(*cartesian_product)
