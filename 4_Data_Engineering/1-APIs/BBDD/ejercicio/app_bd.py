
import sqlite3
from flask import g, Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

DATABASE = 'books.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 0.Ruta para obtener todos los libros
@app.route('/libros', methods=['GET'])
def get_libros():
    db = get_db()
    cur = db.execute('SELECT * FROM books')
    books = [dict(row) for row in cur.fetchall()]
    return jsonify(books)

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/conteo', methods=['GET'])
def get_conteo():
    db = get_db()
    cur = db.execute('SELECT author, count(title) as n_books from books GROUP by author ORDER BY n_books DESC')
    books = [dict(row) for row in cur.fetchall()]
    return jsonify(books), 200

# 2.Ruta para obtener los libros de un autor
@app.route('/libros_autor', methods=['GET'])
def get_libros_autor():
    db = get_db()
    author = request.args['author']
    cur = db.execute(
        'SELECT * FROM books WHERE author LIKE ?', 
        (f'%{author}%',)
        )
    libros_author = [dict(row) for row in cur.fetchall()]
    return jsonify(libros_author), 200
# http://127.0.0.1:5000/libros_autor?author=Asako

# 3.Ruta para añadir un libro
# @app.route('/add_libro', methods=['POST'])
# def add_book():
#     # data = request.json()
#     db = get_db()
#     cur = db.execute("""insert into books (published, author, title, first_sentence)
#                      VALUES (2007, 'Muriel Barbery', 'La elegancia del erizo', 
#                      'En el número 7 de la calle Grenelle, un inmueble burgués de París, nada es lo que parece. Dos de sus habitantes esconden un secreto. 
#                      Renée, la portera, lleva mucho tiempo fingiendo ser una mujer común. 
#                      Paloma tiene doce años y oculta una inteligencia')""")
#     db.commit()
#     return jsonify({"message": "Libro añadido correctamente"}), 201


@app.route('/add_libro_sql_2', methods=['POST'])
def add_book():
    db = get_db()
    cur = db.execute("""
        INSERT INTO books (published, author, title, first_sentence)
        VALUES (
            2021,
            'Anna Sólyom',
            'Neko Café',
            'La vida de Nagore ha sido una sucesión de calamidades desde que se separó de su pareja y fue despedida de su último trabajo...'
        )
    """)
    db.commit()

    # new_id = cur.lastrowid   # aqui no tenemos id
    # cur.execute("SELECT * FROM books WHERE id = ?", (new_id,))
    # libro_nuevo = cur.fetchone()

    # return jsonify(dict(libro_nuevo)), 201

    return jsonify({"message": "Libro añadido correctamente"}), 201

@app.route('/add_json', methods=["POST"])
def post_books():
    data = request.get_json()
    print('------------------------------ data:', data)
    db = get_db()
    cur = db.execute("INSERT INTO books (published, author, title, first_sentence) VALUES (?, ?, ?, ? )",
        (data['published'], data['author'], data['title'], data['first_sentence'],))
    db.commit()
    return jsonify({"message": "Libro añadido correctamente"}), 201

"""
{
    "published": 2016,
    "author": "Asako Hiruta",
    "title": "La insólita pasión del vendedor de lencería",
    "first_sentence": "Satsuko tiene 32 años, trabaja en una agencia de publicidad y, a decir verdad, no lleva la vida más plena del mundo."
    }
"""

app.run()