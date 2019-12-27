from django.shortcuts import render, redirect

from core.models import Dork


def index(request):
    dorks = Dork.objects.all()
    return render(request, 'index.html', {'dorks':dorks})

def get_query(request, selected_dork):
    dork = Dork.objects.get(id=selected_dork)
    return render(request, 'search.html', {'dork': dork})


def search(request, id, query):
    google_url = 'https://www.google.com/search?q='
    dork = Dork.objects.get(id=id)
    new_url = google_url+dork.dork+str(query)
    return redirect(new_url)
