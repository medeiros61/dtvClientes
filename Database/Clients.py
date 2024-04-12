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
            ConsultaSQL = f"SELECT `id`,`nome_empresa`,`uf`,`municipio`,`ativo` FROM `clients`"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            #Usando fetchmany para buscar 3 linhas de resultados
            #results = cursor.fetchmany(size=3)
            #for result in results:
            #    id,nome_empresa,uf,municipio,ativo = result
            #    print(result)
                
        
        
            if results is not None: 
                return results
            else:
                return None

    finally:
        connection.close()

getclientlist_complete()
