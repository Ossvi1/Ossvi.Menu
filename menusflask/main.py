from flask import Flask, render_template

app = Flask(__name__)

menu = {
    "Inicio": "/",
    "Oferta Educativa": {
        "Ingenierías": {
            "Ingeniería Ambiental": "/ingenieria/ambiental",
            "Ingeniería Electromecánica": "/ingenieria/electromecanica",
            "Ingeniería Electrónica": "/ingenieria/electronica",
            "Ingeniería Industrial": "/ingenieria/industrial",
            "Ingeniería Química": "/ingenieria/quimica",
            "Ingeniería en Gestión Empresarial": "/ingenieria/gestion",
            "Ingeniería en Sistemas Computacionales": "/ingenieria/sistemas"
        },
        "Posgrado": {
            "Maestría en Ingeniería Electrónica": "/posgrado/electronica"
        }
    },
    "Contacto": "/contacto"
}

@app.route("/")
def inicio():
    return render_template("menu.html", menu=menu, title="Inicio")

@app.route("/contacto")
def contacto():
    return render_template("menu.html", menu=menu, title="Contacto")

@app.route("/ingenieria/<nombre>")
def ingenieria(nombre):
    titulos = {
        "ambiental": "Ingeniería Ambiental",
        "electromecanica": "Ingeniería Electromecánica",
        "electronica": "Ingeniería Electrónica",
        "industrial": "Ingeniería Industrial",
        "quimica": "Ingeniería Química",
        "gestion": "Ingeniería en Gestión Empresarial",
        "sistemas": "Ingeniería en Sistemas Computacionales"
    }
    return render_template("menu.html", menu=menu, title=titulos.get(nombre, "Ingeniería"))

@app.route("/posgrado/electronica")
def posgrado_electronica():
    return render_template("menu.html", menu=menu, title="Maestría en Ingeniería Electrónica")

if __name__ == "__main__":
    app.run(debug=True)
