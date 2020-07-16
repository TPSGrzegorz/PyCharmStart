import numpy as np

N, M, P = list(map(int, input().split()))
result = np.array(list(map(int, input().split())))
for i in range(M + N - 1):
    result = np.concatenate((result, np.array(list(map(int, input().split())))), axis=0)

print(result.reshape((N + M), P))
