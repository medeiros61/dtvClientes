import pymysql
def connect_to_da():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )

def VerificaçãoEmail_existe(Email):
   
    Email = Email.lower()

    connect_to_da()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `email` FROM `pyusers` WHERE `email` = '{Email}'"
            cursor.execute(ConsultaSQL)
            result = cursor.fetchone()
            if result is not None: 
                return True
            else:
                return False

    finally:
        connection.close()

def Alterasenha(Email,novasenha):
   
    Email = Email.lower()

    connect_to_da()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"UPDATE `pyusers` SET password = '{novasenha}' WHERE `email` = '{Email}'"
            cursor.execute(ConsultaSQL)
            connection.commit()       

    finally:
        connection.close()


def VerificaçãoLogin(Email,Senha):
   
    Email = Email.lower()

    connect_to_da()
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `email` FROM `pyusers` WHERE `email` = '{Email}'"
            cursor.execute(ConsultaSQL)
            result = cursor.fetchone()
            #print(result)
            if result is not None: 
                if Email in result:
                    ConsultaSQL = f"SELECT `email`,`password`,`role`,`name` FROM `pyusers` WHERE  `email` = '{Email}' AND BINARY `password` = '{Senha}'"
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
            ConsultaSQL = f"SELECT `id`, `name`, `email`,`created_at`,`role` FROM `pyusers` WHERE `name` LIKE '%{nome}%'"
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
            ConsultaSQL = f"SELECT `id`, `name`, `email`,`created_at`,`role` FROM `pyusers` WHERE `name` LIKE '%{nome}%'"
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