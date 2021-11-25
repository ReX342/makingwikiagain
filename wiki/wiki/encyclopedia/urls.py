from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
    path("<str:title>", views.detailv, name="detailview"),
]
