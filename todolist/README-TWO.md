### PBP Assignment 5 :memo:

### Deployment Link Please Check:
[Assignment 6 Rani](https://katalog-rani.herokuapp.com/todolist/)


##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronus dapat diartikan sebagai konsep pemrograman yang akan mengeksekusi kode program yang kita buat baris perbaris atau atas ke bawah sesuai dengan berurutan. Proses Sycnhronus adalah blocking, yang dapat diartikan sebagai harus menunggu proses sebelumnya selesai, lalu lanjut ke proses berikutnya. Umumnya menggunakan kode synchronus memakan waktu dan browser dapat ngefreeze.

- Asynchronus dapat diartikan sebagai konsep pemrograman yang akan mengeksekusi kode program secara terpisah dari program utama. Program akan melanjutkan baris kode selanjutnya, tanpa perlu menunggu proses asynchronus selesai. Umumnya menggunakan asynchronus menghemat waktu.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
- Event drive programming dapat diartikan sebagai salah satu pendekatan pada programming dimana objek dapat berkomunikasi secara tidak langsung dan berkomunikasi melalui sebuah perantara. Perantaranya adalah event dan dapat dieksekusi berdasarkan event. Event dapat mentrigger user untuk memencet tombol tertentu. Contoh Event Drive pada task ini adalah saat tombol ```Add Task``` yang memicu fungsi sehingga terdapat sebuah event yang berakibat muncul  di htmlnya.

## Jelaskan penerapan asynchronous programming pada AJAX.

- Penerapannya di AJAX dapat diaplikasikan ketika ingin mengeksekusi kode program secara terpisah dari kode program utama tanpa menungu proses asynchronus selesai. Dalam hal ini, browser tidak perlu meloading jika terdapat perubahan data yang kecil. Contohnya, ketika melakukan tambah task, program langsung bertambah tanpa mereload.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### Bagian Pertama

- Di ```views.py``` membuat view baru untuk mengembalikan seluruh data task berbentuk JSON.
- Connect ke ```urls.py``` dengan membuat path.
- Setelah dikembalikan datanya, lalu terdapat pengembalian task menggunakan ```AJAX GET```


#### Bagian Kedua

- Membuat tombol ```Add Task``` untuk mendapatkan task (menggunakan sebuah modal)
- Membuat view baru di ```views.py``` untuk mendapatkan task baru.
- Connect ke ```urls.py``` dengan membuat path
- Kita bisa melihat data secara asynchronus tanpa reload pagenya.
