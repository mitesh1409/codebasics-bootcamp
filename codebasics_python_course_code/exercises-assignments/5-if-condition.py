number = input('Enter a whole number:')
print(number)
print(type(number))

number = int(input('Enter a whole number:'))
print(number)
print(type(number))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

number = 5
message = f'{number} is even' if number % 2 == 0 else f'{number} is odd'
print(message)

age = 12
is_adult = True if age >= 18 else False
if not is_adult:
    print('Entry denied! This movie is for the adults only')
else:
    print('Entry allowed')

age = 20
is_adult = True if age >= 18 else False
has_driving_license = True

if is_adult and has_driving_license:
    print('Can drive :)')
else:
    print('Cannot drive')

indian = ['Samosa', 'Daal', 'Naan']
chinese = ['Egg Role', 'Pot Sticker', 'Fried Rice']
italian = ['Pizza', 'Pasta', 'Risotto']

input_dish = input('Enter a dish:')

if input_dish in indian:
    print(f'{input_dish} is an Indian recipe')
elif input_dish in chinese:
    print(f'{input_dish} is a Chinese recipe')
elif input_dish in italian:
    print(f'{input_dish} is an Italian recipe')
else:
    print(f'{input_dish} is not Indian, Chinese or Italian recipe')

n = -5
message = "Negative" if n >= 0 else "Positive"
print(message)

age = 17
if age >= 30:
    print("Adult")
elif age > 18 and age < 30:
    print("Young adult")
else:
    print("Minor")
