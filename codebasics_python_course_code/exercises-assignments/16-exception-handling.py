# Exception handling example

import traceback

dividend = 103
divisor = 4
quotient = None
remainder = None

try:
    quotient = int(dividend / divisor)
    remainder = dividend % divisor
    text = 'baby yoda' + 56
except ZeroDivisionError as e:
    print('Got an error:', e)
    traceback.print_exc()
except TypeError as e:
    print('Got an error:', e)
    traceback.print_exc()
except Exception as e:
    print('Got an error:', e)
    traceback.print_exc()
finally:
    # Do clean-up operations
    print('Finally...')

print(f'Quotient of {dividend} / {divisor} = {quotient}')
print(f'Remainder of {dividend} / {divisor} = {remainder}')
