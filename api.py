from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {'id':1, 'titulo':'Star Wars', 'genero':'sci-fi'},
    {'id':2, 'titulo':'It', 'genero':'Horror'},
    {'id':3, 'titulo':'Um tira da pesada', 'genero':'commedy'}
]

@app.route('/api/movies')
def get_movies():
    return jsonify(movies)