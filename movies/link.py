import os
import csv


class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


def load_links_from_csv(file_path):
    links = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            link = Link(row["movieId"], row["imdbId"], row["tmdbId"])
            links.append(link)
    return links


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "links.csv")

links_list = load_links_from_csv(file_path)
