import numpy as np
import sys

numbers = np.array([1, 2, 3])
print('numpy array', numbers)

numbers_list = [1, 2, 3]
print('Python list', numbers_list)

# Create a list of 100 numbers
python_list = list(range(100))
print(python_list)

python_list_size = sys.getsizeof(python_list) + sum(sys.getsizeof(i) for i in python_list)
print(f'Python list size: {python_list_size}')

# Create a numpy array of 100 numbers
numpy_array = np.arange(100)
print(numpy_array)

print(f'numpy array size: {numpy_array.nbytes}')

# This clearly shows why numpy is preferred for large numerical data — it's significantly more memory efficient than a Python list!

# Python list vs numpy array
import time

ten_millions = 10_0_00_000
print(ten_millions)

list1 = list(range(ten_millions))
list2 = list(range(ten_millions))

start_time = time.time()
list3 = [x + y for x, y in zip(list1, list2)]
end_time = time.time()

print(f'Python list took {end_time - start_time}')

numpy_array1 = np.array(range(ten_millions))
numpy_array2 = np.array(range(ten_millions))

start_time = time.time()
numpy_array3 = numpy_array1 + numpy_array2
end_time = time.time()

print(f'Numpy array took {end_time - start_time}')

# numpy allows to do simple arithmatic operations
python_list1 = list(range(5))
python_list2 = list(range(5))
python_list3 = [x + y for x, y in zip(python_list1, python_list2)]
print(python_list3)

numpy_array1 = np.arange(5)
numpy_array2 = np.arange(5)

numpy_array3 = numpy_array1 + numpy_array2
print(numpy_array3)

numpy_array3 = numpy_array1 - numpy_array2
print(numpy_array3)

numpy_array3 = numpy_array1 * numpy_array2
print(numpy_array3)

numpy_array3 = numpy_array1 / numpy_array2
print(numpy_array3)

np.arange(10)
