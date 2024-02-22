def conexion(id_alumno):
    import pymysql
    import datetime

    db = pymysql.connect(host='', user='root', password='password', db='bd', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"INSERT INTO tabla (campos,campos,campos) VALUES ('{ahorita}', {registro}, {registro});"
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()