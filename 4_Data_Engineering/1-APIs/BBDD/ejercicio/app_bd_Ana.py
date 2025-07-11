
import sqlite3
from flask import g, Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

DATABASE = 'books.db'

def conn_db_exec_query(str_query):
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()
    query = str_query
    res = cursor.execute(query).fetchall()
    con.commit()
    con.close()
    return jsonify(res)

# 0.Ruta para obtener todos los libros
@app.route('/libros', methods=['GET'])
def get_libros():
    query = 'SELECT * FROM books'
    res= conn_db_exec_query(query)
    return res, 200

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/conteo', methods=['GET'])
def get_conteo():
    query = 'SELECT author, count(title) as n_books from books GROUP by author ORDER BY n_books DESC'
    res= conn_db_exec_query(query)
    return res, 200

# 2.Ruta para obtener los libros de un autor
@app.route('/libros_autor', methods=['GET'])
def get_libros_autor():
    author = request.args['author']
    query = 'SELECT * FROM books WHERE author LIKE "%' + author +'%"'
        
    res= conn_db_exec_query(query)
    return res, 200
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
    query ="""
        INSERT INTO books (published, author, title, first_sentence)
        VALUES (
            2021,
            'Anna Sólyom',
            'Neko Café',
            'La vida de Nagore ha sido una sucesión de calamidades desde que se separó de su pareja y fue despedida de su último trabajo...'
        )
    """
    res= conn_db_exec_query(query)

    # new_id = cur.lastrowid   # aqui no tenemos id
    # cur.execute("SELECT * FROM books WHERE id = ?", (new_id,))
    # libro_nuevo = cur.fetchone()

    # return jsonify(dict(libro_nuevo)), 201

    return res, 201

@app.route('/add_json', methods=["POST"])
def post_books():
    data = request.get_json()
    query = "INSERT INTO books (published, author, title, first_sentence) VALUES (" + str(data['published'])+ ",'" + data['author']+ "','"+ data['title']+"','" +data['first_sentence'] + "')"
    print('------------------------------------------',query)
    res= conn_db_exec_query(query)
    return res, 201

"""
{
    "published": 1987,
    "author": "Haruki Murakami",
    "title": "Tokio blues",
    "first_sentence": "Toru Watanabe, un ejecutivo de 37 años, escucha casualmente mientras aterriza en un aeropuerto europeo una vieja canción de los Beatles, y la música le hace retroceder a su juventud, al turbulento Tokio de finales de los sesenta. "
    }
"""

app.run()