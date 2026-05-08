import pandas as pd
from typing import Any

def printx(title: str, data: Any, separator: str='\n\n') -> None:
    print(title)
    print(data)
    print(separator)

# Reading everything
df = pd.read_csv('stock_data.csv')
printx('df', df)

# Skip the first row
df = pd.read_csv('stock_data.csv', skiprows=1)
printx('df', df)

# Reading with options like - header, column names, NA values etc.
df = pd.read_csv(
    'stock_data.csv', # File path
    header=1, # header at 2nd row
    names=['Symbol', 'EPS', 'Revenue', 'Price', 'People'], # Change column names
    # nrows=2 # Get the limited number of rows
    na_values={
        'EPS': ['not available'],
        'Revenue': [-1],
        'Price': ['n.a.'],
        'People': ['n.a.']
    }
)
printx('df', df)

# Specifying common na_values for all the columns
df = pd.read_csv(
    "stock_data.csv",
    header=1,
    na_values=['not available', -1, 'n.a.']
)
printx("df", df)

# Add a new column pe, derived from price/eps.
df = pd.read_csv(
    "stock_data.csv",
    header=1,
    na_values=['not available', -1, 'n.a.']
)
df['pe'] = round(df['price'] / df['eps'], 2)
printx("df", df)

# Creating a CSV file from the DataFrame.
df.to_csv('output.csv')

# Don't want an index column.
# df.to_csv('output.csv', index=False)

# Don't want the header.
# df.to_csv("output.csv", index=False, header=False)
