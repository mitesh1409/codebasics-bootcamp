# Movie data analysis using pandas
import pandas as pd

def analyse_ratings(ratings: pd.Series) -> dict:
    return {
        "avg": ratings.mean(),
        "min": ratings.min(),
        "max": ratings.max()
    }

all_movies_df = pd.read_csv('movies.csv')
print(all_movies_df)
print('All movies rating analysis')
print(analyse_ratings(all_movies_df.imdb_rating))

bollywood_movies_df = all_movies_df[all_movies_df.industry == 'Bollywood']
print(bollywood_movies_df)
print('Bollywood movies rating analysis')
print(analyse_ratings(bollywood_movies_df.imdb_rating))

hollywood_movies_df = all_movies_df[all_movies_df.industry == 'Hollywood']
print(hollywood_movies_df)
print('Hollywood movies rating analysis')
print(analyse_ratings(hollywood_movies_df.imdb_rating))

# print('df')
# print(df)
# print('\n\n')

# print('df.head()')
# print(df.head())
# print('\n\n')

# print('df.tail()')
# print(df.tail())
# print('\n\n')

# print('df.sample()')
# print(df.sample())
# print('\n\n')

# print('df[2:6]')
# print(df[2:6])
# print('\n\n')

# print('df.shape')
# print(df.shape)
# print('\n\n')

# print('df.imdb_rating')
# print(df.imdb_rating)
# print(type(df.imdb_rating))
# print('\n\n')

# print("df['imdb_rating']")
# print(df['imdb_rating'])
# print(type(df['imdb_rating']))
# print('\n\n')

# print('df.imdb_rating.count()')
# print(df.imdb_rating.count())
# print('\n\n')

# print('df.imdb_rating.min()')
# print(df.imdb_rating.min())
# print('\n\n')

# print('df.imdb_rating.max()')
# print(df.imdb_rating.max())
# print('\n\n')

# print('df.imdb_rating.mean()')
# print(round(df.imdb_rating.mean(), 2))
# print('\n\n')
