from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path("",views.index, name="Home"),
    path("index",views.index, name="index"),
    path("destination", views.offers, name="offers"),
    path('search', SearchResultsView.as_view(), name='search_results'),
    #path('index', HomePageView.as_view(), name='home'),
]
