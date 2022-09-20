import numpy as np
m,n=map(int,input().split())
matrix=[]
for _ in range(m):
    k=list(map(int,input().split()))
    matrix.append(k)
print(np.mean(matrix, axis = 1))

print(np.var(matrix, axis = 0))

k=np.std(matrix, axis = None)
print(k.round(11))