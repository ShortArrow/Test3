from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kariru", views.kariru, name="kariru"),
    path('kariru/<int:num>', views.kariru, name='kariru'),
    path("kasu", views.kasu, name="kasu"),
    path("kakunin", views.kakunin, name="kakunin"),
    path("mailpage", views.mailpage, name="mailpage"),
    path("edit/<int:num>", views.edit, name='edit'),
    path("delete/<int:num>", views.delete, name='delete'),
    path("find", views.find, name='find'),
    path("message/", views.message, name="message"),
    path("message/<int:page>", views.message, name="message"),
]
