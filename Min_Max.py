import numpy as np
n,m=map(int,input().split())
j=[]
for _ in range(n):
    k=list(map(int,input().split()))
    j.append(k)

n=sorted(np.min(j, axis = 1))
print(n[-1])
