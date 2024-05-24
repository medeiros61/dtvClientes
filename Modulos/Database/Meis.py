import pymysql
from datetime import date

def connect_to_db():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )
def getMeilist_complete():
    # Conecta ao banco de dados
    
    connect_to_db()
    
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
    
    connect_to_db()
    
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


def getMEIdata_all(nome_empresa_p,nome,identificacao_p,identificacao,ativo_p,ativo):
    # Conecta ao banco de dados
    
    connect_to_db()
    data_quary = [
    "id",
    "mei_id",
    "situacao",
    "nome",
    "identificacao",
    "cnpj",
    "tributacao",
    "data_abertura",
    "prefeitura",
    "login",
    "senha",
    "pendencia_recolhimentos",
    "entrega_das_mensal",
    "pendencias",
    "email",
    "pendencia",
    "observacoes",
    "cpf",
    "codigo_acesso",
    "senha_gov",
    "nivel_gov",
    "endereco",
    "inscricao_estadual",
    "inscricao_municipal",
    "certificado_digital",
    "modelo_datavix",
    "homologado_sindicato",
    "vencimento",
    "created_at",
    "updated_at"
    ]
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT "
            for index,item in enumerate(data_quary):
                ConsultaSQL += f'`{item}`'

                if index < len(data_quary) - 1:
                    ConsultaSQL += ","
                    
            ConsultaSQL += f"FROM `meis` WHERE `{nome_empresa_p}` LIKE '%{nome}%'"
            if identificacao_p and identificacao:
                ConsultaSQL += f" AND `{identificacao_p}` LIKE '%{identificacao}%'"
            if ativo_p and ativo is not None:
                ConsultaSQL += f" AND `{ativo_p}` LIKE '%{ativo}%'"
            
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            
            nova_listacompleta = []
            for cliente in results:

                # Convertendo a tupla em lista para poder modificar valores
                cliente = list(cliente)

                # cliente[7] representa a coluna "ativo" na consulta SQL
                botões_yesornot = [2,24]
                for item in botões_yesornot:
                    if cliente[item] == 1:
                        cliente[item] = "SIM"
                    else:
                        cliente[item] = "NÃO"

        
                
                
                # Convertendo de volta para tupla, se necessário
                resultscliente = tuple(cliente)

                nova_lista = []  # Lista para armazenar os itens convertidos
                n=0
                Listadeidentificação=[]
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
                return None

    finally:
        connection.close()


def GetnameMEI(IDdomei):
    # Conecta ao banco de dados
    
    connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `nome` FROM `meis` WHERE `id` = '{IDdomei}'"
 
            
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()

        
            if results is not None: 
                return results
            else:
                return None

    finally:
        connection.close()

def getParceiras_toEdit(IDempresaContratante):
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `id`,`nome`,`pendencias`,`situacao` FROM `meis` WHERE `mei_id` = '{IDempresaContratante}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results

def getLista_De_DASN_toEdit(IDempresaContratante):
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `ano`,`faturamento`,`observacao` FROM `das` WHERE `mei_id` = '{IDempresaContratante}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results

def getLista_De_Servicos_toEdit(Idmei):
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `tipo`,`servico`,`salao`,`parceiro` FROM `py_meis_servicos` WHERE `mei_id` = '{Idmei}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()
            return results
                
def getmeidata_toEdit(IDempresa):
    # Conecta ao banco de dados
    
    connect_to_db()
    data_quary = [
    "id",
    "mei_id",
    "situacao",
    "nome",
    "identificacao",
    "cnpj",
    "tributacao",
    "data_abertura",
    "prefeitura",
    "login",
    "senha",
    "pendencia_recolhimentos",
    "entrega_das_mensal",
    "pendencias",
    "email",
    "pendencia",
    "observacoes",
    "cpf",
    "codigo_acesso",
    "senha_gov",
    "nivel_gov",
    "endereco",
    "inscricao_estadual",
    "inscricao_municipal",
    "certificado_digital",
    "modelo_datavix",
    "homologado_sindicato",
    "vencimento",
    "created_at",
    "updated_at"
    ]
  
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT "
            for index,item in enumerate(data_quary):
                ConsultaSQL += f'`{item}`'

                if index < len(data_quary) - 1:
                    ConsultaSQL += ","

            ConsultaSQL += f"FROM `meis` WHERE `id` = '{IDempresa}'"
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
            botões_yesornot = [2,24]
            for item in botões_yesornot:
                if results_list[item] == 1:
                    results_list[item] = "SIM"
                else:
                    results_list[item] = "NÃO"

      
            
            
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
                meis = getParceiras_toEdit(nova_lista[0]) 
                Lista_de_DAS = getLista_De_DASN_toEdit(nova_lista[0])
                Lista_de_Servicos = getLista_De_Servicos_toEdit(nova_lista[0])
                DadosComplemtares = Novosdados_ParaContrato(nova_lista[0])
                ListaDadosContrato = []  # Lista para armazenar os itens convertidos
                for item in DadosComplemtares:
    
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
                    ListaDadosContrato.append(novoitemlistagem)
        
                
                
                return nova_lista,Listadeidentificação,data_quary,meis,Lista_de_DAS,Lista_de_Servicos,ListaDadosContrato
            else:
                return None,None,None,None,None,None,None,None

    finally:
        connection.close() 

