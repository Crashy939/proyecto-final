import mysql.connector
from datetime import datetime, timedelta
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

conexion = mysql.connector.connect(
    host="192.168.1.77",
    user="raspberry",
    password="184620",
    database="escuela"
)
cursor = conexion.cursor()

lector_rfid = SimpleMFRC522()

def tomar_asistencia():
    try:
        print("Esperando a que se escanee una tarjeta RFID...")
        id_rfid, _ = lector_rfid.read()
        print("Tarjeta RFID escaneada. ID:", id_rfid)

        # Obtener id alumno
        consulta_id_alumno = "SELECT id_alumno FROM alumnos WHERE rfid = %s"
        cursor.execute(consulta_id_alumno, (id_rfid,))
        resultado = cursor.fetchone()

        if resultado:
            id_alumno = resultado[0]
            print("ID del alumno:", id_alumno)

            # Obtener el ID del grupo del alumno
            consulta_grupo_alumno = "SELECT grupo FROM alumnos WHERE id_alumno = %s"
            cursor.execute(consulta_grupo_alumno, (id_alumno,))
            grupo_id = cursor.fetchone()[0]
            print("ID del grupo del alumno:", grupo_id)

            # Obtener la próxima clase del grupo del alumno
            dia_semana_actual = datetime.now().strftime('%A')
            hora_actual = datetime.now().strftime('%H:%M:%S')
            consulta_proxima_clase = "SELECT id_horario, hora_inicio, tolerancia_antes, tolerancia_despues FROM horarios WHERE grupo_id = %s AND dia_semana = DAYNAME(%s) AND hora_inicio > %s ORDER BY hora_inicio ASC LIMIT 1"
            print(grupo_id, dia_semana_actual, hora_actual)
            cursor.execute(consulta_proxima_clase, (grupo_id, dia_semana_actual, hora_actual))
            proxima_clase = cursor.fetchone()
            print(datetime.now().strftime('%H:%M'))
            print(proxima_clase)
            if proxima_clase :
                id_horario, hora_inicio, tolerancia_antes, tolerancia_despues = proxima_clase
                hora_inicio = hora_inicio.strftime('%H:%M:%S')
                tolerancia_antes = tolerancia_antes.strftime('%H:%M:%S')
                tolerancia_despues = tolerancia_despues.strftime('%H:%M:%S')

                print("ID del horario de la próxima clase:", id_horario)
                print("Hora de inicio de la próxima clase:", hora_inicio)
                print("Tolerancia antes de la clase:", tolerancia_antes)
                print("Tolerancia después de la clase:", tolerancia_despues)

                hora_inicio_tolerancia_antes = (datetime.strptime(hora_inicio, '%H:%M:%S') - timedelta(hours=tolerancia_antes.hour, minutes=tolerancia_antes.minute)).strftime('%H:%M:%S')
                hora_inicio_tolerancia_despues = (datetime.strptime(hora_inicio, '%H:%M:%S') + timedelta(hours=tolerancia_despues.hour, minutes=tolerancia_despues.minute)).strftime('%H:%M:%S')

                print("Hora de inicio con tolerancia antes:", hora_inicio_tolerancia_antes)
                print("Hora de inicio con tolerancia después:", hora_inicio_tolerancia_despues)

                if hora_inicio_tolerancia_antes <= hora_actual <= hora_inicio_tolerancia_despues:
                    # El alumno llegó a tiempo, registra la asistencia
                    fecha_actual = datetime.now().strftime('%Y-%m-%d')
                    hora_actual = datetime.now().strftime('%H:%M:%S')

                    # Insertar registro de asistencia
                    consulta_insertar_asistencia = "INSERT INTO asistencia (clase_id, grupo_id, alumno_id, fecha, hora, asistio) VALUES (%s, %s, %s, %s, %s, %s)"
                    valores_asistencia = (id_horario, grupo_id, id_alumno, fecha_actual, hora_actual, True)
                    cursor.execute(consulta_insertar_asistencia, valores_asistencia)
                    conexion.commit()
                    print("Asistencia registrada exitosamente.")
                else:
                    print("El alumno llegó fuera del tiempo de tolerancia para esta clase.")
            else:
                print("No se encontraron clases próximas para el grupo del alumno.")
        else:
            print("Tarjeta RFID no asociada a ningún alumno.")
    finally:
        cursor.close()
        conexion.close()
        GPIO.cleanup()  # Limpieza de GPIO al finalizar el script

if __name__ == "__main__":
    tomar_asistencia()
