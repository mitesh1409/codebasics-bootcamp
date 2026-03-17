# Imagine you run a loyalty program where customers earn rewards based on the total amount they have spent. The rewards levels are defined based on the total purchase amount. Based on this scenario, complete the following tasks.

# Task 1
# 
# You are given a file called customers.txt that contains the name of the customer and total amount they spent.
# Read this file line by line and save the customer name and total amount in a dictionary.
# 
# For example, customers.txt file will content the data in the following format,
# 
# Srinivas,120
# John,250
# Maria,150
# Smith,510
# Anjali,45
# 
# You will read this and build a dictionary like this,
# 
# {
#     "Srinivas": 120,
#     "John": 250,
#     "Maria": 150,
#     "Smith": 510,
#     "Anjali": 45
# }

customers = {}
with open('customers.txt', 'r') as file_stream:
    for line in file_stream:
        customer_name, spent_amount = line.split(',')
        spent_amount = int(spent_amount.strip())
        customers[customer_name] = spent_amount

print(customers)

# Task 2
# 
# The rewards levels are defined below based on the total purchase amount.
# Using this define a function called calculate_rewards that takes total as input and returns the reward.
# 
# 1. Bronze: Total purchases $100-$199
# 2. Silver: Total purchases $200-$499
# 3. Gold: Total purchases $500+

def calculate_rewards(spent_amount):
    if spent_amount <= 199:
        return 'Bronze'
    if spent_amount <= 499:
        return 'Silver'
    return 'Gold'

# Task 3
# 
# Now for each of the customers in our customers_dict, calculate the rewards and build a customers_summary dictionary that looks like the following, (key is the name of the customer and the value is a tuple containing total amount and rewards level)
# 
# {
#    'Srinivas': (120, 'Bronze'),
#    'John': (250, 'Silver'),
#    'Maria': (150, 'Bronze'),
#    'Smith': (510, 'Gold'),
#    'Anjali': (45, 'None')
# }

customers_summary = {}
for customer_name, spent_amount in customers.items():
    customers_summary[customer_name] = (spent_amount, calculate_rewards(spent_amount))

print(customers_summary)

# Task 4
# 
# Now stitch all of the above code together and create a function that takes file name as input and returns the customer_summary dictionary.
# 
# def process_customer_data(file_name):
#     # return customer_summary dict

def calculate_rewards(spent_amount):
    if spent_amount <= 199:
        return 'Bronze'
    if spent_amount <= 499:
        return 'Silver'
    return 'Gold'

def process_customer_data(file_name):
    customers_summary = {}

    with open(file_name, 'r') as file_stream:
        for line in file_stream:
            customer_name, spent_amount = line.split(',')
            spent_amount = int(spent_amount.strip())
            customers_summary[customer_name] = (spent_amount, calculate_rewards(spent_amount))

    return customers_summary

customers_summary = process_customer_data('customers.txt')

print(customers_summary)
