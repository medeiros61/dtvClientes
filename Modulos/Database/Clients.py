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
    
def getclientlist_complete():
    # Conecta ao banco de dados
    
    connect_to_db()
    
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

   
def getclientComents(id):
    # Conecta ao banco de dados
    
    connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `created_at`,`observacao`,`user_id` FROM `events` WHERE `client_id`= {id}"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            
            nova_lista = []  # Lista para armazenar os itens convertidos

            for item in results:
                id_user = item[2]
                ConsultaSQL = f"SELECT `name` FROM `users` WHERE `id`= {id_user}"
                cursor.execute(ConsultaSQL)
                usuario = cursor.fetchone()
                usuario = list(usuario)

                # Cria uma nova tupla com o item convertido e adiciona à nova lista
                novoitemlistagem = (item[0], item[1], usuario[0])
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                return nova_lista
            else:
                return None

    finally:
        connection.close()

def RegisterclientComents(Clientid,Mensagem,userid,agora):
    # Conecta ao banco de dados
    
    connect_to_db()

    try:
      

        
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id` FROM `users` WHERE `email`= '{userid}'"
            cursor.execute(ConsultaSQL)
            usuario = cursor.fetchone()

            ConsultaSQL = f"INSERT INTO `events` (`client_id`,`observacao`,`user_id`,`created_at`) VALUES ({Clientid},'{Mensagem}',{usuario[0]},'{agora}')"
            cursor.execute(ConsultaSQL)
            connection.commit()  
    finally:
        connection.close()


def getclientlist_byfilter(nome_empresa_p,nome,uf_p,uf,ativo_p,ativo):
    # Conecta ao banco de dados
    
    connect_to_db()
    
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
    
    connect_to_db()
    
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
   
def getassocietes_toEdit(IDempresa):
    

        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `nome`,`cpf`,`porcentagem` FROM `associates` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results
   
def getLivro_Entradas_toEdit(IDempresa):
    
      with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `numero`,`ano` FROM `livro_entradas` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results
   
def getLivro_Inventarios_toEdit(IDempresa):
    

      with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `numero`,`ano` FROM `livro_inventarios` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results

def getLivroECD_toEdit(IDempresa):
    
      with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `numero`,`ano` FROM `livro_ecds` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results
        
def getLivroECF_toEdit(IDempresa):
    

        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `numero`,`ano` FROM `livro_ecfs` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results

def getsyndicates_toEdit(IDempresa):
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `nome`,`data_base`,`periodo_vigencia_ultima_cct`,`site_cct` FROM `syndicates` WHERE `client_id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results
    
