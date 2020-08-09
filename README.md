# Dokumentasi API dengan data book_c.csv</h1>
    Created by Aditya Wicaksono - August 2020
## Introduction 
    API (Application Programming Interface) ini digunakan untuk mengambil data dari books_c.csv melewati webpage yang telah ditentukan routenya.

## Method list

### STATIC ENDPOINT 1: Method `top10`
            Menampilkan top 10 Author berdasarkan jumlah rating per author<br>

### STATIC ENDPOINT 2: Method `top10_score`
            Menampilkan top 10 Author dan rata-rata skor rating<br>


### DYNAMIC ENDPOINT 1: Method `/book_rank/<value>'
            Menampilkan buku berdasarkan ranking, nomor ranking tergantung masukan dari user<br>

### DYNAMIC ENDPOINT 2: Method `/author_rank/<value>'
            Menampilkan author berdasarkan ranking, nomor ranking tergantung masukan dari user<br>

### Usage case

                `localhost:5000/top10`
                'localhost:5000/top10_score`
                `localhost:5000/book_rank/1`
                `localhost:5000/book_rank/8`
                `localhost:5000/author_rank/1`
                `localhost:5000/author_rank/100`