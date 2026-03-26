import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(len(numbers))
print(numbers[9])

print(numbers[0:3])

print(numbers[7:15]) # last index is 9 but it does not give index out of range error

print(numbers[-1])
print(numbers[-2])
print(numbers[-2:])

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Get 6 - 2nd row, 3rd column
print(numbers[1, 2])

# Get 7 - 3rd row, 1st column
print(numbers[2, 0])

# Get the last row
print(numbers[-1])

# Get the first 2 elements from the last row
print(numbers[-1, 0:2])

# Get the last element in the last row
print(numbers[-1, -1])

# Get all the rows one by one
print(numbers[0])
print(numbers[1])
print(numbers[2])

# Slicing rows
print(numbers[:0])
print(numbers[:1])
print(numbers[:2])

# Get all the columns one by one
print(numbers[:, 0])
print(numbers[:, 1])
print(numbers[:, 2])

# Get 2nd and 3rd columns
print(numbers[:, 1:3])

# Customer ID, Name
customers_one = np.array([
    [101, 'Mira'],
    [102, 'Abdul'],
    [103, 'Andrea']
])

# Customer ID, Purchase Amount, Purchase Date
customers_two = np.array([
    [101, 250.50, '2023-08-01'],
    [102, 150.00, '2023-08-02'],
    [103, 300.75, '2023-08-01'],
])

# Horizontal Stacking
combined_data = np.hstack((customers_one, customers_two))

print(combined_data)

customers_list_1 = np.array([
    [101, 'Mira'],
    [102, 'Abdul'],
    [103, 'Andrea']
])

customers_list_2 = np.array([
    [104, 'Shahid'],
    [105, 'Rehman'],
    [106, 'John']
])

# Vertical Stacking
combined_data = np.vstack((customers_list_1, customers_list_2))

print(combined_data)

# Horizontal Splitting

transactions = np.array([
    [101, 'Mohan', 250.50, '2023-08-01'],
    [102, 'Bob', 150.00, '2023-08-02'],
    [103, 'Fatima', 300.75, '2023-08-01'],
    [104, 'David', 400.20, '2023-08-03'],
    [105, 'Aryan', 330.1, '2023-08-04'],
])

print(np.hsplit(transactions, [3]))

print(np.hsplit(transactions, [2]))

# Vertical Splitting

print(np.vsplit(transactions, [4]))
print(np.vsplit(transactions, [2]))

# Filter monthly sales
monthly_sales = np.array([30, 33, 35, 28, 42])
target = 32
sales_below_target = monthly_sales < 32

print(sales_below_target)

print(monthly_sales[sales_below_target])

# Get the highest monthly sales
print(monthly_sales.max())
max_sales_index = np.argmax(monthly_sales)
print(max_sales_index)
print(monthly_sales[max_sales_index])

# Get the transaction with max amount
transactions = np.array([
    [101, 'Mohan', 250.50, '2023-08-01'],
    [102, 'Bob', 150.00, '2023-08-02'],
    [103, 'Fatima', 300.75, '2023-08-01'],
    [104, 'David', 400.20, '2023-08-03'],
    [105, 'Aryan', 330.1, '2023-08-04'],
])

transaction_column = transactions[:, 2].astype(float)

max_transaction_index = np.argmax(transaction_column)
print(max_transaction_index)
print(transactions[max_transaction_index])

# Get the transaction with id 105
transactions[transactions[:, 0].astype(int) == 105]


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:2, 1:])

print(arr[:2])
print(arr[:2, 1:])
