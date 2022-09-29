### PBP Assignment 4 :memo:

### Deployment Link Please Check:
[Assignment 4 Rani](https://katalog-rani.herokuapp.com/todolist/)

:warning: You Must Login To Create To - Do List! :warning:

####  1. Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
- ```{% csrf_token %}``` adalah (Cross-site Request Forgery) adalah salah satu jenis serangan keamanan web untuk mendapatkan atau mengirim request yang dieksekusi atas wewenang korban, tanpa dikehendakinya. 
- ```{% csrf_token %}``` berguna untuk mencegah dan melindungi dari CSRF yang akan membuat attackers tidak mungkin melakukan request terkait dengan POST/GET dalam sebuah web. Menggunakan ```{% csrf_token %}``` dilakukan dengan menghasilkan token di sisi server dan akan merecheck ulang permintaan tersebut, jika permintaan tersebut tidak cocok maka permintaan pada form akan ditolak. 
- Jika tidak terdapat potongan kode tersebut maka route link yang dapat diakses oleh orang lain tanpa recheck (mempunya celah) dan dapat diretas oleh orang lain.

#### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
- Jawabannya adalah Ya, kita dapat membuat form secara manual. Dalam lab kali ini, kita bisa berkreatif membuat ```forms.py``` atau manual sesuai dengan keinginan kita. Cara membuat <form> manual adalah:
```
<body>
    <form method="post">
        {% csrf_token %}
        {% for field in form %}
        <label for="{{ field.auto_id }}">
            {{ field.label }}
            {% for error in field.errors %}
            {{ error }}
            {% endfor %}
        </label>

        <div>
            {{ field }}
        </div>
        {% endfor %}
        <div>
            <input type="button" value="Simpan">
        </div>
    </form>
</body>
```
- dari sepotong kode berikut, maka kita bisa menyimpulkan bahwa membuat form manual membutuhkan:
1.  elemen ```<form>```
2.  elemen ```<input>``` dan ```<type>``` atau ```<value>``` digunakan untuk submit data sesuai dengan keinginan kita.

#### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Isi Data
- User mengisi data pada form tersebut. Menggunakan POST.
2. Check Data
- Data yang dimasukkan oleh user akan dicheck kembali apakah data tersebut valid atau tidak.
3. Interaksi dengan Models
- Data yang valid tersebut akan diproses dan akan berinteraksi dengan Models yang disalurkan ke database nantinya. 
4. Menampilkan HTML
- Setelah dikirimkan database, model tersebut disalurkan ke HTML dan ditampilkan di HTML.

#### 4. Implementasi
###### Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
- Setelah mengaktifkan virtual environment, lalu di cmd menuliskan sebuah command yaitu ```python manage.py startapp todolist```
###### Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
 - Cara menambahkan path adalah dalam ```urls.py```, untuk menambahkan todolist maka menuliskan command yaitu ```path('todolist/', include('todolist.urls'))``` dengan tujuan untuk menghubungkan ```urlpatterns``` pada ```project_django``` dan ```todolist```
###### Membuat sebuah model Task yang memiliki atribut ```user```,```date```,```title```,```is_finished```:
- Di dalam ```models.py``` saya menambahkan ```user```,```date```,```title```,```is_finished``` di kelas ```Task``` dan mengaplikasikannya dengan ```python manage.py makemigrations``` setelah itu ```python manage.py migrate```
###### Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
- Pengimplementasikan form registrasi, login, dan logout dilakukan di ```views.py``` dan menambahkan path di ```urls.py``` yang akan diimplementasikan untuk fitur tersebut.
###### Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
- Halaman utama tersebut dibuat di ```todolist.html``` sesuai dengan ketentuan yang berlaku, sebelum membuat htmlnya harus terdapat ```show_todolist``` dalam ```views.py``` yang akan dipanggil.
- Halaman lain dibuat di ```create_task.html``` sesuai dengan ketentuan yang berlaku, sebelum dibuat htmlnya maka membuat ```create_task``` terlebih dahulu dalam ```views.py``` yang akan dipanggil. 
- Sama seperti yang diatas, ```login.html``` dan ```register.html``` harus sesuai dengan ketentuan, dan harus terdapat fungsi di ```views.py``` maka nanti html tersebut dapat terpanggil.
###### Membuat halaman form untuk pembuatan task
- Pembuatan halaman form dimulai di ```views.py``` yaitu dibuat fungsi ```create_task``` dan akan diimplementasikan di ```create_task.html```. Karena saya menggunakan ```forms.py``` maka saya akan membuat file forms terlebih dahulu dan nanti akan digunakan di ```create_task``` atau ```delete_task```.
###### Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut
- Merouting dengan cara fungsi - fungsi yang terdapat di ```views.py``` seperti ```register```,```login```,```logout```,```create-task```,```delete-task```,dan```change-status``` di dalam ```urlpatterns```
- Setelah merouting, silahkan dijalankan di ```python manage.py runserver```
###### Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Sebelum  mendeploy, kita harus melakukan git add, commit,push terlebih dahulu
- Setelah itu, aplikasi yang sudah kita punya akan berintegrasi dengan todolist kita sendiri karena telah dimasukkan ```APP_NAME``` dan ```API_KEY``` nya.
###### Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
akun pertama:
    ![image](https://user-images.githubusercontent.com/103547185/192919554-3cd03cca-b61e-43b9-a39c-5fec1ecba99e.png)
akun kedua:
    ![image](https://user-images.githubusercontent.com/103547185/192921183-b7672a21-5053-4210-ac3b-3e9efdabdd1b.png)

