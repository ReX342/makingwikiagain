from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponse
from django.urls import reverse
from .forms import PageForm

import markdown

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
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('view', kwargs={'title': title}))
        else:
            pass
    else:
        form = PageForm(request.POST)
    return render(request, 'crp.html', {'form': form})



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
#return HttpResponseRedirect(reverse('view', kwargs={'name': title}))
#Look at documentation source (lecture 3 source code base) for ragna wiki

# def index from tasks from lecture 3

# overview_posts on ragna wiki    
def view(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# view_post    
def detailv(request, title):
    if not title in util.list_entries():
        return HttpResponseNotFound("Could not find that entry!")
    entire_entry = util.get_entry(title)
    # Markdown to HTML
    html_entry = markdown.markdown(entire_entry)
    
    return render(request, "detailv.html", {
        "title": title,
        "content": html_entry
    })

