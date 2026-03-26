import numpy as np

q1_revenue = np.array([1, 2, 3])
q2_revenue = np.array([4, 5, 6])
q3_revenue = np.array([7, 8, 9])
q4_revenue = np.array([10, 11, 12])

print(q1_revenue)
print(q2_revenue)
print(q3_revenue)
print(q4_revenue)

print(q1_revenue.ndim)

annual_revenue = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])

print(annual_revenue.ndim)

print(annual_revenue)
print(annual_revenue.ndim)
print(annual_revenue.dtype)

annual_revenue = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
], dtype=np.float64)

print(annual_revenue.dtype)

# Size of an item
print(annual_revenue.itemsize)

# Total number of items
print(annual_revenue.size)

# Shape of the numpy array - (rows, columns)
print(annual_revenue.shape)

# Sorting
annual_revenue = np.array([
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7],
    [12, 11, 10],
], dtype=np.float64)

np.sort(annual_revenue)
np.sort(annual_revenue, axis=None)
print(annual_revenue)

np.zeros((2, 3))

np.zeros((3, 4)).shape

np.ones((3, 5))

np.arange(10, 20)

# Odd numbers between 1 to 100
np.arange(1, 101, 2)

# Even numbers between 1 to 100
np.arange(2, 101, 2)

# Linearly spaced elements
np.linspace(1, 100, 5)
np.linspace(1, 100, 10)
np.linspace(1, 100, 20)
np.linspace(1, 100, 50)

annual_revenue = np.array([
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7],
    [12, 11, 10],
], dtype=np.float64)

print(annual_revenue.ravel())
print(annual_revenue)

print(annual_revenue.flatten())
print(annual_revenue)

# Reshape
annual_revenue = np.array([
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7],
    [12, 11, 10],
], dtype=np.float64)

print(annual_revenue.reshape(12, 1))
print(annual_revenue.reshape(6, 2))
print(annual_revenue.reshape(4, 3))
print(annual_revenue)

# min value
print(annual_revenue.min())

# max value
print(annual_revenue.max())

annual_revenue = np.array([
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7],
    [12, 11, 10],
], dtype=np.float64)

# Get the sum of row values
print(annual_revenue.sum(axis=1))

# Get the sum of column values
print(annual_revenue.sum(axis=0))

for row in annual_revenue:
    print('Row', row)

numpy_array = np.array([1, 4, 9, 16, 25])
np.sqrt(numpy_array)

numbers = [1, 2, 3, 4, 5]
np.square(numbers)

np.std(numbers)
