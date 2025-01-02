import numpy as np
import time
l1=range(1,100000)
l2=range(1,100000)

A1 = np.array(l1)
A2 = np.array(l2)

start= time.time()
result1 = [x+y for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start = time.time()
result2 = A1+A2
print((time.time()-start)*1000)
