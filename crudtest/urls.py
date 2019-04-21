from django.urls import path
from crudtest import views

urlpatterns = [
    path("", views.index, name="index"),
]
