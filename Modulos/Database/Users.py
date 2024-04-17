import pymysql
def connect_to_da():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )
    
def VerificaçãoLogin(Email,Senha):
   
    Email = Email.lower()

    connect_to_da()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `email` FROM `newusers` WHERE `email` = '{Email}'"
            cursor.execute(ConsultaSQL)
            result = cursor.fetchone()
            #print(result)
            if result is not None: 
                if Email in result:
                    ConsultaSQL = f"SELECT `email`,`password`,`role`,`name` FROM `newusers` WHERE  `email` = '{Email}' AND BINARY `password` = '{Senha}'"
                    cursor.execute(ConsultaSQL)
                    result = cursor.fetchone()
                    #print(result) 
                    if result is not None: 
                        return True,result
                    else:
                        return False,None
            else:
                return False
    finally:
        connection.close()


def listarusuarios(nome,tipo):
    connect_to_da()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`, `name`, `email`,`created_at`,`role` FROM `newusers` WHERE `name` LIKE '%{nome}%'"
            if tipo is not None:
                ConsultaSQL += f"AND `role` LIKE '%{tipo}%'"

            cursor.execute(ConsultaSQL)
            result = cursor.fetchall()
           

            if result is not None: 
                return result
            else:
                return None
    finally:
        connection.close()         

def listarusuariosporemail(nome,tipo,email):
    connect_to_da()
    email = email.lower()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`, `name`, `email`,`created_at`,`role` FROM `newusers` WHERE `name` LIKE '%{nome}%'"
            if tipo is not None:
                ConsultaSQL += f"AND `role` LIKE '%{tipo}%'"
            
            ConsultaSQL += f"AND `email` = '{email}'"
            
            cursor.execute(ConsultaSQL)
            result = cursor.fetchall()
           

            if result is not None: 
                return result
            else:
                return None
    finally:
        connection.close()           