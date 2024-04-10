import os
import csv


class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp


def load_tags_from_csv(file_path):
    tags = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag = Tag(row["userId"], row["movieId"], row["tag"], row["timestamp"])
            tags.append(tag)
    return tags


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "tags.csv")

tags_list = load_tags_from_csv(file_path)
