items = ['fruits', 'vegetables', 'milk', 'ghee', 'curd']
print(items)
len(items)

items[0]
items[1]
items[2]
items[3]
items[4]
items[5]
items[-1]

items[0:2]
items[3:]

# Clear the list, remove all the elements.
# items.clear()
# print(items)

items.append('bread')
print(items)

items.remove('butter')
print(items)

items.remove('bread')
print(items)

items.insert(1, 'bread')
print(items)

# List is mutable, we can change one or more items.
items[1] = 'maggie'
print(items)

items[3:] = ['honey']
print(items)

'rice' in items

'honey' in items

expenses = [10, 50, 20, 40, 30]
print(expenses)

expenses.sort()
print(expenses)

expenses.sort(reverse=True)
print(expenses)

grocery_items = ['milk', 'curd', 'ghee', 'honey', 'fruits', 'vegetables']
stationery_items = ['pen', 'pencil', 'sharpener', 'eraser', 'notebook']
all_items = grocery_items + stationery_items
print(all_items)
len(all_items)

type(all_items)

dir(list)

help(list)

# Lists in Python need not to be homogeneous,
# they can be heterogeneous.
import math
random_items = ['War Machine', 50, 'Apple', math.pi, [1, 2, 4, 8]]
print(random_items)

animals = ["cat", "dog", "rabbit", "wolf"]
animals.remove("lion")

prices = [300, 50, 1200, 10]
# This does not modify the original list,
# but it sorts and returns a new list.
sorted(prices)
print(prices)
print(prices[2])

# This modifies the original list.
prices.sort()
print(prices)

office_supplies = ["pen", "paper", "stapler"]
kitchen_supplies = ["fork", "knife", "spoon"]
combined_list =  kitchen_supplies + office_supplies
print(combined_list[2: 4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
numbers[-4:]
numbers[10] = 11 # index out of range
numbers.append(11)
numbers.insert(10, 11)
print(numbers)


x = [1, 2, 3]

y = list(x)
# OR
# y = x[:]

print(x)
print(y)

x[1] = 99

print(x)
print(y)

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = list(x)

print(x)
print(y)

x[1][1] = 50


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

del numbers[4:6]
print(numbers)


areas_ext = [
    "hallway", 11.25,
    "kitchen", 18.0,
    "living room", 20.0,
    "bedroom", 10.75,
    "bathroom", 10.50,
    "poolhouse", 24.5,
    "garage", 15.45
]
print(areas_ext)

del areas_ext[-4]
del areas_ext[-3]

print(areas_ext)
