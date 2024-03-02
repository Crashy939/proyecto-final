def conexion(id_alumno):
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.10.123', user='root', password='password', db='AlmacenDeTemperaturas', charset='utf8')
    ahorita = datetime.datetime.now()
   
    db.commit()
    db.close()