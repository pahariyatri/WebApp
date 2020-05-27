from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("",views.index, name="Home"),
    path("index",views.index, name="index"),
    path("destination", views.offers, name="offers"),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('adventure', views.adventure, name='adventure'),

    path('solo', views.solo, name='solo'),
    path('group', views.group, name='group'),
    path('religous', views.religous, name='religous'),
    path('wateractivities', views.wateractivities, name='wateractivities'),
    path('nature', views.nature, name='nature'),
    path('family', views.family, name='family'),
    path('romantic', views.romantic, name='romantic')

    #path('index', HomePageView.as_view(), name='home'),
]
