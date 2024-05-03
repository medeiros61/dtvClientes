from tkinter import *
from tkinter import filedialog
import Modulos.Cliente.Botoes_Edicao as btedit
import Modulos.Database.Clients as dbc
import pandas as pd
import Modulos.Database.Logs as log
import Modulos.Cliente.Cliente_V_E as C_Tela_Edit
Evento_CAD= f'Entrou na tela de cadastro de cliente'
obs_CAD = ""

Evento_Exporta= f'Exportando Listagem de clientes'
obs_Exporta = ""

#FUNÇÃO PARA ADICIONAR
def Adicionar_cliente(Dadosparateladeedição):
    frame_edição_dados = Dadosparateladeedição[0]
    Frame_atual = Dadosparateladeedição[1]
    C_Tela_Edit.definiçãotipodeentrada('Criação')
    btedit.limparcampos()
    Frame_atual.pack_forget()
    frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 
    
    log.RegistrarEventosdeLOG(Evento_CAD,obs_CAD) 



#FUNÇÃO PARA EXCLUIR
def excluir_cliente(TreeView):
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
                # Agora você tem o nome do cliente selecionado
                Evento= f'Excluindo cliente: [id:{id}] {nome_cliente}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
         
            else:
                print("Nenhum cliente selecionado.")


#FUNÇÃO PARA EDITAR
def editar_cliente(TreeView,Dadosparateladeedição):
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
                btedit.Importardados(id)
                Frame_atual.pack_forget()
                frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 
                # Agora você tem o nome do cliente selecionado
                Evento= f'Editando cliente: [id:{id}] {nome_cliente}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
                C_Tela_Edit.definiçãotipodeentrada('Edição')
            
            else:
                print("Nenhum cliente selecionado.")


#FUNÇÃO PARA COMENTAR
def comentar_cliente(TreeView):
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
                # Agora você tem o nome do cliente selecionado
                Evento= f'Comentando cliente: [id:{id}] {nome_cliente}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
          
            else:
                print("Nenhum cliente selecionado.")
#FUNÇÃO PARA EXCEL

def Exportar_clientes(clinte_filter_entry,uf_filter_entry,Status_filter_entry):

    

    # Cabeçalhos e dados
    cabecalhos = [
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

    nome = clinte_filter_entry

    uf = uf_filter_entry
    ativo = Status_filter_entry
        
    if ativo == "ATIVO" :
            ativo = 1
    if ativo == "INATIVO" :
            ativo = 0 
        
    if uf =="TODOS":
            uf = None

    if ativo =="TODOS":
            ativo = None

    
 
    dados= dbc.getclientdata_all('nome_empresa',nome,'uf',uf,'ativo',ativo)

    # Converter os dados em um DataFrame do pandas
    df = pd.DataFrame(dados, columns=cabecalhos)

    df = df[[
        "id",
        "nome_empresa",
        "cnpj",
        "uf",
        "municipio",
        "atividade",
        "data_abertura",
        "link_whatsapp",
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
        "dpto_pessoal_sindicalizada",
        "dpto_pessoal_login",
        "dpto_pessoal_senha",
        "sistema_bpo",
        "site_bpo",
        "usuario_bpo",
        "senha_simples_bpo",
        "banco1",
        "banco2",
        "tipo_bpo",
        "observacoes_gerais_bpo",
        "municipal_observacoes",
        "municipal_demais_senhas",
        "municipal_senha_abertura_processos",
        "created_at",
        "updated_at"
    ]]  # Reorganize as colunas conforme necessário

    pasta_selecionada = filedialog.askdirectory()
    
    # Exportar o DataFrame para um arquivo Excel
    df.to_excel(f'{pasta_selecionada}/dados_clientes.xlsx', index=False)  # O argumento index=False evita a inclusão do índice no arquivo Excel
    

    log.RegistrarEventosdeLOG(Evento_Exporta,obs_Exporta) 