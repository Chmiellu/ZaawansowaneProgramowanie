from django.http import HttpResponse
from django.http import JsonResponse
from movies.link import links_list
from movies.movie import movies_list
from movies.rating import ratings_list
from movies.tag import tags_list


def home_page_view(request):
    return HttpResponse("Hello, World!")


def test_view(request):
    return HttpResponse("This is the test endpoint.")


def movie_list(request):
    if request.method == "GET":
        serialized_movies = [
            {"movieId": movie.movie_id, "title": movie.title, "genres": movie.genres}
            for movie in movies_list
        ]
        return JsonResponse(serialized_movies, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def link_list(request):
    if request.method == "GET":
        serialized_links = [
            {"movieId": link.movie_id, "imdbId": link.imdb_id, "tmdbId": link.tmdb_id}
            for link in links_list
        ]
        return JsonResponse(serialized_links, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def rating_list(request):
    if request.method == "GET":
        serialized_ratings = [
            {
                "userId": rating.user_id,
                "movieId": rating.movie_id,
                "rating": rating.rating,
                "timestamp": rating.timestamp,
            }
            for rating in ratings_list
        ]
        return JsonResponse(serialized_ratings, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def tag_list(request):
    if request.method == "GET":
        serialized_tags = [
            {
                "userId": tag.user_id,
                "movieId": tag.movie_id,
                "tag": tag.tag,
                "timestamp": tag.timestamp,
            }
            for tag in tags_list
        ]
        return JsonResponse(serialized_tags, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
