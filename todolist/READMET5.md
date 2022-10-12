### PBP Assignment 5 :memo:

### Deployment Link Please Check:
[Assignment 5 Rani](https://katalog-rani.herokuapp.com/todolist/)

####  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline: Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HMTL mempunyai atribut style. Di situlah inline CSS ditulis.
- Internal: Internal CSS adalah kode CSS yang ditulis dalam tag<style> dan kode HTML yang ditulis di bagian header file HTML.  Internal CSS digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan di halaman website yang lain.  Internal CSS dapat digunakan untuk membuat tampilan website jadi lebih unik
- External: External CSS adalah kode CSS yang ditulis terpisah dari kode HTML. External CSS ditulis di sebuah file khusus menggunakan ekstensi .css. File external CSS umumnya diletakkan setelah bagian <head> di halaman. 
  
 
####  Jelaskan tag HTML5 yang kamu ketahui.
- ```<!DOCTYPE>``` -> Tag untuk menentukan tipe dokumen
- ```<body>``` -> Tag untuk membuat tubuh dari sebuah halaman
- ```<button>``` -> Tag untuk membuat sebuah tombol yang dapat diklik
- ```<datalist>``` -> Menentukan daftar pilihan yang telah ditetapkan untuk kontrol input 
- ```<textarea>``` -> Tag untuk membuat sebuah kontrol input multibaris (text area)

####  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Selektor Tag
```
  p {
    color: blue;
}
 ```

- Selektor Class
```
  .pink {
  color: white;
  background: pink;
  padding: 5px;
}
  ```
- Selektor ID
 ```
  #header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}
  ```
 - Selektor Atribut
 ```
  input[type=text] {
    background: none;
    color: cyan;
    padding: 10px;
    border: 1px solid cyan;
}
  ```
 - Selektor Universal
  ```
  * {
    border: 1px solid grey;
}
  ```
  - Pseudo Selektor
 ```
  * {
    border: 1px solid grey;
}
  ```
 
 ####  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Mendownload CSS dan JS pada bootsrap dan memasukkannya ke sebuah file yang static
2. Menghias file .html dengan seperti login, register, create, delete
  3. Mengaplikasikan komponen ke dalam html menggunakan kode yang ada pada Bootstrap
