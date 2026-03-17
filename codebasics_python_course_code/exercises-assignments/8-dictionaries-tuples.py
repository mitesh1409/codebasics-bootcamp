point_2d = (10, 20)
print(point_2d)
type(point_2d)

help(tuple)

point_3d = (10, 20, 30)
print(point_3d)

point_2d[0]
point_2d[1]
point_2d[2]

# tuples are immutable
point_2d[0] = 11

def lat_long(location_name):
    # find latitude and longitude for the given location.
    lat = '23.0225° N'
    long = '72.5714° E'
    return (lat, long)

latitude, longitude = lat_long('Ahmedabad, Gujarat, India')

print(f'{latitude}, {longitude}')

# Contacts list using tuples
contacts = [
    ('Mitesh', '8490873425'),
    ('Gautam', '9988776655'),
    ('Chintan', '1234567890')
]

# Get contact of Chintan
for contact in contacts:
    if contact[0] == 'Chintan':
        print(contact[1])

# What if there are millions of records in the contacts list.
# Using this approach is not a good idea. It is not efficient.
# O(n) or Linear time complexity

# To solve this problem we can use dictionaries in Python.
# O(1) Time complexity for look up by key
# O(1) Time complexity for insertion/deletion
# Dictionary is implemented using Hash Map data structure.

contacts = {
    'Mitesh': '8490873425',
    'Gautam': '9988776655',
    'Chintan': '1234567890'
}

print(contacts['Chintan'])
print(contacts['Gautam'])
print(contacts['Parth'])
print(contacts.get('Parth'))

# Dictionaries are mutable.
contacts['Gautam'] = '1212343456'

print(contacts)

contacts['Siddharaj'] = '9876543210'

print(contacts)

del contacts['Siddharaj']

print(contacts)

'Gautam' in contacts

'Kaushal' in contacts

contacts = {
    'Mitesh': {
        'Phone': '8490873425',
        'Email': 'mitesh5.mprajapati@gmail.com',
        'Address': 'Mitesh Address'
    },
    'Gautam': {
        'Phone': '9876543210',
        'Email': 'gautam.patel@gmail.com',
        'Address': 'Gautam Address'
    },
    'Chintan': {
        'Phone': '1234567890',
        'Email': 'chintan.patel@gmail.com',
        'Address': 'Chintan Address'
    }
}

print(contacts['Chintan'])
print(contacts['Chintan']['Phone'])
print(contacts['Chintan']['Email'])
print(contacts['Chintan']['Address'])

contacts.keys()
contacts.values()

for key, value in contacts.items():
    print(f'Key: {key}')
    print(f'Value: {value}')

# Apple revenues data
apple_revenues = {
    'India': {
        'iPhone': 10,
        'iPad': 20,
        'MacBook': 30
    },
    'USA': {
        'iPhone': 40,
        'iPad': 50,
        'MacBook': 60
    },
    'China' : {
        'iPhone': 70,
        'iPad': 80,
        'MacBook': 90
    }
}

for country, revenue_data in apple_revenues.items():
    for product, revenue in revenue_data.items():
        print(f'{country} {product} revenue: {revenue} millions USD per year')

type(apple_revenues)

help(dict)

dir(dict)
