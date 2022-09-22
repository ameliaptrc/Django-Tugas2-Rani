#### Deployment Link
[Tugas 3 Rani](https://katalog-rani.herokuapp.com/mywatchlist/)

## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!

- ```JSON``` dengan kepanjangan **JavaScript Object Notation** adalah sebuah format untuk menyimpan, membaca, dan menukar informasi dari web server sehingga dapat dibaca oleh pengguna. Nama file JSON adalah ```extension.json```.JSON merupakan subset dari ```JavaScript```.Hampir semua web modern yang digunakan sudah mendung format JSON. JSON dibangun dengan dua struktur, yaitu **name & value pairs** dan **ordered list of values**.JSON menggunakan ```REST API```dan didukung oleh encoding UTF-8 dan UTF-16.  JSON tidak bisa di extent.

- ```XML``` dengan kepanjangan **Extensive Markup Languange** adalah sebuah _markup language_ untuk menyimpan dan mengantarkan data. Kelebihan XML adalah easy to read, unambiguous, extensible, platform - independent. XML merupakan turunan dari SGML seperti HTML. XML menggunakan tag yaitu setiap start tags harus mempunyai end tags, lalu harus memiliki element root. Tag - tag tersebut dapat dikembangkan dan XML umumnya berorientasi pada isi. Ekstensi file pada XML adalah ```extension.html```. XML lebih _extensible_ dan rumit untuk file besar.
- ```HTML``` dengan kepanjangan **Hyper Text Markup Language** adalah sebuah _markup language_ untuk mengelola serangakaian data dan informasi sehingga suatu dokumen dapat ditampilkan di internet melalui layanan web. Extension dalam html adalah ```extension.html```.HTML memiliki tag - tag yang fixed, berorientasi pada tampilan, dan tidak mempunyai kemampuan untuk melakukan validasi data. HTML tidak memiliki sintaks penyimpanan dan pertukaran data seperti dua diatas.

## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Data delivery digunakan untuk mempermudah proses pertukaran data. Data delivery digunakan untuk mengambil dan menaruh data. Penggunaan pada data delivery akan mempermudah manusia untuk _cross platform_.Keutamaan data delivery adalah data yang dikirim ke berbagai platform dapat ditampilan ke user sehingga user dapat memahami dan menikmati data tersebut dengan struktur berbeda misalnya menggunakan JSON, HTML, XML.  
## 3.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Pertama - tama, kita harus menyalakan _virtual environment_ 
dengan cara ```python -m venv env``` dan ```env\Scripts\activate.bat```
#### Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
- membuat folder ```mywatchlist``` yang terdapat pada tugas lalu (di file saya, berada di PBP-Rani)
- setelah itu, dalam _cmd_ setelah masuk ke dalam virtual environment, menuliskan sebuah command ```python manage.py startapp mywatchlist```
#### Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
#### Membuat sebuah model ```MyWatchList``` yang memiliki atribut sebagai ```watched```,```title```,```rating```,```release_date```,```review```
- Sebelum user dapat mengakses localhost, saya mengubah dan menambahkan beberapa codingan di ```models.py```, ```views.py```, dan ```urls.py```
- Dalam ```models.py```, menambahkan ```watched```,```title```,```rating```,```release_date```,```review``` dan mengaplikasikannya ```python manage.py makemigrations``` setelah itu ```python manage.py migrate```.
- Dalam ```views.py```, menambahkan ```my_watchlist```,```show_xml```,```show_json```
- Dalam ```urls.py```, menambahkan path yang akan diimplementasikan untuk memetakan request dalam bentuk JSON, HTML, XML.
- Dalam ```urls.py```, untuk menambahkan path mywatchlist maka menuliskan command ```path('mywatchlist/', include('mywatchlist.urls'))``` untuk menghubungkan ```urlpatterns``` pada ```project_django``` dan ```mywatchlist```.
#### Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
- Menambahkan data di ```initial_mywatchlist_data.json``` sebelum itu, membuat folder ```fixtures```terlebih dahulu, sesuai dengan format dan berisikan 10 data yang telah dianjurkan.
- ![image](https://user-images.githubusercontent.com/103547185/191641335-c161c99d-3876-48be-894c-79aeade25c87.png)
- Membuat sebuah fungsi untuk mengembalikan data HTML, JSON, dan XML.
- Memetakan template ke ```watchlist.html```
- Membuat  ```test.py``` untuk mengecek app yang dibuat.
#### Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Membuat aplikasi di Heroku.com, menambahkan secrets yang terdiri dari ```HEROKU_APP_NAME``` dan ```HEROKU_API_KEY```. Lalu melakukan re-run jobs untuk mendeploy dengan benar.
- Sudah terdapat ```API_KEY``` dan ```APP_NAME``` pada tugas lalu.

### Postman Screenshot
**Postman HTML**
![postman html](https://user-images.githubusercontent.com/103547185/191642477-f01e4ac1-a0ec-481e-8da6-10d172200514.png)
**POSTMAN JSON**
![postman json](https://user-images.githubusercontent.com/103547185/191642699-3854b327-35ff-4bb2-95c2-eb9a1c03c68b.jpg)
**POSTMAN XML**
![postman xml](https://user-images.githubusercontent.com/103547185/191642656-da35da3c-d1eb-4f5b-8080-d937e23fc15d.png)
