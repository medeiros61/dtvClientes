import pymysql

def VerificaçãoLogin(Email,Senha):
    # Conecta ao banco de dados
    connection = pymysql.connect(
        host='mysql02-farm10.kinghost.net',
        user='datavixsolucao',
        password='R4QePW2ze9Hpa6F',
        database='datavixsolucao'
    )

    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `email` FROM `newusers` WHERE `email` = '{Email}'"
            cursor.execute(ConsultaSQL)
            result = cursor.fetchone()
            #print(result)
            if result is not None: 
                if Email in result:
                    ConsultaSQL = f"SELECT `email`,`password` FROM `newusers` WHERE  `email` = '{Email}' AND BINARY `password` = '{Senha}'"
                    cursor.execute(ConsultaSQL)
                    result = cursor.fetchone()
                    #print(result) 
                    if result is not None: 
                        return True
                    else:
                        return False
            else:
                return False
    finally:
        connection.close()


