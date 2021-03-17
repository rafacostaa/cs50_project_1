from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def detail(request, title):
    return render(request, "encyclopedia/detail.html", {
        "entries": util.get_entry(title)
    })