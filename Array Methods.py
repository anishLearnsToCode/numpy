import numpy as np

array = np.array([1, 2])
print(array.ndim)

array2 = np.array([[1,2], [3, 10]])
print(array2.ndim)
print(array2.shape)

list = range(5)
npRangeArray = np.arange(0,5)
print(npRangeArray)

npRangeArray = np.arange(0,5,2)
print(npRangeArray)

# Linearly spaced numbers
npLinSpace = np.linspace(0, 10, 5)
print(npLinSpace)

# Reshaping an array
array = np.array([[1, 2, 3], [1, 3, 4], [1, 5, 6]])
print(array)
print(array.shape)
val = array.reshape(1,9)
print(val)

# Ravel (Flatten) an array
flatArray = array.ravel()
print(flatArray)

# Sum functions and minMax
print(array.sum())
print(array.sum(axis=0))
print(array.sum(axis=1))