def getclientdata_toEdit(IDempresa):
    # Conecta ao banco de dados
    
    connect_to_db()
    data_quary = [
        "id",
        "nome_empresa",
        "cnpj",
        "uf",
        "municipio",
        "atividade",
        "data_abertura",
        "ativo",
        "formas_tributacao",
        "anexo_simples_nacional",
        "folha_pagamento",
        "responsavel_contabil",
        "responsavel_fiscal",
        "responsavel_societario",
        "responsavel_dp",
        "domicilio_eletronico",
        "email",
        "nome_representante",
        "cpf_representante_legal",
        "data_nascimento",
        "contabilidade_finalizada",
        "certificado_digital",
        "senha_certificado",
        "data_vencimento_certificado",
        "codigo_ecac",
        "senha_ecac",
        "codigo_simples",
        "estado",
        "inscricao_estadual",
        "credenciamento_nfe",
        "numero_csc",
        "site_caixa_postal",
        "inscricao_municipal",
        "site",
        "login",
        "senha",
        "alvara_funcionamento",
        "data_vencimento_alvara_funcionamento",
        "alvara_sanitario",
        "data_vencimento_alvara_sanitario",
        "licenca_ambiental",
        "data_vencimento_licenca_ambiental",
        "bombeiros",
        "data_vencimento_bombeiros",
        "ultima_alteracao_contratual",
        "numero_alteracao_contratual",
        "observacoes_gerais_societario",
        "folha_pagto",
        "quantidade_funcionarios",
        "prolabore",
        "quantidade_socios",
        "esocial_usuario",
        "esocial_senha",
        "esocial_codigo_acesso",
        "fap_usuario",
        "fap_senha",
        "empregador_web_usuario",
        "empregador_web_senha",
        "sistema_bpo",
        "site_bpo",
        "usuario_bpo",
        "senha_simples_bpo",
        "banco1",
        "banco2",
        "tipo_bpo",
        "observacoes_gerais_bpo",
        "created_at",
        "updated_at",
        "link_whatsapp",
        "municipal_observacoes",
        "municipal_demais_senhas",
        "municipal_senha_abertura_processos",
        "dpto_pessoal_sindicalizada",
        "dpto_pessoal_login",
        "dpto_pessoal_senha"
    ]
  
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT "
            for index,item in enumerate(data_quary):
                ConsultaSQL += f'`{item}`'

                if index < len(data_quary) - 1:
                    ConsultaSQL += ","

            ConsultaSQL += f"FROM `clients` WHERE `id` = '{IDempresa}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()
            #Usando fetchmany para buscar 3 linhas de resultados
            #results = cursor.fetchmany(size=3)
            #for result in results:
            #    id,nome_empresa,uf,municipio,ativo = result
            #    print(result)

          
            # Convertendo a tupla em lista para poder modificar valores
            results_list = list(results)

            # results_list[7] representa a coluna "ativo" na consulta SQL
            botões_yesornot = [7,21,27,29,36,38,40,42,47,49,72]
            for item in botões_yesornot:
                if results_list[item] == 1:
                    results_list[item] = "SIM"
                else:
                    results_list[item] = "NÃO"

            botões_yesornot = [10,15]
            for item in botões_yesornot:
                if results_list[item] == '1':
                    results_list[item] = "SIM"
                else:
                    results_list[item] = "NÃO"

            if results_list[9]:
                    valor = results_list[9]
                    valor = valor.replace("[","").replace("]","")
                    results_list[9] = valor
            
            # Convertendo de volta para tupla, se necessário
            results = tuple(results_list)

            nova_lista = []  # Lista para armazenar os itens convertidos
            n=0
            Listadeidentificação=[]
            for item in results_list:
                
                identificador = f"""{n}:{item} - {data_quary[n]}"""
                #print(identificador)
                n += 1
                Listadeidentificação.append(identificador)
                if item == None:
                    item="N/A"
                    
                if item == '':
                    item="N/A"       
                #try:
                if isinstance(item, date):    
                        # Formatando a data para "DD/MM/AAAA"
                        data_formatada = item.strftime("%d/%m/%Y") # Convertendo para datetime

                        #print(data_formatada)  # Saída
                        item = data_formatada
                #except Exception:
                #    pass

                novoitemlistagem = (item)
                nova_lista.append(novoitemlistagem)
        
            if nova_lista is not None: 
                socios = getassocietes_toEdit(IDempresa)
                sindicatos = getsyndicates_toEdit(IDempresa)
                livroECD = getLivroECD_toEdit(IDempresa)
                LivroECF=getLivroECF_toEdit(IDempresa)
                LivroEntradas = getLivro_Entradas_toEdit(IDempresa)
                Livroinvetario = getLivro_Inventarios_toEdit(IDempresa)
                return nova_lista,Listadeidentificação,data_quary,socios,sindicatos,livroECD,LivroECF,LivroEntradas,Livroinvetario
            else:
                return None,None,None,None,None,None,None,None,None

    finally:
        connection.close() 

