# API dengan data book_c.csv & Chinook db</h1>
    This is a project for Algoritma Capstone Project Python for Data Analyst
    Created by Aditya Wicaksono - August 2020
## Introduction 
    API (Application Programming Interface) ini digunakan untuk mengambil data dari books_c.csv melewati webpage yang telah ditentukan routenya.

## Endpoint list

### STATIC ENDPOINT 1:  Endpoint `top10`
            Menampilkan top 10 Author berdasarkan jumlah rating per author<br>

### STATIC ENDPOINT 2: Endpoint `top10_score`
            Menampilkan top 10 Author dan rata-rata skor rating<br>
            
### STATIC ENDPOINT 3: Endpoint `BrazilonFriday`
            Menampilkan nilai jumlah invoice di Brazil di hari Jumat<br>

### DYNAMIC ENDPOINT 1: Endpoint `/book_rank/<value>`
            Menampilkan buku berdasarkan ranking, nomor ranking tergantung masukan dari user<br>

### DYNAMIC ENDPOINT 2: Endpoint `/author_rank/<value>`
            Menampilkan author berdasarkan ranking, nomor ranking tergantung masukan dari user<br>

### Usage case

                `localhost:5000/top10`
                `localhost:5000/top10_score`
                `localhost:5000/book_rank/1`
                `localhost:5000/book_rank/8`
                `localhost:5000/author_rank/1`
                `localhost:5000/author_rank/100`
### Usage case HEROKU
https://capstone-api1.herokuapp.com/docs ->documentation <br>
https://capstone-api1.herokuapp.com/top10 <br>
https://capstone-api1.herokuapp.com/top10_score <br>
https://capstone-api1.herokuapp.com/book_rank/5 <br>
https://capstone-api1.herokuapp.com/author_rank/20 <br>
https://capstone-api1.herokuapp.com/BrazilonFriday
