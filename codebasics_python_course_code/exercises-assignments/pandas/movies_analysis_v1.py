# Movie data analysis using Python only

import csv

def rating_stats(ratings):
    return {
        "avg": round(sum(ratings) / len(ratings), 2),
        "min": min(ratings),
        "max": max(ratings)
    }

def analyse_ratings(movies_data_file):
    all_movies_ratings = []
    bollywood_movies_ratings = []
    hollywood_movies_ratings = []

    with open(movies_data_file, newline="", encoding="utf-8") as data_file:
        reader = csv.DictReader(data_file)

        for movie in reader:
            if movie['imdb_rating'] == 'NULL':
                continue

            rating = float(movie['imdb_rating'])

            all_movies_ratings.append(rating)

            bollywood_movies_ratings.append(rating) if movie['industry'].lower() == 'bollywood' else hollywood_movies_ratings.append(rating)

    return {
        "all": rating_stats(all_movies_ratings),
        "bollywood": rating_stats(bollywood_movies_ratings),
        "hollywood": rating_stats(hollywood_movies_ratings)
    }

movies_ratings = analyse_ratings('movies.csv')
print(movies_ratings)
