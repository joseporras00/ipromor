import MySQLdb as sql
import pandas as pd

con = sql.connect(host='localhost', user= '5q8jDuKCGP', passwd='WxAvWTalRm', db='5q8jDuKCGP')

sql = "SELECT idRegistro, cliente, maquina FROM usuarios"

df = pd.read_sql_query(sql, con=con)