def getclientdata_all(nome_empresa_p,nome,uf_p,uf,ativo_p,ativo):
    # Conecta ao banco de dados
    
    connect_to_db()
    data_quary = [
        "id",
        "nome_empresa",
        "cnpj",
        "uf",
        "municipio",
        "atividade",
        "data_abertura",
        "ativo",
        "formas_tributacao",
        "anexo_simples_nacional",
        "folha_pagamento",
        "responsavel_contabil",
        "responsavel_fiscal",
        "responsavel_societario",
        "responsavel_dp",
        "domicilio_eletronico",
        "email",
        "nome_representante",
        "cpf_representante_legal",
        "data_nascimento",
        "contabilidade_finalizada",
        "certificado_digital",
        "senha_certificado",
        "data_vencimento_certificado",
        "codigo_ecac",
        "senha_ecac",
        "codigo_simples",
        "estado",
        "inscricao_estadual",
        "credenciamento_nfe",
        "numero_csc",
        "site_caixa_postal",
        "inscricao_municipal",
        "site",
        "login",
        "senha",
        "alvara_funcionamento",
        "data_vencimento_alvara_funcionamento",
        "alvara_sanitario",
        "data_vencimento_alvara_sanitario",
        "licenca_ambiental",
        "data_vencimento_licenca_ambiental",
        "bombeiros",
        "data_vencimento_bombeiros",
        "ultima_alteracao_contratual",
        "numero_alteracao_contratual",
        "observacoes_gerais_societario",
        "folha_pagto",
        "quantidade_funcionarios",
        "prolabore",
        "quantidade_socios",
        "esocial_usuario",
        "esocial_senha",
        "esocial_codigo_acesso",
        "fap_usuario",
        "fap_senha",
        "empregador_web_usuario",
        "empregador_web_senha",
        "sistema_bpo",
        "site_bpo",
        "usuario_bpo",
        "senha_simples_bpo",
        "banco1",
        "banco2",
        "tipo_bpo",
        "observacoes_gerais_bpo",
        "created_at",
        "updated_at",
        "link_whatsapp",
        "municipal_observacoes",
        "municipal_demais_senhas",
        "municipal_senha_abertura_processos",
        "dpto_pessoal_sindicalizada",
        "dpto_pessoal_login",
        "dpto_pessoal_senha"
    ]
  
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT "
            for index,item in enumerate(data_quary):
                ConsultaSQL += f'`{item}`'

                if index < len(data_quary) - 1:
                    ConsultaSQL += ","
                
            ConsultaSQL += f"FROM `clients`"

            ConsultaSQL += f" WHERE `{nome_empresa_p}` LIKE '%{nome}%'"
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
            nova_listacompleta = []
            for cliente in results:
            # Convertendo a tupla em lista para poder modificar valores
                cliente = list(cliente)

                # results_list[7] representa a coluna "ativo" na consulta SQL
                botões_yesornot = [7,10,15,21,27,29,39,41,42,43,47,49]
                for item in botões_yesornot:
                    if cliente[item] == 1:
                        cliente[item] = "SIM"
                    else:
                        cliente[item] = "NÃO"

               
                
                # Convertendo de volta para tupla, se necessário
                resultscliente = tuple(cliente)

                nova_lista = []  # Lista para armazenar os itens convertidos
                for item in resultscliente:
                    
                    
                    if item == None:
                        item="N/A"
                        
                    if item == '':
                        item="N/A"       
                    #try:
                    if isinstance(item, date):    
                            # Formatando a data para "DD/MM/AAAA"
                            data_formatada = item.strftime("%d/%m/%Y") # Convertendo para datetime

                            #print(data_formatada)  # Saída
                            item = data_formatada
                    #except Exception:
                    #    pass

                    novoitemlistagem = (item)
                    nova_lista.append(novoitemlistagem)
                nova_listacompleta.append(nova_lista)


            if nova_listacompleta is not None: 
                return nova_listacompleta
            else:
                return None,None

    finally:
        connection.close() 

