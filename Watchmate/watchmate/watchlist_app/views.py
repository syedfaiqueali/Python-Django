'''from django.shortcuts import render
from django.http import JsonResponse

from watchlist_app.models import Movie


# Create your views here.
def movie_list(request):
    #1- To get all available obj from dB
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
        }

    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
        }
    return JsonResponse(data)
'''
