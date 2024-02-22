from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    import obtenerDatos
    resultado = obtenerDatos.leerDatos()
    return render_template('reporte.html', resultado = resultado)

if __name__ == '__main__':
    app.run (debug=True, port=80,host='0.0.0.0')