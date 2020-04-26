from django.urls import path
from . import views

urlpatterns = [
    path("user_register",views.user_register, name="user_register"),
    path("user_login",views.user_login, name="user_login"),
    path("logout",views.logout, name="logout"),
    path("snippet", views.snippet_detail, name="snippet"),
]