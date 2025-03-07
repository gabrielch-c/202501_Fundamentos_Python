from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = "papas fritas"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form["nombre"]
    session["numero"] = request.form["numero"]
    session["lugar"] = request.form["lugar"]
    session["comida"] = request.form["comida"]
    session["profesion"] = request.form["profesion"]

    return redirect("/futuro")

@app.route("/futuro")
def futuro():
    return render_template("futuro.html", nombre=session["nombre"], numero=session["numero"], lugar=session["lugar"], comida=session["comida"], profesion=session["profesion"])

if __name__ == "__main__":
    app.run(debug=True)
