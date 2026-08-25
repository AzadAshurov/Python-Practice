import numpy as np
numbers = np.arange(24)

print(numbers)
print(numbers.shape)
numbers = numbers.reshape(4, 6)
print(numbers)
print(numbers.shape)
print(numbers[0])
print(numbers[-1,-1])
matrix = np.ones((3, 3))
print(matrix)
matrix_new = np.zeros((2, 5))
print(matrix_new)   
