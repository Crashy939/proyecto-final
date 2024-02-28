from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configuración de la conexión a la base de datos de HeidiSQL
concexio = mysql.conector.connect
DB_HOST = '192.168.1.230'
DB_USER = 'raspberry'
DB_PASSWORD = '184620'
DB_NAME = 'escuela1'

# Ruta para mostrar el formulario de ingreso de grupo
@app.route('/agregar_grupo', methods=['GET', 'POST'])
def agregar_grupo():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_grupo = request.form['id_grupo']
        carrera = request.form['carrera']
        semestre = request.form['semestre']
        turno = request.form['turno']

        # Realiza la conexión a la base de datos
        connection = pymysql.connect(host=DB_HOST,
                                     user=DB_USER,
                                     password=DB_PASSWORD,
                                     database=DB_NAME,
                                     cursorclass=pymysql.cursors.DictCursor)

        # Inserta los datos en la base de datos
        with connection.cursor() as cursor:
            sql = "INSERT INTO grupos (id_grupo, carrera, semestre, turno) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_grupo, carrera, semestre, turno))
            connection.commit()

        # Cierra la conexión a la base de datos
        connection.close()

        # Redirige a la página principal después de agregar el grupo
        return redirect(url_for('index'))

    return render_template('agregar_grupo.html')

# Ruta para mostrar el formulario de ingreso de alumno
@app.route('/agregar_alumno', methods=['GET', 'POST'])
def agregar_alumno():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        fecha_nacimiento = request.form['fecha_nacimiento']
        rfid = request.form['rfid']
        carrera = request.form['carrera']
        semestre = request.form['semestre']
        grupo = request.form['grupo']
        correo_electronico = request.form['correo_electronico']
        grupo_id = request.form['grupo_id']

        # Realiza la conexión a la base de datos
        connection = pymysql.connect(host=DB_HOST,
                                     user=DB_USER,
                                     password=DB_PASSWORD,
                                     database=DB_NAME,
                                     cursorclass=pymysql.cursors.DictCursor)

        # Inserta los datos en la base de datos
        with connection.cursor() as cursor:
            sql = "INSERT INTO alumnos (nombre, matricula, apellido_paterno, apellido_materno, fecha_nacimiento, rfid, carrera, semestre, grupo, correo_electronico, grupo_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, matricula, apellido_paterno, apellido_materno, fecha_nacimiento, rfid, carrera, semestre, grupo, correo_electronico, grupo_id))
            connection.commit()

        # Cierra la conexión a la base de datos
        connection.close()

        # Redirige a la página principal después de agregar el alumno
        return redirect(url_for('index'))

    return render_template('agregar_alumno.html')

if __name__ == '__main__':
    app.run(debug=True)
