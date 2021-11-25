from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util
from . import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


#Create New Page
def crp(request):
    # if request.method == "POST":
    #     form = forms.PageForm(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data["title"]
    #         content = form.cleaned_data["content"]

    #         return HttpResponseRedirect(reverse("encyclopedia:index"))
    #     else:
    #         return render(request, "encyclopedia/crp.html", {
    #             "form": form
    #         })
    # else: #not posting to create new page.html
    #     form = forms.PageForm
    return render(request, "encyclopedia/crp.html", {
        "form": PageForm()
    })

# def index from tasks from lecture 3    
def view(request):
    pass
    # if "entries" not in request.session:
    #     request.session["entries"] = []
    # return render(request, "encyclopedia/index.html", {
    #     "entries": request.session["entries"]
    # })