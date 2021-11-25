from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
    path("<str:title>", views.detailv, name="detail view"),
]
