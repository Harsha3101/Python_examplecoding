import numpy as np

lists=list(map(float,input().split()))

array = np.array(lists)
np.set_printoptions(legacy='1.13')
print (np.floor(array))
print (np.ceil(array))
print (np.rint(array))
