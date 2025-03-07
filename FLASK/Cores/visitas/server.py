from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def visitas():
    session['visitas'] = session.get('visitas', 0) + 1
    return f"Visitas: {session['visitas']}"

@app.route('/incrementar_2')
def incrementar_2():
    session['visitas'] = session.get('visitas', 0) + 2
    return render_template('index.html', visitas=session['visitas'])

@app.route('/destruir_sesion')
def destruir_sesion():
    session.pop('visitas', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)