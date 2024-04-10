import os
import csv


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp


def load_ratings_from_csv(file_path):
    ratings = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating = Rating(
                row["userId"], row["movieId"], row["rating"], row["timestamp"]
            )
            ratings.append(rating)
    return ratings


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ratings.csv")

ratings_list = load_ratings_from_csv(file_path)
