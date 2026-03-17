first_name = 'Peter'
last_name = 'Parker'
full_name = first_name + ' ' + last_name
age = 20
print(full_name)
print(f'{first_name} {last_name}')

full_name = f'{first_name} {last_name}'
print(f'{full_name}, {age}')

print(full_name)
print(full_name[0])
print(full_name[1])
print(full_name[0:5])
print(full_name[6:])

print(full_name[-1])
print(full_name[-2])

len(full_name)
print(full_name[12])

# String objects are immutable
full_name[0] = 'X'

recipe = "Veg biryani with saffron, cardamom and cloves, garnished with fried onions and cilantro."
print(recipe)

# Handle long strings/text using '''
recipe = '''
Veg biryani with saffron, cardamom and
cloves, garnished with fried onions and
cilantro.
'''
print(recipe)

spice = 'cardamom'
spice in recipe

'cardamom' in recipe
'saffron' in recipe
'cloves' in recipe
'milk' in recipe

print(recipe.find('saffron'))

dir(str)

bill_description = 'Patient was charged $100 for the lab tests.'
print(bill_description)
bill_description = bill_description.replace('100', '50')
print(bill_description)
print(bill_description.index('50'))
print(bill_description.index('90'))

print(full_name)
print(full_name.upper())
print(full_name.lower())

print('499.5'.isdigit())
print('499.5'.isdecimal())
print('499.5'.isnumeric())

print('99'.isdigit())

some_text = 'My age is:'
age = 45
print(some_text + age)
print(f'{some_text} {age}')
print(some_text + str(age))

hello = 'hello\t:)'
print(hello)

stock_tickers = 'TCS|RELIANCE|HDFCBANK|TATAPOWER'
print(stock_tickers.split('|'))
print(stock_tickers.split('|', maxsplit=2))

some_text = '    Hello! How are you?    '
print(f'*{some_text}*')
print(f'*{some_text.lstrip()}*')
print(f'*{some_text.rstrip()}*')
print(f'*{some_text.strip()}*')

file_name = 'report_2024-25.pdf'
file_name.endswith('.pdf')
file_name.startswith('report')
file_name.startswith('xyz')
