from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '<h1>Mi 1er API</h1>'

@app.route('/books', methods=['GET'])
def get_books():
    return books

@app.route('/book', methods=['GET'])
def get_books_by_id():
    id = int(request.args['id'])
    res = [book for book in books if book['id']==books['id']]
    return res

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return books

app.run()