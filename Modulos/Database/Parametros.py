import pymysql
from datetime import date,datetime

def connect_to_db():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )

   
def pegar_parametro(parametro):
    # Conecta ao banco de dados
    
    connect_to_db()
    
    try:	

        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `valor` FROM `pyparameter` WHERE `parametro`= '{parametro}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()

            return results[0]
 

    finally:
        connection.close()
