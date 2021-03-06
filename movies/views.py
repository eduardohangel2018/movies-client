from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from .services import get_movies_and_persons


def movie_list(request):
    movies = cache.get('movies')
    if not movies:
        movies = get_movies_and_persons(
                films_endpoint=settings.FILMS_ENDPOINT,
                people_endpoint=settings.PEOPLE_ENDPOINT,
            )
        cache.set('movies', movies)
    return render(request, 'movies.html', {'movies': movies})
