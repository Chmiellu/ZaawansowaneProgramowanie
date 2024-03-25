import requests
import argparse


class Brewery:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.brewery_type = data["brewery_type"]
        self.street = data["street"] if "street" in data else None
        self.city = data["city"]
        self.state = data["state"]
        self.country = data["country"]
        self.phone = data["phone"] if "phone" in data else None
        self.website_url = data["website_url"] if "website_url" in data else None

    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.city}, {self.state}, {self.country}\nWebsite: {self.website_url}\n"


def fetch_breweries(city=None):
    url = "https://api.openbrewerydb.org/breweries"
    if city:
        url += f"?by_city={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[:20]
        return [Brewery(item) for item in data]
    else:
        print("Failed to fetch data from the API.")
        return []
