from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import BarangWatchlist

# Create your views here.

def my_watchlist(request):
    data_my_watchlist = BarangWatchlist.objects.all()
    watched = 0
    unwatched = 0
    response = ""
    for movie in data_my_watchlist:
        if (movie.watched == True):
            watched += 1
        else:
            unwatched += 1

    if (watched > unwatched):
        response = "Selamat, kamu sudah banyak menonton!"
    elif (watched == unwatched):
        response = "Waduh, jatah menonton kamu dan belum menonton kamu setengah - setengah nih"
    elif(watched < unwatched):
        response = "Wah, kamu masih sedikit menonton"
    context = {
        'list_movie': data_my_watchlist,
        'nama': 'Amelia Putri Chaerani',
        'npm' : '2106751985',
        'response': response,

}
    return render(request, 'watchlist.html',context)

def show_xml(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
