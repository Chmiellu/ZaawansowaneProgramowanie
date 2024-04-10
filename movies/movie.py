import os
import csv


class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres


def load_movies_from_csv(file_path):
    movies = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = Movie(row["movieId"], row["title"], row["genres"])
            movies.append(movie)
    return movies


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "movies.csv")

movies_list = load_movies_from_csv(file_path)
