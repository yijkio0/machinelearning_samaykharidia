import numpy as np 
a=np.arange(1,10)
a=a.reshape((3,3))
a[1]=a[1]*2
print(a)