def gerartexto():
    Listadedados, identificadores, qr = getclientdata_toEdit(14)
        
    Variaveis= [
        "NumeroID",
        "entry_Nome_empresa",
        "entry_CNPJ",
        "entry_Estado",
        "entry_Municpio",
        "entry_Atividade",
        "entry_Data_abertura_",
        "entry_Ativo",
        "entry_Link_WhatsApp",
        "entry_Formas_de_tributao",
        "entry_Anexo_simples_nacional",
        "entry_Folha_de_pagamento",
        "entry_Responsvel_contabil",
        "entry_Responsvel_fiscal",
        "entry_Responsvel_societrio",
        "entry_Responsvel_DP",
        "entry_Domiclio_eletrnico",
        "entry_Email",
        "entry_Nome_representante",
        "entry_CPF_representante_legal",
        "entry_Data_de_nascimento_",
        "entry_Contabilidade_finalizada_",
        "entry_Certificado_digital",
        "entry_Senha_certificado",
        "entry_Data_de_vencimento_",
        "entry_Cdigo_e_cac",
        "entry_Senha_EAC",
        "entry_Cdigo_Simples",
        "entry_Nmero_de_livros_ECD",
        "entry_Ano_Nmero_de_livros_ECD",
        "entry_Nmero_de_livros_ECF",
        "entry_Ano_Nmero_de_livros_ECF",
        "entry_UF",
        "entry_Inscrio_estadual",
        "entry_Credenciamento_NFE",
        "entry_Nmero_CSC",
        "entry_Site_caixa_postal",
        "entry_Livros_Fiscais_Entrada_Ano_Nmero",
        "entry_Livros_Fiscais_Inventrio_Ano_Nmero",
        "entry_Inscrio_municipal",
        "entry_Site",
        "entry_Login",
        "entry_Senha",
        "entry_Demais_senhas",
        "entry_Senha_Abertura_Processos",
        "entry_Observaes",
        "entry_Alvara_de_funcionamento",
        "entry_Data_vencimento_",
        "entry_Alvara_sanitrio",
        "entry_Licenca_ambiental",
        "entry_Bombeiros",
        "entry_ltima_alterao_contratual_",
        "entry_Nmero_alterao_contratual",
        "entry_Observaes_gerais",
        "entry_Folha_de_pagto",
        "entry_Quantidade_de_funcionrios",
        "entry_Prolabore",
        "entry_Quantidade_de_scios",
        "entry_Esocial_usurio",
        "entry_Esocial_senha",
        "entry_Esocial_cdigo_de_acesso",
        "entry_FAP_usurio",
        "entry_FAP_senha",
        "entry_Empregador_WEB_usurio",
        "entry_Empregador_WEB_senha",
        "entry_Sistema",
        "entry_Site",
        "entry_Usurio",
        "entry_Senha_simples",
        "entry_Banco_1",
        "entry_Banco_2",
        "entry_Tipo_de_BPO"

        ]

    for i, item in enumerate(Variaveis):
        num=i
        if i >8:
            num -=1
        if i >26:
            num -=6    
        if i==8 or (i>26 and i<32):
            print(f"""{item}.insert(0,"")""")
            #print(f"""{item}=""")
        else:    
            print(f"""{item}.insert(0,Listadedados[{num}]) # Campo {qr[num]} do banco de dados""")#
            
            #print(f"""{item}={identificadores[num]}""")#
        

        #print(f"""{item}.configure = {Listadedados[i]} #{identificadores[i]}""")

def Query_Save_Data(Query):
    
    connect_to_db() 

    try:
        with connection.cursor() as cursor:
            ConsultaSQL = Query
            cursor.execute(ConsultaSQL)
            connection.commit()       
    finally:
        connection.close()
   

def Query_remove_Data(Query):
    
    connect_to_db() 

    try:
        with connection.cursor() as cursor:
            ConsultaSQL = Query
            cursor.execute(ConsultaSQL)
            connection.commit()       
    finally:
        connection.close()
      