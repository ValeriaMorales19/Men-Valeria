from flask import Flask, render_template
import webbrowser
import threading
import time

app = Flask(__name__)

menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrado": {}
    },
    "Contacto": {}
}

@app.route('/')
def index():
    return render_template('menu.html', menu=menu)

def abrir_navegador():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Thread(target=abrir_navegador).start()
    app.run(debug=True) 