from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kariru", views.kariru, name="kariru"),
    path("kasu", views.kasu, name="kasu"),
    path("kakunin", views.kakunin, name="kakunin"),
]
