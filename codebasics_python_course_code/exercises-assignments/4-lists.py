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
