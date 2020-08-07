from flask import Flask, request 
import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

#hello world
@app.route('/home')
def home():
    return 'Hello World'

#test query localhost:5000/query?name=Budi Setiawan&age=32
@app.route('/query')
def query_example():
    key1 = 'name'
    key2 = 'age'
    name = request.args[key1] # Jika key tidak disertakan dalam URL, maka akan terjadi server error
    age = request.args.get(key2) # Jika key tidak disertakan dalam URL, maka age akan bernilai None
    return(f"Hello, {name}, yoau are {age} years old")

#test get post
@app.route('/coba', methods=['GET', 'POST'])
def terserah():
    if request.method == 'GET':
        return "Ini adalah Hasil method GET"
    else:
        return "Ini adalah hasil method POST"

#form
@app.route('/form', methods=['GET', 'POST']) #allow both GET and POST requests
def form():
    if request.method == 'POST':  # Hanya akan tampil setelah melakukan POST (submit) form
        key1 = 'name'
        key2 = 'age'
        name = request.form.get(key1)
        age = request.form[key2]

        return (f'''<h1>Your Name  is: {name}</h1>
                   <h1>Your Age is: {age}</h1>
                ''')


    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  Age: <input type="text" name="age"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''
#json
@app.route('/json', methods=['POST'])
def json_exmp():

    req = request.get_json(force=True) # melakukan parsing data json, menyimpannya sebagai dictionary

    name = req['name']
    age = req['age']
    address = req['address']

    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')

# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET'])
def get_data(data_name):
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())


# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET'])
def get_data_equal(data_name, column, value):
    data = pd.read_csv('data/' + str(data_name)) #membaca data <data name>
    mask = data[column] == value #filtering
    data = data[mask]
    return (data.to_json())



@app.route('/test', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colours=colours)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 