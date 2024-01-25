import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
from datetime import datetime

# Configura la conexión con la base de datos
db_connection = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)
cursor = db_connection.cursor()

# Configura el lector RFID
reader = SimpleMFRC522()

try:
    while True:
        print("Esperando tarjeta...")
        id, text = reader.read()
        print(f"Tarjeta detectada: {id}")

        # Registra la asistencia en la base de datos
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO asistencias (id_estudiante, fecha) VALUES (%s, %s)"
        values = (id, current_time)

        cursor.execute(query, values)
        db_connection.commit()

        print("Asistencia registrada con éxito.")

finally:
    GPIO.cleanup()
    cursor.close()
    db_connection.close()
