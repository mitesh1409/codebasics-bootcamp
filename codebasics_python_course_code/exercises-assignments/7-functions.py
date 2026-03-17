# The formula for calculating the future value of an SIP is:
#
# FV = p * (((1 + r)**t - 1) / r) * (1 + r)
# Where
# FV = Future value of your investment
# p = Monthly investment amount
# r = Expected annual return / 12
# n = Investment duration in months
#
# Example
# Say you want to invest ₹5,000 every month for the next 40 years, with a return expectation of 12%.
# Here’s a breakdown of how you can calculate the future value of your investment:
#
# Monthly investment (p) ₹5,000
# Investment duration (n) 40 years = 40 * 12 = 480 months
# Expected annual return (r) 12% = (12 / 100) / 12
#
# Plugging these values in the formula, your investment will grow to 5,94,12,101.

import math

def sip_calculator(p, r, t):
    """Calculates future value of the SIP investments.

    Args:
        p (float): SIP value per month
        r (float): Rate of return per year
        t (int): Investment duration in months

    Returns:
        int: Future values of the SIP investments
    """
    r = (r / 100) / 12
    future_value = p * (((1 + r)**t - 1) / r) * (1 + r)
    return future_value

print(round(sip_calculator(5000, 12, 480)))

def cylinder_volume(radius, height=10):
    """Calculates cylinder volume.

    Args:
        radius (float): Radius of the cylinder
        height (float): Height of the cylinder

    Returns:
        float: Volume of the cylinder
    """
    return round(math.pi * radius**2 * height, 2)

print(cylinder_volume(5, 10))
print(cylinder_volume(5))
print(cylinder_volume(10, 5))
print(cylinder_volume(height=10, radius=5))

# variadic positional parameter OR
# star argument OR
# arbitrary arguments
# *args = variable number of non-keyword arguments, they are stored into tuple by the function.
def sum_all(*nums):
    print(type(nums))
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30, 40, 50))

# Variable number of keyword arguments
# **kwargs = variable number of keyword arguments, they are stored into dictionary by the function.
def company_info(**params):
    print(type(params))
    print(params)
    for key in params:
        print(f'{key} - {params[key]}')

company_info(ticker='BAJAJHFL', ceo="Rahul Bajaj", market_cap=68417, pe=27.5, roce=9.55, rsi=27.2)

# One liner anonymous functions OR
# lambda function
# lambda arguments: expression
isAdult = lambda age: age > 18

print(isAdult(5))
print(isAdult(15))
print(isAdult(25))

# An empty function
# It can be used in interfaces to define a skeleton/structure.
def do_nothing():
    pass
