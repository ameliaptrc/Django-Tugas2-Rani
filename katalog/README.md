## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas html!

<img width="2617" alt="Untitled" src="https://user-images.githubusercontent.com/103547185/190173477-4b72924d-2898-4b23-a884-c6d0eeb2418c.png">

- Client mengirimkan request ke URL Conf, setelah itu URL akan memilih view yang tepat yang sesuai. Lalu, views akan menampilan template yang sesuai dengan request oleh client. Jika client tersebut meminta query data, maka views akan meminta ke model dan akan dibuatkan struktur data, setelah itu, model melakukan transaksi data ke database. (meminta sebuah data ke database).
- Data yang sudah didapatkan dari database, maka dikembalikan ke models dan respond date ke views. Views akan memilih template HTML yang cocok ke webpage yang diinginkan. 
- Menggunakan cara ini  memudahkan kita untuk memantain dan menhandle webpage kita. 

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

#### Jelaskan kenapa menggunakan virtual environment?
Virtual environment merupakan sebuah alat yang membantu kita dalam setiap pembuatan proyek. Proyek tersebut akan terisolasi dari direktori sistem dan memiliki python packages tersendiri di dalam virtual environment tersebut.
Dalam tugas ini, virtual environment mengisolasi depedencies dan packages yang digunakan pada proyek ini. Kegunaan virtual environment adalah terisolasi dari proyek lain maka proyek kita tidak akan terganggu dan memudahkan testing.
#### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawabannya adalah Ya, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, akan mendapatkan berbagai masalah. Contohnya ketika kita mempunyai berbagai projects di dalam perangkat yang sama. Project tersebut akan mengalami conflict depedencies. Conflict tersebut akan mengganggu packages dan depedencies lain. Maka, lebih disarankan menggunakan virtual environment.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

#### Poin 1
- Di dalam views.py terdapat fungsi ```show_catalog``` yang didalamnya terdapat pengambilan data. Jalan kerjanya adalah di dalam function tersebut terdapat parameter untuk pengambilan data. Pengambilan data dilakukan di ```variabel data_barang_catalog``` yang mengambil data dari ```CatalogItem```. Data yang didapatkan dari database kemudian akan dikembalikan lagi ke Models dan kembali ke Query Database. Lalu, function ini membuat suatu context yang berisi nama, npm, dan listbarang dan akan dirender sehingga data tersebut nantinya akan muncul pada file html.
- Context adalah template yang digunakan di html tersebut.


#### Poin 2
- di dalam ```urls.py``` ditambahkan sebuah path yaitu ```path('katalog/', include('katalog.urls'))``` berguna untuk menyambungkan ```urlpatterns```.
- di dalam ```urls.py``` ditambahkan sebuah path yaitu ```path('', show_katalog, name='show_katalog')``` berguna untuk mengubah katalog di ```show_catalog```

#### Poin 3
- Untuk pemetaan data template, terdapat ```nama``` dan ```npm``` lalu terdapat detail list barang sesuai dengan apa yang diinginkan.

#### Poin 4
- Membuat aplikasi di Herokuapp dan menghubungkannya di github dengan cara mengakses repository kita dan masuk ke secret dan menambahkan dua secrets yaitu ```HEROKU_API_KEY``` dan ```HEROKU_APP_NAME```. Setelah itu di deploy sesuai dengan perintahnya atau menggunakan re-run jobs agar deploy dengan sempurna.


### Credits:
- https://towardsdatascience.com/why-you-should-use-a-virtual-environment-for-every-python-project-c17dab3b0fd0
- https://www.youtube.com/watch?v=qGPSGuTqajo
- https://www.youtube.com/watch?v=twu1t_yo0PM
