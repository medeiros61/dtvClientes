from tkinter import *
import Modulos.Mei.Botoes_Edicao as btedit
import Modulos.Database.Logs as log
import Modulos.Mei.Mei_V_E as M_Tela_Edit
import Modulos.Database.Meis as dbm
import pandas as pd
from tkinter import filedialog

Evento_Contratante = f'Entrou na tela de cadastro de MEI Contratante'
obs_Contratante = ""

Evento_Parceira= f'Entrou na tela de cadastro de MEI Parceira'
obs_Parceira = ""

Evento_exportar= f'Exportando Listagem MEIS'
obs_exportar = ""

#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Contratante(Dadosparateladeedição):

            
    frame_edição_dados = Dadosparateladeedição[0]
    Frame_atual = Dadosparateladeedição[1]
    M_Tela_Edit.definiçãotipodeentrada('Criação_Contratante')
    
    btedit.limparbotões()
    Frame_atual.pack_forget()
    frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 

    btedit.preencher_tipo('Criar_Contratante',"")
    log.RegistrarEventosdeLOG(Evento_Contratante,obs_Contratante) 

#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Parceira(Dadosparateladeedição,TreeView):
    # Obtém a seleção da TreeView
    selecao = TreeView.selection()
    # Verifica se há algum item selecionado
    if selecao:
        # Obtém as informações do item selecionado
        valores = TreeView.item(selecao[0])['values']
        # Verifica se há valores associados
        if valores:
            # Obtém o nome do MEI
            id = valores[0]
            nome_cliente = valores[1]
            btedit.id_empresa_Contratante(id)
            btedit.preencher_tipo('Criar_Parceira',nome_cliente)

    frame_edição_dados = Dadosparateladeedição[0]
    Frame_atual = Dadosparateladeedição[1]
    M_Tela_Edit.definiçãotipodeentrada('Criação_Parceira')
    btedit.limparbotões()
    Frame_atual.pack_forget()
    frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 

    
    log.RegistrarEventosdeLOG(Evento_Parceira,obs_Parceira) 




#FUNÇÃO PARA EXCLUIR
def excluir_MEI(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                id = valores[0]
                nome_MEI = valores[1]
                Evento= f'Excluindo MEI: [id:{id}] {nome_MEI}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 

            else:
                print("Nenhum MEI selecionado.")


#FUNÇÃO PARA EDITAR
def editar_MEI(TreeView,Dadosparateladeedição):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do cliente
                id = valores[0]
                nome_cliente = valores[1]
                frame_edição_dados = Dadosparateladeedição[0]
                Frame_atual = Dadosparateladeedição[1]
                Frame_atual.pack_forget()
                frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True)
                btedit.Importardados(id,Dadosparateladeedição)
                Evento= f'Editando Cliente Planilha MEI: [id:{id}] {nome_cliente}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
                M_Tela_Edit.definiçãotipodeentrada('Edição')
            else:
                print("Nenhum cliente selecionado.")

#FUNÇÃO PARA COMENTAR
def comentar_MEI(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                id = valores[0]
                nome_MEI = valores[1]
                Evento= f'Comentando Cliente Planilha MEI: [id:{id}] {nome_MEI}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
            else:
                print("Nenhum MEI selecionado.")
#FUNÇÃO PARA EXCEL


def Exportar_MEIs(clinte_filter_entry,identificacao_filter_entry,Status_filter_entry):

    

    # Cabeçalhos e dados
    cabecalhos = [
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
    
    nome = clinte_filter_entry

    identificacao = identificacao_filter_entry
    ativo = Status_filter_entry
        
    if ativo == "ATIVO" :
            ativo = 1
    if ativo == "INATIVO" :
            ativo = 0 
        
    if identificacao =="TODOS":
            identificacao = None

    if ativo =="TODOS":
            ativo = None

    
 
    dados= dbm.getMEIdata_all('nome',nome,'identificacao',identificacao,'situacao',ativo)

    # Converter os dados em um DataFrame do pandas
    df = pd.DataFrame(dados, columns=cabecalhos)

    df = df[[
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
    ]]  # Reorganize as colunas conforme necessário

    pasta_selecionada = filedialog.askdirectory()
    
    # Exportar o DataFrame para um arquivo Excel
    df.to_excel(f'{pasta_selecionada}/Dados_Meis.xlsx', index=False)  # O argumento index=False evita a inclusão do índice no arquivo Excel

    log.RegistrarEventosdeLOG(Evento_exportar,obs_exportar) 
         
