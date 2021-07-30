from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    alan = "hello alan these is working now ."
    params = {
        'alan': alan
    }
    return render(request, 'home.html', params)