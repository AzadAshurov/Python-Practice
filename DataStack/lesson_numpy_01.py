import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers))
print(numbers.shape)
new_numbers = numbers * 3
matrix = np.array([
 [1,2,3],
 [4,5,6]
])

print(matrix[0]) 
print(matrix[0, 1])

print(numbers.dtype)
a = np.array([1, 2, 3])
b = np.array([1.5, 2.5, 3.5])
c = np.array([True, False, True])
print(a.dtype)
print(b.dtype)

print(c.dtype)
print(c)
d = np.array([1, 2, 3.5])
print(d.dtype)
print(d)
