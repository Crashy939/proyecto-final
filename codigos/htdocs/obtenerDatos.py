def leerDatos():
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.10.123', user='root', password='password', db='escuela', charset='utf8')
    ahora= datetime.datetime.now()
    sql = f"SELECT * from alumnos;"
    cur = db.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    db.commit()
    db.close()
    return resultado