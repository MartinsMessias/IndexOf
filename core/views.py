from django.shortcuts import render
from core.models import Dork


def index(request):
    dorks = Dork.objects.all()
    return render(request, 'index.html', {'dorks':dorks})