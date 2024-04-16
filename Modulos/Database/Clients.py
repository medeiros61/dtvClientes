import pymysql
def connect_to_da():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )
def getclientlist_complete():
    # Conecta ao banco de dados
    
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`,`nome_empresa`,`uf`,`municipio`,`ativo` FROM `clients`"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            #Usando fetchmany para buscar 3 linhas de resultados
            #results = cursor.fetchmany(size=3)
            #for result in results:
            #    id,nome_empresa,uf,municipio,ativo = result
            #    print(result)
                
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                # Verifica o último elemento  e converte para "ATIVO" ou "INATIVO"
                if item[-1] == 1:
                    estado = "ATIVO"
                else:
                    estado = "INATIVO"
                
                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], item[2], item[3], estado)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()


def getclientlist_byfilter(nome_empresa_p,nome,uf_p,uf,ativo_p,ativo):
    # Conecta ao banco de dados
    
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`, `nome_empresa`, `uf`, `municipio`, `ativo` FROM `clients` WHERE `{nome_empresa_p}` LIKE '%{nome}%'"
            if uf_p and uf:
                ConsultaSQL += f" AND `{uf_p}` LIKE '%{uf}%'"
            if ativo_p and ativo is not None:
                ConsultaSQL += f" AND `{ativo_p}` LIKE '%{ativo}%'"
            
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            #Usando fetchmany para buscar 3 linhas de resultados
            #results = cursor.fetchmany(size=3)
            #for result in results:
            #    id,nome_empresa,uf,municipio,ativo = result
            #    print(result)
                
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                # Verifica o último elemento  e converte para "ATIVO" ou "INATIVO"
                if item[-1] == 1:
                    estado = "ATIVO"
                else:
                    estado = "INATIVO"
                
                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], item[2], item[3], estado)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()


def getmunicipioslist_complete():
    # Conecta ao banco de dados
    
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `municipio` FROM `clients`"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            #Usando fetchmany para buscar 3 linhas de resultados
            #results = cursor.fetchmany(size=3)
            #for result in results:
            #    id,nome_empresa,uf,municipio,ativo = result
            #    print(result)
                
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                # Verifica o último elemento  e converte para "ATIVO" ou "INATIVO"
                if item[-1] == 1:
                    estado = "ATIVO"
                else:
                    estado = "INATIVO"
                
                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], item[2], item[3], estado)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()