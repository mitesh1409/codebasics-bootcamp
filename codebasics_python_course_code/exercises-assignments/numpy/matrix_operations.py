import numpy as np

# Sales data for Quater 1 (Matrix 1)
# Row represent different products, columns represent different regions

q1 = np.array([
    [200, 220, 250], # Product A
    [150, 180, 210], # Product B
    [300, 330, 360], # Product C
])

q2 = np.array([
    [209, 231, 259], # Product A
    [155, 192, 222], # Product B
    [310, 340, 375], # Product C
])

print(f'''
Quarter #1
{q1}
''')
print(f'''
Quarter #2
{q2}
''')

# Combine sales of Quarter 1 and Quarter 2
q1_and_q2 = q1 + q2

print(f'''
Quarter 1 & Quarter 2 Combined
{q1_and_q2}
''')

# Quarter2 absolute growth
q2_abs_growth = q2 - q1

print(f'''
Quarter 2 Absolute Growth
{q2_abs_growth}
''')

# Quarter2 percentage growth
q2_percentage_growth = ((q2 - q1)/q1) * 100

print(f'''
Quarter 2 Percentage Growth
{q2_percentage_growth.round(2)}
''')

# Calculate revenue from prices and units data for Quarter 1.

prices_q1 = np.array([
    [10, 12, 11], # Product A
    [8, 9, 10], # Product B
    [15, 16, 17], # Product C
])

units_q1 = np.array([
    [200, 220, 250], # Product A
    [150, 180, 210], # Product B
    [300, 330, 360], # Product C
])

revenue_q1 = units_q1 * prices_q1

print(f'''
Revenue Q1
{revenue_q1}
''')

# Calculate 20% discount data on revenue for Quarter 1.
discount_q1 = revenue_q1 * 0.2

print(f'''
Discount Q1
{discount_q1}
''')

net_revenue_q1 = revenue_q1 - discount_q1

print(f'''
Net Revenue Q1
{net_revenue_q1}
''')

# Calculate total revenue for Quarter 1.

print(f'''
Total Revenue
{np.sum(revenue_q1)}
''')

# Dot product example

# Real estate houses data with features (area in square foot, # of bedrooms)
houses = np.array([
    [2000, 3], # 2000 square foots, 3 bed rooms
    [1800, 2]  # 1800 square foots, 2 bed rooms
])
weights = np.array([150, 50000])

housing_prices = np.dot(houses, weights)

print(f'''
Housing Prices
{housing_prices}
''')

# Cross product example

one = np.array([1, 2, 3])
two = np.array([4, 5, 6])

cross_product = np.cross(one, two)

print(f'''
Cross Product of {one} & {two}
{cross_product}
''')
