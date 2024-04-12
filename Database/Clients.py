import pymysql

def getclientlist_complete():
    # Conecta ao banco de dados
    connection = pymysql.connect(
        host='mysql02-farm10.kinghost.net',
        user='datavixsolucao',
        password='R4QePW2ze9Hpa6F',
        database='datavixsolucao'
    )

    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT * FROM `clients`"
            cursor.execute(ConsultaSQL)
            result = cursor.fetchone()
            #print(result)
          
            if result is not None: 
                return result
            else:
                return None

    finally:
        connection.close()


