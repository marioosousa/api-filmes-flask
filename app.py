#! /usr/bin/python
#! -*- coding utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

filmes = [
    {"id": 1, "titulo": "Cidadão Kane", "autor": "Orson Welles", "ano": 1941},
    {"id": 2, "titulo": "O Poderoso Chefão", "autor": "Francis Ford Coppola", "ano": 1972},
    {"id": 3, "titulo": "Pulp Fiction: Tempo de Violência", "autor": "Quentin Tarantino", "ano": 1994},
    {"id": 4, "titulo": "Titanic", "autor": "James Cameron", "ano": 1997},
    {"id": 5, "titulo": "Central do Brasil", "autor": "Walter Salles", "ano": 1998},
    {"id": 6, "titulo": "Matrix", "autor": "Lana e Lilly Wachowski", "ano": 1999},
    {"id": 7, "titulo": "A Viagem de Chihiro", "autor": "Hayao Miyazaki", "ano": 2001},
    {"id": 8, "titulo": "Cidade de Deus", "autor": "Fernando Meirelles", "ano": 2002},
    {"id": 9, "titulo": "A Origem", "autor": "Christopher Nolan", "ano": 2010},
    {"id": 10, "titulo": "Parasita", "autor": "Bong Joon-ho", "ano": 2019}
]

@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify({"filmes": filmes}), 200

if __name__ == "__main__":
    app.run(debug=True)