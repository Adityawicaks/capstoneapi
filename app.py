import pandas as pd
from flask import Flask, request
import sqlite3
import numpy as np

app = Flask(__name__)
book = pd.read_csv('data/books_c.csv')
app.debug = True


# documentation
@app.route('/docs')
def doc():
    page_html = '''
    <html>
        <body>
    <h1>Dokumentasi API dengan data book_c.csv</h1>
    Created by Aditya Wicaksono - August 2020
    <h2>Introduction</h2> 
    API (Application Programming Interface) ini digunakan untuk mengambil data dari books_c.csv melewati webpage yang telah ditentukan routenya.
    <br><br>
    <h2>Method list:</h2>
    <ol type="1">
        <li>
            <h3>STATIC ENDPOINT 1: Method `top10`</h3> 
            Menampilkan top 10 Author berdasarkan jumlah rating per author<br>
        </li>
        <li>
           <h3>STATIC ENDPOINT 2: Method `top10_score`</h3> 
            Menampilkan top 10 Author dan rata-rata skor rating<br>
            </ul>
        </li>
        <li>
        <li>
           <h3>STATIC ENDPOINT 3: Method `BrazilonFriday`</h3> 
            Menampilkan nilai jumlah invoice di Brazil di hari Jumat<br>
            </ul>
        </li>
        <li>


           <h3>DYNAMIC ENDPOINT 1: Method `/book_rank/<value>`</h3> 
            Menampilkan buku berdasarkan ranking, nomor ranking tergantung masukan dari user<br>
            <br><br>
        </li>
        <li>

           <h3>DYNAMIC ENDPOINT 2: Method `/author_rank/<value>`</h3> 
            Menampilkan author berdasarkan ranking, nomor ranking tergantung masukan dari user<br>
            <br><br>
        </li>
        
            <strong>Usage case</strong>
            <ul>
                <li>`localhost:5000/top10`</li>
                <li>`localhost:5000/top10_score`</li>
                <li>`localhost:5000/book_rank/1`</li>
                <li>`localhost:5000/book_rank/8`</li>
                <li>`localhost:5000/author_rank/1`</li>
                <li>`localhost:5000/author_rank/100`</li>
            </ul>

        </li>

    </ol>
    <br><br><br><br>
        </body>
    </html>
    '''

    return page_html


# Static Endpoint 1: top10 Author
@app.route('/top10')
def top10():
    popular_author = book.groupby(['authors'])['ratings_count'].sum().reset_index().sort_values(by=['ratings_count'],
                                                                                                ascending=False)
    pop_author = popular_author.drop(columns='ratings_count')
    top10 = pop_author.head(10)
    return (top10.to_json())


# Static Endpoint 2: top10 author score
@app.route('/top10_score')
def top10_score():
    popular_author = book.groupby(['authors'])['ratings_count'].sum().reset_index().sort_values(by=['ratings_count'],
                                                                                                ascending=False)
    avg_author = book.groupby(['authors'])['average_rating'].mean().reset_index()
    top10_score = popular_author.merge(avg_author, on='authors', how='left')
    top10_mean = top10_score.head(10)
    return (top10_mean.to_json())


# Dynamic Endpoint: Book Rank by Rating
@app.route('/book_rank/<value>', methods=['GET'])
def book_ranked(value):
    popular_book = book.groupby(['title', 'authors', 'ratings_count'])[
        'average_rating'].sum().reset_index().sort_values(by=['ratings_count', 'average_rating'], ascending=False)
    p_book = popular_book.reset_index().reset_index()
    p_book['rank'] = p_book['level_0'] + 1  # create new column 'rank'

    # move 'rank' column to front
    col_name = 'rank'
    first_col = p_book.pop(col_name)
    p_book.insert(0, col_name, first_col)

    book_ranked = p_book.drop(columns=['level_0', 'index'])  # drop column old index
    book_ranked['rank'] = book_ranked['rank'].astype(str)  # change int to string
    mask = book_ranked['rank'] == value
    book_ranked = book_ranked[mask]
    return (book_ranked.to_json())


# Dynamic Endpoint: Author Rank by Rating
@app.route('/author_rank/<value>', methods=['GET'])
def author_ranked(value):
    popular_author = book.groupby(['authors'])['ratings_count'].sum().reset_index().sort_values(by=['ratings_count'],
                                                                                                ascending=False)
    avg_author = book.groupby(['authors'])['average_rating'].mean().reset_index()
    top10_score = popular_author.merge(avg_author, on='authors', how='left')
    p_author = top10_score.reset_index().reset_index()
    p_author['rank'] = p_author['level_0'] + 1  # create new column 'rank'

    # move 'rank' column to front
    col_name = 'rank'
    first_col = p_author.pop(col_name)
    p_author.insert(0, col_name, first_col)

    author_ranked = p_author.drop(columns=['level_0', 'index'])  # drop column old index
    author_ranked['rank'] = author_ranked['rank'].astype(str)  # change int to string
    mask = author_ranked['rank'] == value
    author_ranked = author_ranked[mask]
    return (author_ranked.to_json())


@app.route('/BrazilonFriday')
def BrazilonFriday():
    conn = sqlite3.connect("data/chinook.db")
    data = pd.read_sql_query(
        '''
        SELECT customers.FirstName,customers.LastName,invoices.CustomerId,customers.country,invoices.Total,invoices.InvoiceDate
        FROM customers
        LEFT JOIN invoices
        ON customers.CustomerId = invoices.CustomerId
        ''',
        conn
    )

    data['InvoiceDate'] = data['InvoiceDate'].astype('datetime64')
    data['InvoiceDOW'] = data['InvoiceDate'].dt.day_name()
    dayorder = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    BrazilonFriday = data[(data['InvoiceDOW'] == 'Friday') & (data['Country'] == 'Brazil')].pivot_table(index='InvoiceDOW',columns='Country',values='Total',aggfunc='sum').melt()
    return (BrazilonFriday.to_json())


if __name__ == '__main__':
    app.run(debug=True, port=5000) 
