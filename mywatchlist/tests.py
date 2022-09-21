from mywatchlist.views import show_json,show_xml,my_watchlist
from django.test import TestCase,Client
from django.urls import resolve


# Create your tests here.

# Function untuk Melakukan Testing terhadap Url Watchlist
class Tugas3UnitTest(TestCase):
    # test HTML
    # def test_url_check_html(Self):
    #     response = Self.client.get('http://localhost:8000/mywatchlist/html')
    #     Self.assertRedirects(response,'http://localhost:8000/mywatchlist/html',status_code = 301, target_status_code=200)
    # # test XML
    # def test_url_check_xml(Self):
    #     response = Self.client.get('http://localhost:8000/mywatchlist/xml')
    #     Self.assertRedirects(response,'http://localhost:8000/mywatchlist/xml',status_code = 301, target_status_code=200)
    # # test JSON
    # def test_url_check_json(Self):
    #     response = Self.client.get('http://localhost:8000/mywatchlist/json')
    #     Self.assertRedirects(response,'http://localhost:8000/mywatchlist/json',status_code = 301, target_status_code=200)

    # test HTML
    def test_url_check_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEquals(response.status_code,200)
        # test XML
    def test_url_check_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEquals(response.status_code,200)
        # test JSON
    def test_url_check_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEquals(response.status_code,200)