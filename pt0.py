import numpy as np

data=np.loadtxt("inferences.txt",dtype=np.float64)

xcoord=np.array(data[:,0])
print(xcoord)