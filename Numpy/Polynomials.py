import numpy as np
coefficients = list(map(float, input().split()))
n = float(input())
result = np.polyval(coefficients,n)
print(result)
