from django.urls import path
from . import views


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.shows, name='shows'),
    path('bio/<int:id>', views.biography, name='biography'),
    path('discover-shows', views.discover ,name='discover'),
    path('whenplay', views.whenplay, name='whenplay'),

]
'''
browse
about
cats  - kids, drema and others stuffs
explore
tranding
according to the time
search

'''
