from django.shortcuts import render, redirect

from core.models import Dork

google_url = 'https://www.google.com/search?q='

def index(request):
    dorks = Dork.objects.all()
    return render(request, 'index.html', {'dorks':dorks})

def get_query(request, selected_dork):
    dork = Dork.objects.get(id=selected_dork)
    return render(request, 'search.html', {'dork': dork})


def search(request, dork):

    if request.method ==  'GET':
        query = request.GET.get('query')
        new_url = str(str(google_url)+str(dork)+str(query)).replace('&', '%26')
        return redirect(new_url)
    redirect(index)

def search_music(request):
    if request.method ==  'POST':
        singer = request.POST.get('query-singer')
        music = request.POST.get('query-music')
        query = 'intitle:”index.of ”'+ str(singer) + '”parent directory” “size” “last modified” “description” '+str(music)+' (mp4|mp3|avi|flac|alac|ape|ogg) -inurl:(jsp|php|html|aspx|htm|cf|shtml|lyrics-realm|mp3-collection) -site:.info'
        new_url = str(google_url)+str(query)
        return redirect(new_url)
    return render(request, 'music.html')
