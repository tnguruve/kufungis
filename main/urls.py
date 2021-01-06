from django.urls import path
from . import views

# these direct users to the right urls
urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("register/", views.home, name="register"),
path("create/", views.create, name="index"),
path("<int:id>", views.index, name="index"),
]