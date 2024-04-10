from django.urls import path

from .views import (
    home_page_view,
    test_view,
    movie_list,
    link_list,
    rating_list,
    tag_list,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("test/", test_view, name="test"),
    path("movies/", movie_list, name="movie-list"),
    path("links/", link_list, name="link-list"),
    path("ratings/", rating_list, name="rating-list"),
    path("tags/", tag_list, name="tag-list"),
]
