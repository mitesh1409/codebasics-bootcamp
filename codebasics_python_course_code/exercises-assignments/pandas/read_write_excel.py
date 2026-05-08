import pandas as pd
from typing import Any

def printx(title: str, data: Any) -> None:
    """Prints data with a given title and seperator at the end.

    Args:
        title (str): Title of the data.
        data (Any): Data that you want to print.

    Returns:
        None: Returns None.
    """
    print(title)
    print(data)
    print('\n\n' + '*' * 50 + '\n\n')

# Read "movies" sheet from the movies_db.xlsx file.
df_movies = pd.read_excel("movies_db.xlsx", "movies")

printx('movies', df_movies)

# Read "actors" sheet from the movies_db.xlsx file.
df_actors = pd.read_excel("movies_db.xlsx", "actors")

printx('actors', df_actors)

# Read "financials" sheet from the movies_db.xlsx file.
df_financials = pd.read_excel("movies_db.xlsx", "financials")

printx('financials', df_financials)

# Standardize currency column.
def standardize_currency(currency: str) -> str:
    if currency == '$$' or currency == 'Dollars':
        return 'USD'
    return currency

df_financials = pd.read_excel("movies_db.xlsx", "financials", converters = {
    'currency': standardize_currency
})

printx('financials', df_financials)

# Merging two sheets on a related column.
df_movies_financials = pd.merge(df_movies, df_financials, on='movie_id')
printx('Movies with Financials', df_movies_financials)

# Save dataframe to an excel file.
df_movies_financials.to_excel("merged.xlsx", sheet_name="movies_and_financials", index=False)

# Create a dataframe from a dictionary.
df_stocks = pd.DataFrame({
    'tickers': ['WIPRO', 'HDFCBANK', 'RADICO'],
    'price': [100, 200, 300],
    'pe': [10, 20, 30],
    'eps': [5, 10, 15]
})
printx('Stocks', df_stocks)

df_weather = pd.DataFrame({
    'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
    'temperature': [32, 35, 28],
    'event': ['Rain', 'Sunny', 'Snow']
})
printx('Weather', df_weather)

with pd.ExcelWriter("stocks_weather.xlsx") as pd_excel_writer:
    df_stocks.to_excel(pd_excel_writer, sheet_name='stocks')
    df_weather.to_excel(pd_excel_writer, sheet_name='weather')
