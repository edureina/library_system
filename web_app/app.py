# web_app/app.py


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask, render_template, request
from library_lib.models import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html", sistema=Triadu)

@app.route("/user_registration", methods=["GET"])
def user_registration_formular():
    return render_template("user_registration.html")

@app.route("/user_registration", methods=["POST"])
def user_registration_process():
    # Get the data from the form
    nombre = request.form["nombre"]
    NewUser = Usuario(nombre, 3456, [])

    return f"Hola, {nombre}. Your user has been created"

@app.route("/system_status", methods=["GET"])
def system_status():
    status = Triadu.mostrar_estado_systema_as_text()
    return f"<pre>{status}</pre>"



if __name__ == "__main__":


    Sistema_cargado = SistemaBibliotecas.cargar_biblioteca("fitxer_biblioteques.pkl")
    Triadu = Sistema_cargado["Triadu"]

    app.run(debug=True)

