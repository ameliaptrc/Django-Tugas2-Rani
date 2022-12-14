from django.urls import path
from mywatchlist.views import my_watchlist
from mywatchlist.views import show_xml 
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', my_watchlist, name='my_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/',my_watchlist, name= 'show_mywatchlist')
]