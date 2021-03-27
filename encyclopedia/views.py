from django.shortcuts import render
import markdown2
from django import forms

from django.http import HttpResponse
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class SearchForm(forms.Form): # lhs search form
    search = forms.CharField(label='', 
    widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia'}))


def details(request, title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/404.html", {
            "message": "Requested page was not found"})
    else:
        return render(request, "encyclopedia/details.html", {
            "title":title.capitalize(),
            "entry":markdown2.markdown(util.get_entry(title)),
            "form": SearchForm()
        })