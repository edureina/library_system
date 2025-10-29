# web_app/app.py


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask, render_template
from library_lib.models import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html", sistema=Triadu)

if __name__ == "__main__":


    Sistema_cargado = SistemaBibliotecas.cargar_biblioteca("fitxer_biblioteques.pkl")
    Triadu = Sistema_cargado["Triadu"]

    app.run(debug=True)

