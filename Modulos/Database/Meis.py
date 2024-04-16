import pymysql
def connect_to_da():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )
def getMeilist_complete():
    # Conecta ao banco de dados
    
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`,`nome`,`identificacao`,`situacao` FROM `meis`"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()

                
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                # Verifica o último elemento  e converte para "ATIVO" ou "INATIVO"
                if item[-1] == 1:
                    estado = "ATIVO"
                else:
                    estado = "INATIVO"
                
                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], item[2], estado)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()


def getMEIlist_byfilter(nome_empresa_p,nome,identificacao_p,identificacao,ativo_p,ativo):
    # Conecta ao banco de dados
    
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`,`nome`,`identificacao`,`situacao` FROM `meis` WHERE `{nome_empresa_p}` LIKE '%{nome}%'"
            if identificacao_p and identificacao:
                ConsultaSQL += f" AND `{identificacao_p}` LIKE '%{identificacao}%'"
            if ativo_p and ativo is not None:
                ConsultaSQL += f" AND `{ativo_p}` LIKE '%{ativo}%'"
            
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()

                
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                # Verifica o último elemento  e converte para "ATIVO" ou "INATIVO"
                if item[-1] == 1:
                    estado = "ATIVO"
                else:
                    estado = "INATIVO"
                
                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], item[2], estado)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()
