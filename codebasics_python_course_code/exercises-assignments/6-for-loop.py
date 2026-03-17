expenses = [100, 299, 300, 50, 499]
print(expenses)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

total_expenses = 0
for expense in expenses:
    total_expenses += expense

print(total_expenses)

for i in range(len(expenses)):
    print(f'{months[i]}: {expenses[i]}')

for key, value in enumerate(expenses):
    print(f'{key}: {value}')

monthly_sales = [25, 35, 45, 55, 50, 51, 60, 59, 53, 60]
sales_threshold = 50

for sales in monthly_sales:
    if sales < 50:
        print(f'Sales amount {sales} below sales threshold {sales_threshold}')

# Find a value and then exit out of the loop

bag_items = ['Mobile Phone', 'Goggles', 'Water Bottle', 'Napkin', 'Car Keys', 'Wallet', 'Movie Tickets']

if 'Movie Tickets' in bag_items:
    print('Found movie tickets')
else:
    print('Tickets not found')

for item in bag_items:
    if item == 'Water Bottle':
        print('Water Bottle found :)')
        break
    else:
        print('Water Bottle not found :(')

monthly_sales = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

sales_threshold = 50

for sales, month in zip(monthly_sales, months):
    print(f'Month: {month} Sales: {sales}')
    if sales < sales_threshold:
        print(f'Sales below threshold {sales_threshold}')
        break

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print odd numbers only
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

for number in numbers:
    if number % 2 != 0:
        print(number)

sum = 0
i = 0

while i < len(numbers):
    sum += numbers[i]
    i += 1

print(f'Sum: {sum}')

products = ['iPhone', 'iPad', 'MacBook']
regions = ['India', 'USA', 'China']
revenue = [10, 20, 30, 40, 50, 60, 70, 80, 90]

i = 0
for product in products:
    for region in regions:
        print(f'{product} {region} revenue = {revenue[i]}')
        i += 1

for i in range(10):
    print(i)
else:
    print('End of loop! Clean up done :)')

for i in range(4):
    print(i)

for i in range(2,10):
    if i % 5 == 0:
        break
    print(i)
