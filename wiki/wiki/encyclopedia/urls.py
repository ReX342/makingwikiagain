# from django.http import HttpResponse
# from django.http import HttpResponseNotFound
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, reverse
# from django.contrib import messages

# import markdown
# from . import util
# from . import forms
# None of this helps to gget detail view working

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
    path("<str:title>", views.detailv, name="detail view"),
]
