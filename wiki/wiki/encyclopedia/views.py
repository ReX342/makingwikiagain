from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.urls import reverse
from .forms import PageForm

from . import util
from . import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#Create New Page
# https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
def crp(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PageForm()
    return render(request, 'home.html', {'form': form})
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
    return render(request, "encyclopedia/view.html", {
        "entries": util.list_entries()
    })
    
def detailv(request, title):
    entry_title = util.get_entry(title)
    return render(request, "detailv.html", {
        "title": entry_title,
        "content": content
    })

