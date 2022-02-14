from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("search", views.search,name="search"),
    path("newPage", views.newPage,name="newPage"),
    path("newPageSave",views.newPageSave,name="newPageSave"),
    path("randomPage", views.randomPage, name="randomPage")
]
