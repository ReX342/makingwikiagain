from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def crp(request):
    #Create New Page
    return render(request, "crp.html", {
        
    })