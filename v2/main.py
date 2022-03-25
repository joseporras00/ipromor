import pyodbc
from datetime import datetime

direccion_servidor = 'ipromorserver.database.windows.net'
nombre_bd = 'ipromor'
nombre_usuario = 'prueba'
password = 'IM2020im2020'
try:
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

cursor = con.cursor()

#SELECT
#cursor.execute("SELECT * from ipromor")
#row = cursor.fetchone()
#while row:
#    print(row[1])
#    row = cursor.fetchone()

#INSERT
#now = datetime.now()
#dato = ['ferrari','motor',now,1,100,'1 productos correctos']
#cursor.execute("INSERT INTO ipromor(cliente,maquina,fechahora,tipo,estado,descripcion) VALUES(?,?,?,?,?,?)",dato[0],dato[1],dato[2],dato[3],dato[4],dato[5])
#con.commit()

#INSERT CSV
#import csv
#with open('prueba.csv') as csvfile:
#    reader = csv.reader(csvfile, delimiter=';')
#    for row in reader:
#        dato = [row[0],row[1],row[2],row[3],row[4],row[5]]
#
#        cursor.execute("INSERT INTO ipromor(cliente,maquina,fechahora,tipo,estado,descripcion) VALUES(?,?,?,?,?,?)",
#                       dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
#        con.commit()

#LEYENDO CSV DEL SERVIDOR FTP
import ftplib
ftp = ftplib.FTP("ftp.ipromor.com")
ftp.login("iiot@ipromor.com", "9G6lYkGZ0W5w")



ftp.cwd('/')
ftp.retrbinary("RETR " + 'prueba.csv', open('prueba.csv', 'wb').write)
ftp.quit()

import csv
with open('prueba.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:

        cursor.execute('SELECT * from ipromor WHERE idRegistro=?', row[0])
        data=cursor.fetchone()

        if data is None:
            dato = [row[0],row[1],row[2],row[3],row[4],row[5],row[6]]
            cursor.execute("INSERT INTO ipromor(cliente,maquina,fechahora,tipo,estado,descripcion) VALUES(?,?,?,?,?,?)",
                        dato[1], dato[2], dato[3], dato[4], dato[5], dato[6])
            con.commit()
con.close()

