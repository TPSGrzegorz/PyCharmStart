import numpy as np
N = int(input())
A = np.array([input().split() for _ in range(N)],float)
result = np.linalg.det(A)
print(round(result,2))

