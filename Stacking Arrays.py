# Stacking Arrays
import numpy as np

array = np.arange(12).reshape(3,4)
print(array)
array = array + 1
print(array)

checkArray = array > 4
print(checkArray)