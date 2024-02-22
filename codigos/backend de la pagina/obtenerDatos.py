 def leerDatos():
    import pymysql
    import datetime

    db = pymysql.connect(host='', user='root', password='password', db='', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"SELECT id, fecha, etc;"
    cur = db.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    db.commit()
    db.close()
    return resultado
