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
    Triadu.registrar_usuario(NewUser)

    resultado = Sistema_cargado.guardar_sistema("fitxer_biblioteques.pkl")

    resultado += f"\n Hola, {nombre}. Your user has been created"

    return f"<pre>{resultado}<pre>"

@app.route("/system_status", methods=["GET"])
def system_status():
    status = Sistema_cargado.mostrar_estado_systema_as_text() + "\n"
    return f"<pre>{status}</pre>"



if __name__ == "__main__":


    Sistema_cargado = SistemaBibliotecas.cargar_biblioteca("fitxer_biblioteques.pkl")
    Triadu = Sistema_cargado.sistema["Triadu"]

    app.run(debug=True)