def getmeidata_all(IDempresa):
    # Conecta ao banco de dados
    
    connect_to_db()
    data_quary = [
    "id",
    "mei_id",
    "situacao",
    "nome",
    "identificacao",
    "cnpj",
    "tributacao",
    "data_abertura",
    "prefeitura",
    "login",
    "senha",
    "pendencia_recolhimentos",
    "entrega_das_mensal",
    "pendencias",
    "email",
    "pendencia",
    "observacoes",
    "cpf",
    "codigo_acesso",
    "senha_gov",
    "nivel_gov",
    "endereco",
    "inscricao_estadual",
    "inscricao_municipal",
    "certificado_digital",
    "modelo_datavix",
    "homologado_sindicato",
    "vencimento",
    "created_at",
    "updated_at"
    ]
  
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT "
            for index,item in enumerate(data_quary):
                ConsultaSQL += f'`{item}`'

                if index < len(data_quary) - 1:
                    ConsultaSQL += ","

            ConsultaSQL += f"FROM `meis` WHERE `id` = '{IDempresa}'"
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
            botões_yesornot = [2,24]
            for item in botões_yesornot:
                if results_list[item] == 1:
                    results_list[item] = "SIM"
                else:
                    results_list[item] = "NÃO"

      
            
            
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
                return nova_lista,Listadeidentificação,data_quary
            else:
                return None,None

    finally:
        connection.close() 

def gerartexto():
    Listadedados, identificadores, qr = getmeidata_toEdit(20)
        
    Variaveis= [
        "entry_Nome",
        "entry_Situao",
        "entry_Identificao",
        "entry_CNPJ",
        "entry_Tributao",
        "entry_Data_abertura_",
        "entry_Prefeitura",
        "entry_Login",
        "entry_Senha",
        "entry_Pendncia_de_Recolhimentos",
        "entry_Entrega_de_DAS_Mensal",
        "entry_E_mail",
        "entry_Pendncias",
        "entry_Observaes",
        "entry_CPF",
        "entry_Cdigo_de_Acesso",
        "entry_Senha_GOV",
        "entry_Nvel_GOV",
        "entry_Endereo",
        "entry_Inscrio_Estadual",
        "entry_Inscrio_Municipal",
        "entry_Certificado_Digital",
        "entry_Modelo_Datavix",
        "entry_Homologado___Sindicato",
        "entry_Vencimento_",
        "entry_Ano",
        "entry_Faturamento",
        ]
    for i, item in enumerate(Variaveis):
        num=i
        if i >= 0 and i < 14: 
            num +=2
        if i == 0:
            num =3  

        if i == 1:
            num =2
          

        if i == 11:
            num =14   
        if i == 12:
            num =13   
        if i == 13:
            num =16   
        if i >= 14:
            num +=3 

        print(f"""\n{item}.delete(0, 'end')""")
        if i==99 or (i>999 and i<9999):
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


def Pegar_dados_contabilidade():
    # Conecta ao banco de dados
    
    connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `cnpj`,`nome`,`telefone` FROM `py_cont_meis`"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchall()

        
            if results is not None: 
                return results
            else:
                return None

    finally:
        connection.close()


def Pegar_dados_para_Contrato(Id,Campos):
    # Conecta ao banco de dados
    
    connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT {Campos} FROM `meis` WHERE id = {Id}"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()

            if results is not None: 
                NovoResult = []  # Lista para armazenar os itens convertidos
                for item in results:
    
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
                    NovoResult.append(novoitemlistagem)

                return NovoResult
            else:
                return None

    finally:
        connection.close()


def Novosdados_ParaContrato(idmei):

    with connection.cursor() as cursor:
            ConsultaSQL = f"SELECT `nome_fantasia`,`razao_social`,`celular`,`cep`,`rua`,`numero`,`complemento`,`bairro`,`cidade`,`estado`,`senha_certificado`,`liberacao_nf`,`nome_pessoa`,`sobrenome`,`nome_mae`,`estado_civil`,`genero`,`data_nascimento`,`numero_rg`,`orgao_rg`,`data_expedicao_rg`,`modelo_contrato`,`data_inicio_parceria`,`data_distrato`,`cnae`,`responsavel_recolhimento`,`valores_recebidos_adm`,`repasse`,`kit_padrao`,`assessoria_contabil`,`nome_assessoria_contabil`,`dias_abertura`,`hora_seg`,`hora_ter`,`hora_qua`,`hora_qui`,`hora_sex`,`hora_sab`,`hora_dom` FROM `meis` WHERE `id` = {idmei}"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()
            return results