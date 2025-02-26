from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_flask():
    return 'Hola desde flask'

@app.route('/ruta')
def ruta():
    return '¿Qué ruta estás buscando?'

@app.route('/bienvenido/python')
def bienvenido():
    return 'Bienvenido a esta ruta Python'

@app.route('/bienvenido/Miyagi')
def bienvenido_miyagi():
    return 'Bienvenido a esta ruta Miyagi'

@app.route('/bienvenido/taquito')
def bienvenido_taquito():
    return 'Bienvenido a esta ruta Taquito'

@app.route('/repite/<repetidor>/<mensaje>')
def repite(repetidor, mensaje):
    return 'Repite despúes de mí: ' + (mensaje + ' ') * int(repetidor)


if __name__ == '__main__':
    app.run(debug=True)