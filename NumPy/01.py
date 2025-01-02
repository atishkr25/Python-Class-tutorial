# import numpy
# print(numpy.__version__)
import numpy as np
x=np.ones((5,5),dtype=int)
print(x)
print("-----------------------------------------------")

import sys
l = [1,2,3,4,5,6,7,8,9]
print(sys.getsizeof(2)*len(l))
print("\n")
arr=np.array(l)
print(arr.size*arr.itemsize)