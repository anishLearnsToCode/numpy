import numpy as np

array = np.array([[1, 2, 3], [3, 4, 5]])

for row in array:
    for column in row:
        print(column)

for element in array.ravel():
    print(element)

