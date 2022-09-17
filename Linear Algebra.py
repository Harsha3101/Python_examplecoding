import numpy as np

k = int(input())
matrix = []
for _ in range(k):
    m = list(map(float, input().split()))
    matrix.append(m)

print(np.linalg.det(matrix).round(2))