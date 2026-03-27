import pandas as pd

df = pd.read_csv("movies.csv")

def printt(title, data, seperator="\n\n"):
    print(title)
    print(data)
    print(seperator)

# DataFrame
printt("df", df)

# pandas.DataFrame
printt("type(df)", type(df))

# Get shape of the DataFrame
printt("df.shape", df.shape)

# Get first 5 entries
printt("df.head()", df.head())

# Get first 2 entries
printt("df.head(2)", df.head(2))

# Get last 5 entries
printt("df.tail()", df.tail())

# Get last 2 entries
printt("df.tail(2)", df.tail(2))

# Get DataFrame columns
printt("df.columns", df.columns)

# df.industry.unique()
printt("df.industry.unique()", df.industry.unique())

# df.language.unique()
printt("df.language.unique()", df.language.unique())

# df.industry.value_counts()
# Get industry wise movies count.
printt("df.industry.value_counts()", df.industry.value_counts())

# df.language.value_counts()
# Get language wise movies count.
printt("df.language.value_counts()", df.language.value_counts())

# Get a subset (title, imdb_rating, industry) of columns from the DataFrame.
df_subset_1 = df[["title", "imdb_rating", "industry"]]
printt('df[["title", "imdb_rating", "industry"]]', df_subset_1)

# Get a subset of rows from the DataFrame.
df_subset_2 = df[(df.release_year >= 2000) & (df.release_year <= 2010)]
printt('df[(df.release_year >= 2000) & (df.release_year <= 2010)]', df_subset_2)

# Get movies from the Marvel Studios.
df_marvel_movies = df[df.studio == 'Marvel Studios']
printt("df[df.studio == 'Marvel Studios']", df_marvel_movies)

# Get quick stats.
df_quick_stats = df.describe()
printt("df.describe()", df_quick_stats)

# Get quick info.
print("df.info()")
df.info()

# Get a movie with max rating.
max_rating_movie = df[df.imdb_rating == df.imdb_rating.max()]
printt("Max rating movie", max_rating_movie)

# Get a movie with min rating.
min_rating_movie = df[df.imdb_rating == df.imdb_rating.min()]
printt("Min rating movie", min_rating_movie)

# Get both movies - max rating & min rating.
printt("Max & Min rating movies", df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])

# Add a new column in the DataFrame.
import datetime
current_year = datetime.date.today().year

df['age'] = df.release_year.apply(lambda year: current_year - year)
printt('df after adding "age" column', df)

# Add a new column in the DataFrame.
df['profit'] = df.revenue - df.budget
printt('df after adding "profit" column', df)

# DataFrame index
printt("df.index", df.index)

# Set movie title as an index of the DataFrame.
df.set_index("title", inplace=True)
printt("df after setting title as an index", df)
printt("df.index", df.index)

# Get a movie by its title (which is the new index now).
printt('RRR', df.loc['RRR'])

# Get multiple movies by its title.
printt('Movies by title', df.loc[['RRR', 'Interstellar']])

printt("df.iloc[0]", df.iloc[0])
printt("df.iloc[1]", df.iloc[1])
printt("df.iloc[0:5]", df.iloc[0:5])

# Reset index.
df.reset_index(inplace=True)
printt('df after resetting index', df)
