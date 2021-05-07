import requests
from django.conf import settings


def merge_people_movie(all_films, all_people):

    film_people = {}

    for people in all_people:
        films = people['films']
        for film in films:
            film_id = film.split(settings.FILMS_ENDPOINT)[1]
            if film_id in film_people.keys():
                film_people[film_id].append(people)
            else:
                film_people[film_id] = [people]

    for film in all_films:
        people = film_people.get(film['id'])
        film['people'] = people

    return all_films


def get_movies_and_persons(*, films_endpoint, people_endpoint):

    all_films = requests.get(films_endpoint).json()
    all_people = requests.get(people_endpoint).json()

    return merge_people_movie(all_films, all_people)


def only_movies(all_films):

    # film_people = {}
    all_films = {}

    for film in all_films:
        film_id = film.split(settings.FILMS_ENDPOINT)[1]
        if film_id in all_films.keys():
            all_films[film_id].append(film)
        else:
            print('Error')

    for film in all_films:
        all_films = all_films.get(film['id'])
        film['all_films'] = film
        

    return all_films


def get_movies(films_endpoint):

    all_films = requests.get(films_endpoint).json()

    return only_movies(all_films)
