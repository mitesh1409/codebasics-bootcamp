# Task 1
# You are a Marvel fan and created a list of superheroes.
# Using this list, calculate how many members in the Avengers team?

avengers = [
    'Iron Man',
    'Captain America',
    'Black Widow',
    'Hulk',
    'Thor',
    'Hawkeye'
]

print(f'Avengers team has {len(avengers)} members')

# Task 2
# Awesome. Now Iron Man made Spider-Man a new member of the Avengers,
# add him to your list at the end.

avengers = [
    'Iron Man',
    'Captain America',
    'Black Widow',
    'Hulk',
    'Thor',
    'Hawkeye'
]

avengers.append('Spider-Man')

print(avengers)

# Task 3
# Looks like you are loving this avengers exercise already😄.
# Let's add a twist to it. Everyone came to a conclusion that Captain America is the leader of the Avengers,
# so please add him before the Iron Man.
# Hint: You can first remove him from the list and add before the Iron Man.
# To remove him you can use a method called .pop()
# 💡 Feel free to take help of ChatGPT just in case you are confused about pop() method.
# Remember becoming a good Python programmer is all about how well you can learn new things on your own.

avengers = [
    'Iron Man',
    'Captain America',
    'Black Widow',
    'Hulk',
    'Thor',
    'Hawkeye',
    'Spider-Man'
]

removed_item = avengers.pop(1)
avengers.insert(0, removed_item)
print(avengers)

# Task 4
# Thor and Hulk are getting angry easily and fight with each other.
# So you have to separate them with each other.
# To separate them, move “Black Widow” in between them.

avengers = [
    'Iron Man',
    'Captain America',
    'Black Widow',
    'Hulk',
    'Thor',
    'Hawkeye',
    'Spider-Man'
]

removed_item = avengers.pop(2)
avengers.insert(3, removed_item)
print(avengers)

# Task 5
# Below list contains scores of students in a class as per their roll number.
# Which means the first element is for roll #1, second one is for roll #2 and so on.
# Print the scores of,
# 1. The first student
# 2. The last student
# 3. First 3 students
# 4. Scores of roll #3, #4 and #5

scores = [92, 85, 76, 58, 89, 91, 73, 84]

# Score of the first student
print(scores[0])

# Score of the last student
print(scores[-1])

# Scores of the first 3 students
print(scores[0:3])

# Scores of roll #3, #4 and #5
print(scores[2:5])

# Task 6
# We got a result of one more student which is 83 marks.
# Append this to the "scores" at the end and print the list.

scores.append(83)
print(scores)

# Task 7
# Categorizes each score into a grade based on the following thresholds:
#
# 1. A: 90 to 100
# 2. B: 80 to 89
# 3. C: 70 to 79
# 4. D: 60 to 69
# 5. F: Below 60
#
# Count the number of students in each grade category and print the summary of how many students received each grade.
#
# Expected output
# 
# Grade Summary:
# - A: 2 students
# - B: 4 students
# - C: 2 students
# - D: 0 students
# - F: 1 students

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_f = 0

for score in scores:
    if score >= 90:
        grade_a += 1
    elif score >= 80:
        grade_b += 1
    elif score >= 70:
        grade_c += 1
    elif score >= 60:
        grade_d += 1
    else:
        grade_f += 1

grade_summary = f'''
Grade Summary:
- A: {grade_a} students
- B: {grade_b} students
- C: {grade_c} students
- D: {grade_d} students
- F: {grade_f} students
'''
print(grade_summary)

# Task 8
# ### Task 8
#
# Managing inventory efficiently is crucial for businesses to ensure they do not run out of key products.
# This exercise simulates a simple inventory management system where the user can see which items are below the minimum stock level and need reordering.
# Below you have two lists that stores product names and their inventory stock levels.
# Using that,
# 1. Check each item to see if its stock level is below a minimum threshold.
# 2. If the stock level is below the minimum, add the product's name to a reorder list.
# 3. Print a list of products that need to be reordered.
#
# Expected Output
#
# Items to Reorder:
# - Pears
# - Grapes

# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering

reorder_list = []

for product, stock in zip(product_names, stock_levels):
    if stock < minimum_stock:
        reorder_list.append(product)

reorder_summary = 'Items to Reorder:\n'
for item in reorder_list:
    reorder_summary += f'- {item}\n'

print(reorder_summary)
