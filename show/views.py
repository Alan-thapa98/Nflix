from django.shortcuts import render, redirect
# Create your views here.
from .models import *

def base(request):
    movie= flix.objects.all()
    context={'movie':movie,}
    return render(request,'base.html',context)

def shows(request):
    movie = flix.objects.all()
    params = {
        'movie': movie
    }
    return render(request, 'shows.html', params)


# these is for the movie or the webseriest all list and the description and others stuffes for the better informations
def biography(request, id):
    movies = flix.objects.filter(id=id).first()
    movies.views = movies.views + 1
    movies.save()
    params={movies:movies}
    return render(request, 'bio.html', params)

# when watching the videos for the entertainment


def whenplay(request):
    play = 'lets enjoy the show sell we '
    params = {'play': play}
    return render(request, 'whenplay.html', params)

def discover(request):

    return render(request,'discover.html')

def profile(request):
    
    return render(request,'proflie.html')
