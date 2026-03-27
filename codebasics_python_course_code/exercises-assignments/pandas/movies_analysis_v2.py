# Movie data analysis using pandas

import pandas as pd

def analyse_ratings(ratings: pd.Series) -> dict:
    return {
        "avg": round(ratings.mean(), 2),
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

print('all_movies_df')
print(all_movies_df)
print('\n\n')

print('all_movies_df.head()')
print(all_movies_df.head())
print('\n\n')

print('all_movies_df.tail()')
print(all_movies_df.tail())
print('\n\n')

print('all_movies_df.sample()')
print(all_movies_df.sample())
print('\n\n')

print('all_movies_df[2:6]')
print(all_movies_df[2:6])
print('\n\n')

print('all_movies_df.shape')
print(all_movies_df.shape)
print('\n\n')

print('all_movies_df.imdb_rating')
print(all_movies_df.imdb_rating)
print(type(all_movies_df.imdb_rating))
print('\n\n')

print("all_movies_df['imdb_rating']")
print(all_movies_df['imdb_rating'])
print(type(all_movies_df['imdb_rating']))
print('\n\n')

print('all_movies_df.imdb_rating.count()')
print(all_movies_df.imdb_rating.count())
print('\n\n')

print('all_movies_df.imdb_rating.min()')
print(all_movies_df.imdb_rating.min())
print('\n\n')

print('all_movies_df.imdb_rating.max()')
print(all_movies_df.imdb_rating.max())
print('\n\n')

print('all_movies_df.imdb_rating.mean()')
print(round(all_movies_df.imdb_rating.mean(), 2))
print('\n\n')
