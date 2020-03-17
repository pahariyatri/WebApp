from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="Home"),
    path("index",views.index, name="index"),
    path("about",views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("explore", views.offers, name="offers"),
    path("find",views.index, name="upcoming_destination"),

]
