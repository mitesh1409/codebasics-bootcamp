# Task #1
# Create a variable named pi and store the value 22/7 in it.
# Now check the data type of this variable.

pi = 22 / 7
print(pi)
type(pi)

# Task #2
# Create a variable called for and assign it a value 4.
# See what happens and find out the reason behind the behavior that you see.

for = 4

# Reason
# "for" is a reserved keyword in Python to write for loops. So you cannot use it to define variables.

# Task #3
# Below we have defined the variables for storing the principal amount, rate of interest and time.
# You need to calculate the simple interest for 3 years.
# Once simple interest is calculated, calculate the total amount you will have at the end of the tenure.

# Calculate the simple intrest using simple math formula:
# 
# simple interest  = P x R x T / 100
# 
# where:
# P = principle amount
# R = rate of interest
# T = time 

principle_amount = 567.00
rate_of_interest = 5.6
time = 3

simple_interest = principle_amount * rate_of_interest * time / 100

print(f'Simple interest = {simple_interest}')

total_amount = principle_amount + simple_interest

print(f'Total amount = {total_amount}')

# Task #4
# There is a circular pond in a village.
# This pond has a radius of 84 meter.
# Can you find the area of the pond?
# If there is a 2000 liter water in a square meter,
# what is the total amount of water in this pond?

import math

radius = 84
area = math.pi * radius * radius
print(f'Area of the pond: {area} square meters')

total_amount_of_water = 2000 * area
print(f'Total amount of water: {total_amount_of_water}')

# Task #5
# If you cross a 490-meter-long street in 7 minutes,
# then what is your speed in meter per seconds.
# Print your answer with only two decimal points.
# Hint:
# Speed = Distance / Time

distance = 490
time = 7 * 60
speed = distance / time
print(f'Speed = {round(speed, 2)} meters/secs')

# Task #6
# Create two variables to store how many fruits and vegetables you eat in a day.
# The value should be numeric for example 3 fruits and 4 vegetables.
# Now Print "I eat x vegetables and y fruits daily" where x and y presents vegetables and fruits that you eat every day.
# Use python f string for this.

fruits = 2
vegetables = 3
print(f'I eat {vegetables} vegetables and {fruits} fruits daily')

# Task #7
# Create a variable and store the string “The Himalayas are one of the youngest mountain range on the planet.”
# 1. Print ‘The Himalayas’ using slice operator
# 2. Print “mountain range” using negative index
# 3. Print “The Himalayas on the planet” using slice as well as f-string

himalayas = "The Himalayas are one of the youngest mountain ranges on the planet."

print(himalayas[0:13])
print(himalayas[-30:-15])
print(f'{himalayas[0:13]} {himalayas[-14:]}')

# Task #8
# You have created a string variable called string= ”There are 9 planets in the solar system”.
# After some time, you have realized that your sentence is incorrect and there are only 8 planets, now correct your sentence by replacing the incorrect words.

solar_planets = "There are 9 planets in the solar system"
solar_planets = solar_planets.replace('9', '8')
print(solar_planets)

# Task #9
# Imagine you are a shop owner tracking sales of three products throughout the day.
# At the end of the day, you want to calculate the total sales from these products.
# Product quantity and prices are given below.
# 
# Task: Write a program that:
# 
# 1. Calculates the total sales for each product.
# 2. Summarizes the total sales for the day.
# 3. Prints this summary in a formatted manner.
# 
# Expected Output:
# 
# Daily Sales Summary:
# - Product 1: Sold 15 units at $20.0 each, Total: $300.0
# - Product 2: Sold 10 units at $35.0 each, Total: $350.0
# - Product 3: Sold 20 units at $12.0 each, Total: $240.0
# Total Sales for the Day: $890.0

# Prices and quantities for each product
product1_price = 20.0  # Price per unit for product 1
product1_quantity = 15  # Quantity sold of product 1
total_sales_product1 = product1_price * product1_quantity

product2_price = 35.0  # Price per unit for product 2
product2_quantity = 10  # Quantity sold of product 2
total_sales_product2 = product2_price * product2_quantity

product3_price = 12.0  # Price per unit for product 3
product3_quantity = 20  # Quantity sold of product 3
total_sales_product3 = product3_price * product3_quantity

total_sales = total_sales_product1 + total_sales_product2 + total_sales_product3

daily_sales_summary = f'''
Daily Sales Summary:
- Product 1: Sold {product1_quantity} units at ${product1_price} each, Total: ${total_sales_product1}
- Product 2: Sold {product2_quantity} units at ${product2_price} each, Total: ${total_sales_product2}
- Product 3: Sold {product3_quantity} units at ${product3_price} each, Total: ${total_sales_product3}
Total Sales for the Day: ${total_sales}
'''

print(daily_sales_summary)

# Task #10
# Get help on str
help(str)
