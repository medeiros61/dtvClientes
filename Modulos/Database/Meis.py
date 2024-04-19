import pymysql
from datetime import datetime, date,timedelta

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

def getmeidata_toEdit(IDempresa):
    # Conecta ao banco de dados
    
    connect_to_da()
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
            botões_yesornot = [25]
            for item in botões_yesornot:
                if results_list[item] == 1:
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

