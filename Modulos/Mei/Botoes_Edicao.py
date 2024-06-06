import customtkinter as ctk
import Modulos.Database.Meis as dbm
from tkinter import *
import tkinter as tk
from tkinter import ttk
import Modulos.Mei.Func_mei as Func_Mei
from tkinter import messagebox
from datetime import datetime
import Modulos.Database.Logs as log
import threading as td
import Modulos.Mei.PainelContratos as Pnel_Cont


def preencher_tipo(tipo_Cont_ou_Parc,contratante):
    if tipo_Cont_ou_Parc == "Criar_Contratante":
        frame_dados_mei[0].configure(text=f"")
        entry_Identificao.configure(state='normal')
        entry_Identificao.delete(0,'end')
        entry_Identificao.insert(0,'Contratante')
        entry_Identificao.configure(state='disabled')
        
    if tipo_Cont_ou_Parc == "Criar_Parceira":
        frame_dados_mei[0].configure(text=f"CONTRATANTE: {contratante}")
        entry_Identificao.configure(state='normal')
        entry_Identificao.delete(0,'end')
        entry_Identificao.insert(0,'Parceira')
        entry_Identificao.configure(state='disabled')

    if tipo_Cont_ou_Parc == "Contratante":
     
        entry_Identificao.configure(state='normal')
        entry_Identificao.delete(0,'end')
        entry_Identificao.insert(0,'Contratante')
        entry_Identificao.configure(state='disabled')
        
    if tipo_Cont_ou_Parc == "Parceira":

        entry_Identificao.configure(state='normal')
        entry_Identificao.delete(0,'end')
        entry_Identificao.insert(0,'Parceira')
        entry_Identificao.configure(state='disabled')

def id_empresa_Contratante(idmei):
    global Id_Contratante
    Id_Contratante = idmei

def pegar_dados_para_envio(tipo):
    
    nomeclienteparalog = entry_Nome.get()

    ##Definições da Query
    CamposBD = ''
    ItensParaBD = ''

    #mei_id
    if tipo == "Criação_Contratante":
        pass
    elif tipo =="Criação_Parceira":
        ItensParaBD += f"'{Id_Contratante}'¬¬"
        CamposBD +='mei_id,'
        
    #situacao - tinyint(1)
    testeValor = entry_Situao.get()
    if testeValor == "SIM":
        ItensParaBD += "1¬¬" 
    else:
        ItensParaBD += "0¬¬" 
    CamposBD +='situacao,'

    #nome - varchar(255)
    ItensParaBD += f"'{entry_Nome.get()}'¬¬"
    CamposBD +='nome,'

    #identificacao - varchar(255)
    ItensParaBD += f"'{entry_Identificao.get()}'¬¬"
    CamposBD +='identificacao,'

    #cnpj - varchar(255)
    ItensParaBD += f"'{entry_CNPJ.get()}'¬¬"
    CamposBD +='cnpj,'

    #tributacao - varchar(255)
    ItensParaBD += f"'{entry_Tributao.get()}'¬¬"
    CamposBD +='tributacao,'

    #data_abertura - date
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_Data_abertura_.get())}'¬¬"
    CamposBD +='data_abertura,'

    #prefeitura - varchar(255)	
    ItensParaBD += f"'{entry_Prefeitura.get()}'¬¬"
    CamposBD +='prefeitura,'

    #login- varchar(255)
    ItensParaBD += f"'{entry_Login.get()}'¬¬"
    CamposBD +='login,'

    #senha- varchar(255)
    ItensParaBD += f"'{entry_Senha.get()}'¬¬"
    CamposBD +='senha,'

    #pendencia_recolhimentos- varchar(255)
    ItensParaBD += f"'{entry_Pendncia_de_Recolhimentos.get()}'¬¬"
    CamposBD +='pendencia_recolhimentos,'

    #entrega_das_mensal- varchar(255)
    ItensParaBD += f"'{entry_Entrega_de_DAS_Mensal.get()}'¬¬"
    CamposBD +='entrega_das_mensal,'

    #pendencias- varchar(255)
    ItensParaBD += f"'{entry_Pendncias.get("1.0", "end-1c")}'¬¬"
    CamposBD +='pendencias,'

    #email- varchar(255)
    ItensParaBD += f"'{entry_E_mail.get()}'¬¬"
    CamposBD +='email,'

    #observacoes - text
    ItensParaBD += f"'{entry_Observaes.get("1.0", "end-1c")}'¬¬"
    CamposBD +='observacoes,'

    #cpf- varchar(255)
    ItensParaBD += f"'{entry_CPF.get()}'¬¬"
    CamposBD +='cpf,'

    #codigo_acesso- varchar(255)
    ItensParaBD += f"'{entry_Cdigo_de_Acesso.get()}'¬¬"
    CamposBD +='codigo_acesso,'

    #senha_gov- varchar(255)
    ItensParaBD += f"'{entry_Senha_GOV.get()}'¬¬"
    CamposBD +='senha_gov,'

    #nivel_gov- varchar(255)
    ItensParaBD += f"'{entry_Nvel_GOV.get()}'¬¬"
    CamposBD +='nivel_gov,'

    #endereco- varchar(255)
    ItensParaBD += f"'{entry_Endereo.get()}'¬¬"
    CamposBD +='endereco,'

    #inscricao_estadual- varchar(255)
    ItensParaBD += f"'{entry_Inscrio_Estadual.get()}'¬¬"
    CamposBD +='inscricao_estadual,'

    #inscricao_municipal- varchar(255)
    ItensParaBD += f"'{entry_Inscrio_Municipal.get()}'¬¬"
    CamposBD +='inscricao_municipal,'

    #certificado_digital - tinyint(1)
    testeValor = entry_Certificado_Digital.get()
    if testeValor == "SIM":
        ItensParaBD += "1¬¬" 
    else:
        ItensParaBD += "0¬¬" 
    CamposBD +='certificado_digital,'

    #modelo_datavix- varchar(255)
    ItensParaBD += f"'{entry_Modelo_Datavix.get()}'¬¬"
    CamposBD +='modelo_datavix,'

    #homologado_sindicato- varchar(255)
    ItensParaBD += f"'{entry_Homologado___Sindicato.get()}'¬¬"
    CamposBD +='homologado_sindicato,'

    #vencimento- date
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_Vencimento_.get())}'¬¬"
    CamposBD +='vencimento,'

    #nome_fantasia VARCHAR(255)
    ItensParaBD += f"'{entry_Fantasia.get()}'¬¬"
    CamposBD +='nome_fantasia,'

    #razao_social VARCHAR(255)
    ItensParaBD += f"'{entry_RAZÃO_SOCIAL.get()}'¬¬"
    CamposBD +='razao_social,'
    
    #celular VARCHAR(255)
    ItensParaBD += f"'{entry_Celular.get()}'¬¬"
    CamposBD +='celular,'
    
    #cep VARCHAR(255)
    ItensParaBD += f"'{entry_cep.get()}'¬¬"
    CamposBD +='cep,'
    
    #rua VARCHAR(255)
    ItensParaBD += f"'{entry_rua.get()}'¬¬"
    CamposBD +='rua,'
    
    #numero VARCHAR(255)
    ItensParaBD += f"'{entry_numero.get()}'¬¬"
    CamposBD +='numero,'
    
    #complemento VARCHAR(255)
    ItensParaBD += f"'{entry_complemento.get()}'¬¬"
    CamposBD +='complemento,'
    
    #bairro VARCHAR(255)
    ItensParaBD += f"'{entry_bairro.get()}'¬¬"
    CamposBD +='bairro,'
    
    #cidade VARCHAR(255)
    ItensParaBD += f"'{entry_cidade.get()}'¬¬"
    CamposBD +='cidade,'
    
    #estado VARCHAR(255)
    ItensParaBD += f"'{entry_Estado.get()}'¬¬"
    CamposBD +='estado,'
    
    #senha_certificado VARCHAR(255)
    ItensParaBD += f"'{entry_Senha_Certificado_Digital.get()}'¬¬"
    CamposBD +='senha_certificado,'
    
    #liberacao_nf VARCHAR(255)
    ItensParaBD += f"'{entry_NF_LIBERADA.get()}'¬¬"
    CamposBD +='liberacao_nf,'
    
    #nome_pessoa VARCHAR(255)
    ItensParaBD += f"'{entry_NomePF.get()}'¬¬"
    CamposBD +='nome_pessoa,'
    
    #sobrenome VARCHAR(255)
    ItensParaBD += f"'{entry_SobrenomePF.get()}'¬¬"
    CamposBD +='sobrenome,'
    
    #nome_mae VARCHAR(255)
    ItensParaBD += f"'{entry_Mae.get()}'¬¬"
    CamposBD +='nome_mae,'
    
    #estado_civil VARCHAR(255)
    ItensParaBD += f"'{ESTADO_CIVIL_var.get()}'¬¬"
    CamposBD +='estado_civil,'
    
    #genero VARCHAR(255)
    ItensParaBD += f"'{GENERO_var.get()}'¬¬"
    CamposBD +='genero,'
    
    #data_nascimento DATE
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_dtNascimento.get())}'¬¬"
    CamposBD +='data_nascimento,'
    
    #numero_rg VARCHAR(255)
    ItensParaBD += f"'{entry_RG.get()}'¬¬"
    CamposBD +='numero_rg,'
    
    #orgao_rg VARCHAR(255)
    ItensParaBD += f"'{entry_RGOrgao.get()}'¬¬"
    CamposBD +='orgao_rg,'
    
    #data_expedicao_rg DATE
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_RGData.get())}'¬¬"
    CamposBD +='data_expedicao_rg,'
    
    #modelo_contrato VARCHAR(255)
    ItensParaBD += f"'{MODELO_CONTRATO_var.get()}'¬¬"
    CamposBD +='modelo_contrato,'
    
    #data_inicio_parceria DATE
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_DATA_INICIAL_PARCEIRA.get())}'¬¬"
    CamposBD +='data_inicio_parceria,'
    
    #data_distrato DATE
    ItensParaBD += f"'{DataEnviadaParaOBD(entry_DATA_DISTRATO_PARCEIRA.get())}'¬¬"
    CamposBD +='data_distrato,'

    #cnae VARCHAR(255)
    
    ItensParaBD += f"'{obter_itens_Cnae()}'¬¬"
    
    CamposBD +='cnae,'
    
    #responsavel_recolhimento VARCHAR(255)
    ItensParaBD += f"'{RESPONSAVEL_RECOLHIMENTO_var.get()}'¬¬"
    CamposBD +='responsavel_recolhimento,'
    
    #valores_recebidos_adm VARCHAR(255)
    ItensParaBD += f"'{GESTAO_VALORES_var.get()}'¬¬"
    CamposBD +='valores_recebidos_adm,'
    
    #repasse VARCHAR(255)
    ItensParaBD += f"'{PERIODO_REPASSE_var.get()}'¬¬"
    CamposBD +='repasse,'
    
    #kit_padrao VARCHAR(255)
    ItensParaBD += f"'{Sw_KIT_PADRAO.get()}'¬¬"
    CamposBD +='kit_padrao,'
    
    #assessoria_contabil VARCHAR(255)
    ItensParaBD += f"'{ASSESSORIA_CONTABIL_var.get()}'¬¬"
    CamposBD +='assessoria_contabil,'
    
    #nome_assessoria_contabil VARCHAR(255)
    ItensParaBD += f"'{CONTABILIDADE_ASSESORA_var.get()}'¬¬"
    CamposBD +='nome_assessoria_contabil,'
    
    #dias_abertura VARCHAR(255)
    DiasMarcados =verificar_dias_marcados()
    nomes_dias = [dia for dia in DiasMarcados]
    nomes_dias = list(nomes_dias)
    dias_abertura_str = ','.join(nomes_dias)
    ItensParaBD += f"'{dias_abertura_str}'¬¬"
    CamposBD +='dias_abertura,'
    
    #hora_seg VARCHAR(255)
    Dia = 'SEG'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_seg,'
    
    #hora_ter VARCHAR(255)
    Dia = 'TER'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_ter,'
    
    #hora_qua VARCHAR(255)
    Dia = 'QUA'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_qua,'
    
    #hora_qui VARCHAR(255)
    Dia = 'QUI'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_qui,'
    
    #hora_sex VARCHAR(255)
    Dia = 'SEX'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_sex,'
    
    #hora_sab VARCHAR(255)
    Dia = 'SAB'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_sab,'
    
    #hora_dom VARCHAR(255)
    Dia = 'DOM'
    HorarioABRIR = f'{eval(f"Hora_Abertura_{Dia}").get()}-{eval(f"Min_Abertura_{Dia}").get()}'
    HorarioFECHAR = f'{eval(f"Hora_Fechamento_{Dia}").get()}-{eval(f"Min_Fechamento_{Dia}").get()}'
    ItensParaBD += f"'{HorarioABRIR}-{HorarioFECHAR}'¬¬"
    CamposBD +='hora_dom,'

    

    agora = datetime.now()
    if tipo =="Edição":
        #- date
        ItensParaBD += f"'{agora}'"
        CamposBD +='updated_at'
    else: 
        #- date   
        ItensParaBD += f"'{agora}'¬¬"
        CamposBD +='created_at,'
        #- date
        ItensParaBD += f"'{agora}'"
        CamposBD +='updated_at'

    # Transforma a string em uma lista de campos separados por vírgula
    CamposBD_List = CamposBD.split(',')
    ItensParaBD_List = ItensParaBD.split('¬¬')

    # Transforma a lista em uma tupla
    CamposBD_tupla = tuple(CamposBD_List)
    ItensParaBD_tupla = tuple(ItensParaBD_List)

    if tipo =="Edição":
        queryUpdate = f"""UPDATE `meis` SET """
        for index,item in enumerate(CamposBD_tupla):
            queryUpdate += f"{CamposBD_tupla[index]} = {ItensParaBD_tupla[index]}"
            if index < len(CamposBD_tupla) - 1:
                queryUpdate += "," 

        queryUpdate += f"WHERE id = {Listadedados[0]};"
        global QuerydeExecução
        QuerydeExecução = queryUpdate
        #QuerydeExecução =''
        #print("Edição")
    else:
        queryCriação = f"""INSERT INTO `meis` ("""
      
        for index,item in enumerate(CamposBD_tupla):
            queryCriação += f"{CamposBD_tupla[index]}" 
            if index < len(CamposBD_tupla) - 1:
                queryCriação += ","

        queryCriação += f") VALUES ("

        for index,item in enumerate(ItensParaBD_tupla):
            queryCriação += f"{ItensParaBD_tupla[index]}" 
            if index < len(ItensParaBD_tupla) - 1:
                queryCriação += ","
        queryCriação += f")"

        QuerydeExecução = queryCriação 
        

    dbm.Query_Save_Data(QuerydeExecução)
    if tipo =="Edição":
        log.RegistrarEventosdeLOG(f'Edição de MEI Salvo - cliente : {nomeclienteparalog}',f'') 
    else:
        log.RegistrarEventosdeLOG('Registrou um MEI  novo',f'Novo cliente : {nomeclienteparalog}')     


def limparbotões():
    global Limpartreeview
    def Limpartreeview(TreeV):
        try:
            for item in TreeV.get_children():
                    TreeV.delete(item)     
        except Exception :
                pass
        
    TabViewGlobal.set("Empresa")
    
    entry_Nome.delete(0, 'end')
    entry_Identificao.delete(0, 'end')
    entry_CNPJ.delete(0, 'end')
    entry_Tributao.delete(0, 'end')
    entry_Data_abertura_.delete(0, 'end')
    entry_Prefeitura.delete(0, 'end')
    entry_Login.delete(0, 'end')
    entry_Senha.delete(0, 'end')
    entry_Pendncia_de_Recolhimentos.delete(0, 'end')
    entry_Entrega_de_DAS_Mensal.delete(0, 'end')
    entry_E_mail.delete(0, 'end')
    entry_Pendncias.delete('1.0', 'end')
    entry_Observaes.delete('1.0', 'end')
    entry_CPF.delete(0, 'end')
    entry_Cdigo_de_Acesso.delete(0, 'end')
    entry_Senha_GOV.delete(0, 'end')
    entry_Nvel_GOV.delete(0, 'end')
    entry_Endereo.delete(0, 'end')
    entry_Inscrio_Estadual.delete(0, 'end')
    entry_Inscrio_Municipal.delete(0, 'end')
    entry_Modelo_Datavix.delete(0, 'end')
    entry_Homologado___Sindicato.delete(0, 'end')
    entry_Vencimento_.delete(0, 'end')
    #entry_Ano_dasn.delete(0, 'end')
    #entry_Faturamento.delete(0, 'end')
    #entry_Observaes_dasn.delete(0, 'end')
    entry_Fantasia.delete(0, 'end')
    entry_RAZÃO_SOCIAL.delete(0, 'end')
    entry_Celular.delete(0, 'end')
    entry_cep.delete(0, 'end')
    entry_rua.delete(0, 'end')
    entry_numero.delete(0, 'end')
    entry_complemento.delete(0, 'end')
    entry_bairro.delete(0, 'end')
    entry_cidade.delete(0, 'end')
    entry_Estado.set(siglas_estados[0])
    entry_Senha_Certificado_Digital.delete(0, 'end')
    entry_NF_LIBERADA.set('Não')
    entry_NomePF.delete(0, 'end')
    entry_SobrenomePF.delete(0, 'end')
    entry_Mae.delete(0, 'end')
    ESTADO_CIVIL_var.set('Solteiro')
    GENERO_var.set('Feminino')
    entry_dtNascimento.delete(0, 'end')
    entry_RG.delete(0, 'end')
    entry_RGOrgao.delete(0, 'end')
    entry_RGData.delete(0, 'end')
    MODELO_CONTRATO_var.set("Contrato Padrão - Versão Datavix Contábil Digital Eireli")
    entry_DATA_INICIAL_PARCEIRA.delete(0, 'end')
    entry_DATA_DISTRATO_PARCEIRA.delete(0, 'end')
    entry_CNAE.delete(0, 'end')
    RESPONSAVEL_RECOLHIMENTO_var.set("Salão Parceiro")
    GESTAO_VALORES_var.set("Salão Parceiro")
    PERIODO_REPASSE_var.set("Mensal")
    #Sw_KIT_PADRAO.set(1)
    ASSESSORIA_CONTABIL_var.set("Sim")
    CONTABILIDADE_ASSESORA_var.set("")
    listboxCnae.delete(0, tk.END)
    bt_Excluir_cnae.configure(state='disabled')
    dias_da_semana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
   
    if len(dias_da_semana)>0:
        for dia in dias_da_semana:
            if dia !='N/A' and dia !='':
                eval(f"Chk_{dia}_var").set(True)
                ativardia(f"Chk_{dia}", dia)
                eval(f"Hora_Abertura_{dia}").set(eval(f'00'))
                eval(f"Min_Abertura_{dia}").set(eval(f'00'))
                eval(f"Hora_Fechamento_{dia}").set(eval(f'00'))
                eval(f"Min_Fechamento_{dia}").set(eval(f'00'))
                eval(f"Chk_{dia}_var").set(False)
                ativardia(f"Chk_{dia}", dia)

    Limpartreeview(TreeViewParceiras)
    Limpartreeview(TreeViewServicos)
    Limpartreeview(TreeviewDas)
    FrameDas.grid_remove()
    
def Importardados(idcliente,Dadosparateladeedição):
    global importar_dados_treeview,CONTABILIDADES_assesoras,tela_Mae,Listadedados

    def importar_dados_treeview(TreeV,dados,):
        for result in dados:
            TreeV.insert("", 'end', values=result)
            
    limparbotões()

    tela_Mae = Dadosparateladeedição

    CONTABILIDADES_assesoras=[]
   
    Listadedados, identificadores,qr,meis,Lista_de_DAS,Lista_Servicos,DadosComplemtares = dbm.getmeidata_toEdit(idcliente)

    Contabilidades_Dados_Gerais = dbm.Pegar_dados_contabilidade()
    

    if Listadedados[0]:
        frame_dados_mei[1].configure(text=f"EMPRESA: {Listadedados[3]} (ID:{Listadedados[0]})")
        frame_dados_mei[2].configure(text=f"TIPO: {Listadedados[4]}")

    if Listadedados[1] != "N/A":
        nomemei=  dbm.GetnameMEI(Listadedados[1])
        
        frame_dados_mei[0].configure(text=f"CONTRATANTE: {nomemei[0]}")
       
        Se_For_Parciera()
        #TreeViewParceiras.grid_remove()
        #scrollbarParceiras.grid_remove()
        #bt_Editar_MEI_Parceiras.grid_remove()
    else:
        Se_For_Contratante()
        
        frame_dados_mei[0].configure(text=f"")
        

        #TreeViewParceiras.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(5,0), pady=(5,10))
        #scrollbarParceiras.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
        #bt_Editar_MEI_Parceiras.grid(row=3, column=0,columnspan=3, sticky="n", padx=(1,0), pady=(5,10))

    

    entry_Nome.insert(0,Listadedados[3]) # Campo nome do banco de dados


    entry_Situao.set(Listadedados[2]) # Campo situacao do banco de dados

    preencher_tipo(Listadedados[4],"") # Campo identificacao do banco de dados

    entry_CNPJ.insert(0,Listadedados[5]) # Campo cnpj do banco de dados

    entry_Tributao.insert(0,Listadedados[6]) # Campo tributacao do banco de dados

    entry_Data_abertura_.insert(0,Listadedados[7]) # Campo data_abertura do banco de dados

    entry_Prefeitura.insert(0,Listadedados[8]) # Campo prefeitura do banco de dados

    entry_Login.insert(0,Listadedados[9]) # Campo login do banco de dados

    entry_Senha.insert(0,Listadedados[10]) # Campo senha do banco de dados

    entry_Pendncia_de_Recolhimentos.insert(0,Listadedados[11]) # Campo pendencia_recolhimentos do banco de dados

    entry_Entrega_de_DAS_Mensal.insert(0,Listadedados[12]) # Campo entrega_das_mensal do banco de dados

    entry_E_mail.insert(0,Listadedados[14]) # Campo email do banco de dados

    entry_Pendncias.insert('1.0',Listadedados[13]) # Campo pendencias do banco de dados

    entry_Observaes.insert('1.0',Listadedados[16]) # Campo observacoes do banco de dados

    entry_CPF.insert(0,Listadedados[17]) # Campo cpf do banco de dados

    entry_Cdigo_de_Acesso.insert(0,Listadedados[18]) # Campo codigo_acesso do banco de dados

    entry_Senha_GOV.insert(0,Listadedados[19]) # Campo senha_gov do banco de dados

    entry_Nvel_GOV.insert(0,Listadedados[20]) # Campo nivel_gov do banco de dados

    entry_Endereo.insert(0,Listadedados[21]) # Campo endereco do banco de dados

    entry_Inscrio_Estadual.insert(0,Listadedados[22]) # Campo inscricao_estadual do banco de dados

    entry_Inscrio_Municipal.insert(0,Listadedados[23]) # Campo inscricao_municipal do banco de dados


    entry_Certificado_Digital.set(Listadedados[24]) # Campo certificado_digital do banco de dados

    entry_Modelo_Datavix.insert(0,Listadedados[25]) # Campo modelo_datavix do banco de dados

    entry_Homologado___Sindicato.insert(0,Listadedados[26]) # Campo homologado_sindicato do banco de dados

    entry_Vencimento_.insert(0,Listadedados[27]) # Campo vencimento do banco de dados

    entry_Fantasia.insert(0,DadosComplemtares[0])
    entry_RAZÃO_SOCIAL.insert(0,DadosComplemtares[1])
    entry_Celular.insert(0,DadosComplemtares[2])
    entry_cep.insert(0,DadosComplemtares[3])
    entry_rua.insert(0,DadosComplemtares[4])
    entry_numero.insert(0,DadosComplemtares[5])
    entry_complemento.insert(0,DadosComplemtares[6])
    entry_bairro.insert(0,DadosComplemtares[7])
    entry_cidade.insert(0,DadosComplemtares[8])
    entry_Estado.set(DadosComplemtares[9])
    entry_Senha_Certificado_Digital.insert(0,DadosComplemtares[10])
    entry_NF_LIBERADA.set(DadosComplemtares[11])
    entry_NomePF.insert(0,DadosComplemtares[12])
    entry_SobrenomePF.insert(0,DadosComplemtares[13])
    entry_Mae.insert(0,DadosComplemtares[14])
    ESTADO_CIVIL_var.set(DadosComplemtares[15])
    GENERO_var.set(DadosComplemtares[16])
    entry_dtNascimento.insert(0,DadosComplemtares[17])
    entry_RG.insert(0,DadosComplemtares[18])
    entry_RGOrgao.insert(0,DadosComplemtares[19])
    entry_RGData.insert(0,DadosComplemtares[20])
    MODELO_CONTRATO_var.set(DadosComplemtares[21])
    entry_DATA_INICIAL_PARCEIRA.insert(0,DadosComplemtares[22])
    entry_DATA_DISTRATO_PARCEIRA.insert(0,DadosComplemtares[23])
    #entry_CNAE.insert(0,DadosComplemtares[24])
    List_Cnaes = DadosComplemtares[24].split(',')
    
    for cnae in List_Cnaes: 
        if cnae != 'N/A':
            listboxCnae.insert(tk.END, cnae)
   
        
    RESPONSAVEL_RECOLHIMENTO_var.set(DadosComplemtares[25])
    GESTAO_VALORES_var.set(DadosComplemtares[26])
    PERIODO_REPASSE_var.set(DadosComplemtares[27])
    Sw_KIT_PADRAO.setvar(DadosComplemtares[28])
    ASSESSORIA_CONTABIL_var.set(DadosComplemtares[29])
    CONTABILIDADE_ASSESORA_var.set(DadosComplemtares[30])
    # Parse 'dias_abertura' and set corresponding widgets
    dias_abertura_str = DadosComplemtares[31]
    dias_marcados = dias_abertura_str.split(',')
    # Set dias_marcados to corresponding widgets

    # Parse and set the opening and closing hours
    hora_SEG = DadosComplemtares[32].split('-')
    hora_TER = DadosComplemtares[33].split('-')
    hora_QUA = DadosComplemtares[34].split('-')
    hora_QUI = DadosComplemtares[35].split('-')
    hora_SEX = DadosComplemtares[36].split('-')
    hora_SAB = DadosComplemtares[37].split('-')
    hora_DOM = DadosComplemtares[38].split('-')
    if len(dias_marcados)>0:
        for dia in dias_marcados:
            if dia !='N/A' and dia !='':
                eval(f"Chk_{dia}_var").set(True)
                ativardia(f"Chk_{dia}", dia)
                eval(f"Hora_Abertura_{dia}").set(eval(f'hora_{dia}[0]'))
                eval(f"Min_Abertura_{dia}").set(eval(f'hora_{dia}[1]'))
                eval(f"Hora_Fechamento_{dia}").set(eval(f'hora_{dia}[2]'))
                eval(f"Min_Fechamento_{dia}").set(eval(f'hora_{dia}[3]'))
                
    
    
    
    
    #entry_Ano_dasn.insert(0,Listadedados[28]) # Campo created_at do banco de dados

    #entry_Faturamento.insert(0,Listadedados[29]) # Campo updated_at do banco de dados

    #entry_Observaes_dasn.insert(0,Listadedados[29]) # Campo updated_at do banco de dados
    try:
        for contabilidade in Contabilidades_Dados_Gerais:
            CONTABILIDADES_assesoras.append(f'{contabilidade[1]}({contabilidade[0]}) Tel: {contabilidade[2]}')
        Menu_CONTABILIDADE_ASSESORA.configure(values=CONTABILIDADES_assesoras)
        CONTABILIDADE_ASSESORA_var.set(value=CONTABILIDADES_assesoras[0])   
        Menu_CONTABILIDADE_ASSESORA.configure(state='normal')     
    except Exception:
        Menu_CONTABILIDADE_ASSESORA.configure(state='disabled')

    for id,result in enumerate(meis):
        if result[2] == None:
            pendencias = ""
        else:
            pendencias = result[2]    
        if result[3] == 1:
            ativo = "ATIVO"
        else:
            ativo = "INATIVO"    
            
        Lista = [result[0],result[1],pendencias,ativo]

        TreeViewParceiras.insert("", 'end', values=Lista)
    
    if len(Lista_Servicos)>0:
        item = Lista_Servicos[0]
        tipo = item[0]
        TP_REPASSE_var.set(f"{tipo}")
    else:

        TP_REPASSE_var.set("Percentual")
    
    importar_dados_treeview(TreeViewServicos,Lista_Servicos)
    importar_dados_treeview(TreeviewDas,Lista_de_DAS)
    if verificar_se_tem_valores_na_treeview(TreeViewServicos)==False:
            Menu_TP_REPASSE.configure(state='normal')  
    else:
            Menu_TP_REPASSE.configure(state='disabled')  
    #reativa o grid do dasn    
    FrameDas.grid(row=0, column=0, sticky="n")

def preparo_para_enviar_contrato():   
    global Id_Contratante

    idMaster = Listadedados[1]
    ConsultaBD = ""
    ConsultaBD +='cnpj,'
    ConsultaBD +='razao_social,'
    ConsultaBD +='nome_fantasia,'
    ConsultaBD +='cpf,'
    ConsultaBD +='nome_pessoa,'
    ConsultaBD +='sobrenome,'
    ConsultaBD +='data_nascimento,'
    ConsultaBD +='email,'
    ConsultaBD +='celular,'
    ConsultaBD +='nome_mae,'
    ConsultaBD +='estado_civil,'
    ConsultaBD +='genero,'
    ConsultaBD +='cep,'
    ConsultaBD +='rua,'
    ConsultaBD +='numero,'
    ConsultaBD +='complemento,'
    ConsultaBD +='bairro,'
    ConsultaBD +='cidade,'
    ConsultaBD +='estado,'
    ConsultaBD +='numero_rg,'
    ConsultaBD +='orgao_rg,'
    ConsultaBD +='data_expedicao_rg,'
    ConsultaBD +='dias_abertura,'
    ConsultaBD +='hora_seg,'
    ConsultaBD +='hora_ter,'
    ConsultaBD +='hora_qua,'
    ConsultaBD +='hora_qui,'
    ConsultaBD +='hora_sex,'
    ConsultaBD +='hora_sab,'
    ConsultaBD +='hora_dom'
    DadosContratante = dbm.Pegar_dados_para_Contrato(idMaster,ConsultaBD)



    ##profissional parceiro


    Profissional_Parceiro = ''
    Profissional_Parceiro += f"{entry_CPF.get()}¬¬"
    Profissional_Parceiro += f"{entry_NomePF.get()}¬¬"
    Profissional_Parceiro += f"{entry_SobrenomePF.get()}¬¬"
    Profissional_Parceiro += f"{entry_dtNascimento.get()}¬¬"
    Profissional_Parceiro += f"{entry_E_mail.get()}¬¬"
    Profissional_Parceiro += f"{entry_Celular.get()}¬¬"
    Profissional_Parceiro += f"{entry_Mae.get()}¬¬"
    Profissional_Parceiro += f"{ESTADO_CIVIL_var.get()}¬¬"
    Profissional_Parceiro += f"{GENERO_var.get()}¬¬"
    Profissional_Parceiro += f"{entry_cep.get()}¬¬"
    Profissional_Parceiro += f"{entry_rua.get()}¬¬"
    Profissional_Parceiro += f"{entry_numero.get()}¬¬"
    Profissional_Parceiro += f"{entry_complemento.get()}¬¬"
    Profissional_Parceiro += f"{entry_bairro.get()}¬¬"
    Profissional_Parceiro += f"{entry_cidade.get()}¬¬"
    Profissional_Parceiro += f"{entry_Estado.get()}¬¬"
    Profissional_Parceiro += f"{entry_RG.get()}¬¬"
    Profissional_Parceiro += f"{entry_RGOrgao.get()}¬¬"
    Profissional_Parceiro += f"{entry_RGData.get()}¬¬"
       

    #CNPJ - PROFISSIONAL PARCEIRO
    Profissional_Parceiro_CNPJ =""
    Profissional_Parceiro_CNPJ += f"{entry_CNPJ.get()}¬¬"
    Profissional_Parceiro_CNPJ += f"{entry_RAZÃO_SOCIAL.get()}¬¬"
    Profissional_Parceiro_CNPJ += f"{obter_itens_Cnae()}¬¬"

    #CONTABILIDADE - PROFISSIONAL PARCEIRO
    Contabilidade_Profissional_Parceiro = ""
    Contabilidade_Profissional_Parceiro += f"{ASSESSORIA_CONTABIL_var.get()}¬¬"
    Contabilidade_Profissional_Parceiro += f"{CONTABILIDADE_ASSESORA_var.get()}¬¬"##Separar dados

    #GESTÃO DE OUTRAS INFORMAÇÕES
    OutrasInformacoes=""
    OutrasInformacoes += f"{entry_DATA_INICIAL_PARCEIRA.get()}¬¬"
    OutrasInformacoes += f"{RESPONSAVEL_RECOLHIMENTO_var.get()}¬¬"



    
    Servicos = []
    for item in TreeViewServicos.get_children():
        Linha = TreeViewServicos.item(item, 'values')
        Servicos.append([Linha[0], Linha[1], Linha[2], Linha[3]])
   


    #Periodicidade do repasse:
    OutrasInformacoes += f"{PERIODO_REPASSE_var.get()}¬¬"


    #Os valores recebidos pelo cliente final serão geridos e administrados por:
    OutrasInformacoes += f"{GESTAO_VALORES_var.get()}¬¬"


    OutrasInformacoes += f"{Sw_KIT_PADRAO.get()}¬¬"


    Profissional_Parceiro = Profissional_Parceiro.split('¬¬')  
    Profissional_Parceiro_CNPJ = Profissional_Parceiro_CNPJ.split('¬¬')    
    Contabilidade_Profissional_Parceiro = Contabilidade_Profissional_Parceiro.split('¬¬')   
    OutrasInformacoes += f"{MODELO_CONTRATO_var.get()}¬¬" 
    
    OutrasInformacoes = OutrasInformacoes.split('¬¬')    
    

    Profissional_Parceiro.pop()
    Profissional_Parceiro_CNPJ.pop()
    Contabilidade_Profissional_Parceiro.pop()
    OutrasInformacoes.pop()
 
    return DadosContratante,Profissional_Parceiro,Profissional_Parceiro_CNPJ,Contabilidade_Profissional_Parceiro,OutrasInformacoes,Servicos,

listaContratos_Digitação = []

id_contrato = 0

def retornarTread():
    return td.Thread(target=Pnel_Cont.digitação_contrato) 

digitaçao = retornarTread()

def envio_dados_contrato():
    global id_contrato,digitaçao 
    id_contrato += 1
    Dados = preparo_para_enviar_contrato()
    listaContratos_Digitação.append([Dados,id_contrato])
    lc = locals()
    emp = Dados[2]  
    nome = emp[1]
    infos = [f'{nome}(ID:{id_contrato})','Digitando']
    Pnel_Cont.incluir_dados_viewDG(infos)
    
    # Verificar se a thread digitação está ativa
    if 'digitaçao' in locals() or digitaçao.is_alive():
        
        print("A thread digitação está ativa.")
    else:
        print("A thread digitação não está ativa.")
        # Create a new thread each time this function is called
        digitaçao = retornarTread()
        
        # Start the new thread
        digitaçao.start()
        print("Ativando...")
    
def pegar_dados_Contrato():
    return listaContratos_Digitação

def Deletar_Primeiro_Contrato():
    listaContratos_Digitação.pop(0)
        
        
def DataEnviadaParaOBD(datainformada):                      
    try:
        data = datetime.strptime(datainformada, "%d/%m/%Y")
        data_formatada = data.strftime("%Y-%m-%d")   
        return data_formatada  
    except Exception:
        pass

def adicição_dados_DASN(operacao):
    IDcliente = Listadedados[0]
    queryCriação = f"INSERT INTO "

         
    if operacao == 'ADD':
        if entry_Ano_dasn.get() !='' and entry_Faturamento.get() !='':
                
            CamposBD = 'mei_id,ano,faturamento,observacao'
            ValoresBD = f"{entry_Ano_dasn.get()},'{entry_Faturamento.get()}','{entry_Observaes_dasn.get()}'"
            ValoresBD_lista = [valor.strip("'") for valor in ValoresBD.split(',')]
            importar_dados_treeview(TreeviewDas,[ValoresBD_lista])
            queryCriação += f"`das`({CamposBD}) VALUES ({IDcliente},{ValoresBD})"
            entry_Ano_dasn.delete(0, 'end')
            entry_Faturamento.delete(0, 'end')
            entry_Observaes_dasn.delete(0, 'end')
            dbm.Query_Save_Data(queryCriação)

    if operacao == 'DEL':
            # Obtém a seleção da TreeView
        selecao = TreeviewDas.selection()
            # Verifica se há algum item selecionado
        if selecao:
                # Obtém as informações do item selecionado
            valores = TreeviewDas.item(selecao[0])['values']
                # Verifica se há valores associados
            if valores:
                    # Obtém o nome do cliente
                v1 = valores[0]
                v2 = valores[1]
                v3 = valores[2]
                queryDeleção = f"DELETE FROM `das` WHERE mei_id = {IDcliente} AND ano = {f'{v1}'} AND faturamento = '{f'{v2}'}' AND observacao = '{f'{v3}'}'" 
                TreeviewDas.delete(selecao)
                dbm.Query_remove_Data(queryDeleção) 

def verificar_se_tem_valores_na_treeview(tree):
    # Obtém todos os itens da TreeView
    itens = tree.get_children()
    
    # Verifica se a lista de itens está vazia
    if len(itens) > 0:
        return True
    else:
        return False

def Envio_dados_servico(operacao):
    IDcliente = Listadedados[0]
    queryCriação = f"INSERT INTO "

         
    if operacao == 'ADD':
        if entry_NOME_SERVICO.get() !='' and entry_REPASSE_SALAO.get() !=''and entry_REPASSE_PROFISSIONAL.get():  
            CamposBD = 'mei_id,tipo,servico,salao,parceiro'
            ValoresBD = f"'{TP_REPASSE_var.get()}','{entry_NOME_SERVICO.get()}','{entry_REPASSE_SALAO.get()}','{entry_REPASSE_PROFISSIONAL.get()}'"
            ValoresBD_lista = [valor.strip("'") for valor in ValoresBD.split(',')]
            importar_dados_treeview(TreeViewServicos,[ValoresBD_lista])
            queryCriação += f"`py_meis_servicos`({CamposBD}) VALUES ({IDcliente},{ValoresBD})"
            entry_REPASSE_SALAO.delete(0, 'end')
            entry_REPASSE_PROFISSIONAL.delete(0, 'end')
            entry_NOME_SERVICO.delete(0, 'end')
            Menu_TP_REPASSE.configure(state='disabled')
            dbm.Query_Save_Data(queryCriação)
            
    if operacao == 'DEL':
            # Obtém a seleção da TreeView
        selecao = TreeViewServicos.selection()
            # Verifica se há algum item selecionado
        if selecao:
                # Obtém as informações do item selecionado
            valores = TreeViewServicos.item(selecao[0])['values']
                # Verifica se há valores associados
            if valores:
                    # Obtém o nome do cliente
                v1 = valores[0]
                v2 = valores[1]
                v3 = valores[2]
                v4 = valores[3]
                queryDeleção = f"DELETE FROM `py_meis_servicos` WHERE mei_id = {IDcliente} AND tipo = '{f'{v1}'}' AND servico = '{f'{v2}'}' AND salao = '{f'{v3}'}'AND parceiro = '{f'{v4}'}'" 
                TreeViewServicos.delete(selecao)
                dbm.Query_remove_Data(queryDeleção) 

        if verificar_se_tem_valores_na_treeview(TreeViewServicos)==False:
            Menu_TP_REPASSE.configure(state='normal')
            
def Addcontabildiades():
    IDcliente = Listadedados[0]
    queryCriação = f"INSERT INTO "

    operacao = 'ADD'    
    if operacao == 'ADD':
        if entry_CNPJ_CONT_MEIS.get() !='' and entry_NOME_CONT_MEIS.get() !=''and entry_TEL_CONT_MEIS.get() !='':  
            CamposBD = 'cnpj,nome,telefone'
            ValoresBD = f"{entry_CNPJ_CONT_MEIS.get()},'{entry_NOME_CONT_MEIS.get()}','{entry_TEL_CONT_MEIS.get()}'"
            ValoresBD_lista = [valor.strip("'") for valor in ValoresBD.split(',')]

            CONTABILIDADES_assesoras.append(f'{entry_NOME_CONT_MEIS.get()}({entry_CNPJ_CONT_MEIS.get()}) Tel: {entry_TEL_CONT_MEIS.get()}')    

            Menu_CONTABILIDADE_ASSESORA.configure(values=CONTABILIDADES_assesoras)
            queryCriação += f"`py_cont_meis`({CamposBD}) VALUES ({ValoresBD})"
            entry_NOME_CONT_MEIS.delete(0, 'end')
            entry_TEL_CONT_MEIS.delete(0, 'end')
            entry_CNPJ_CONT_MEIS.delete(0, 'end')
            dbm.Query_Save_Data(queryCriação)
            TopLevel_CONTABILIDADE.quit()
            TopLevel_CONTABILIDADE.destroy()
            



def criarbotoes(Viewer,frameprincipal,Caminho_Logo_Edit,Caminho_Logo_Add,Caminho_Logo_Rem):
    global frame_dados_mei,entry_Nome,entry_Situao,entry_Identificao,entry_CNPJ,entry_Tributao,entry_Data_abertura_,entry_Prefeitura,entry_Login,entry_Senha,entry_Pendncia_de_Recolhimentos,entry_Entrega_de_DAS_Mensal,entry_E_mail,entry_Pendncias,entry_Observaes,entry_CPF,entry_Cdigo_de_Acesso,entry_Senha_GOV,entry_Nvel_GOV,entry_Endereo,entry_Inscrio_Estadual,entry_Inscrio_Municipal,entry_Certificado_Digital,entry_Modelo_Datavix,entry_Homologado___Sindicato,entry_Vencimento_,entry_Faturamento,TreeViewParceiras,scrollbarParceiras,bt_Editar_MEI_Parceiras,TabViewGlobal,TreeviewDas,entry_Ano_dasn,entry_Faturamento,entry_Observaes_dasn,FrameDas,Framelistaparceiras,FrameDadosContratoParceira,Se_For_Contratante,Se_For_Parciera,entry_Fantasia,entry_RAZÃO_SOCIAL,entry_Celular,entry_cep,entry_rua,entry_numero,entry_complemento,entry_bairro,entry_cidade,entry_Estado,entry_Senha_Certificado_Digital,entry_NF_LIBERADA,entry_NomePF,entry_SobrenomePF,entry_Mae,ESTADO_CIVIL_var,GENERO_var,entry_dtNascimento,entry_RG,entry_RGOrgao,entry_RGData,MODELO_CONTRATO_var,entry_DATA_INICIAL_PARCEIRA,entry_DATA_DISTRATO_PARCEIRA,entry_CNAE,RESPONSAVEL_RECOLHIMENTO_var,GESTAO_VALORES_var,PERIODO_REPASSE_var,Sw_KIT_PADRAO,ASSESSORIA_CONTABIL_var,CONTABILIDADE_ASSESORA_var,verificar_dias_marcados,TreeViewServicos,entry_REPASSE_PROFISSIONAL,entry_REPASSE_SALAO,entry_NOME_SERVICO,TP_REPASSE_var,Menu_TP_REPASSE,Menu_CONTABILIDADE_ASSESORA,ativardia,siglas_estados,listboxCnae,obter_itens_Cnae,bt_Excluir_cnae
    TabViewGlobal = Viewer
    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)   
    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    def dadosparceira(*args):
        
        TeladadosParceiras = ctk.CTkToplevel(Viewer.tab("Contrato de Parceria"))
 
        selecao = TreeViewParceiras.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeViewParceiras.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                Nome = valores[1]
                Pendencias = valores[2]
                Status = valores[3]
                TeladadosParceiras.title(f"{Nome}")

                NomeLB = ctk.CTkLabel(TeladadosParceiras,text='Nome: ')
                NomeLB.grid(row = 0, column = 0, padx=10, pady=5, sticky="w")
                NomeLB_inf = ctk.CTkLabel(TeladadosParceiras,text=Nome)
                NomeLB_inf.grid(row = 0, column = 1, padx=10, sticky="w")
                
                StatusLB = ctk.CTkLabel(TeladadosParceiras,text='Status: ')
                StatusLB.grid(row = 1, column = 0, padx=10, pady=5, sticky="w")
                StatusLB_inf = ctk.CTkLabel(TeladadosParceiras,text=Status)
                StatusLB_inf.grid(row = 1, column = 1, sticky="w")

                PendenciasLB = ctk.CTkLabel(TeladadosParceiras,text='Pendencias')
                PendenciasLB.grid(row = 2, column = 0, padx=10, pady=5,columnspan=2, sticky="nsew")
                PendenciasLB_inf = ctk.CTkTextbox(TeladadosParceiras)
                PendenciasLB_inf.insert("1.0", Pendencias)
                PendenciasLB_inf.grid(row = 3, column = 0,columnspan=2, padx=10, pady=5,sticky="nsew")
                PendenciasLB_inf.configure(state='disabled')
                TeladadosParceiras.resizable(False,False)
    
    def validar_entrada_Numero_7Caracter(digit):
        return digit.isdigit() and len(digit) <= 7 or digit == ""

    def validar_data(entrada):
        if len(entrada) != 10:
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return False

        partes = entrada.split('/')
        if len(partes) != 3:
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return False

        dia, mes, ano = partes
        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return False

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999):
            messagebox.showerror("Erro", "Data fora do intervalo válido.")
            return False

        return True

    def verificar_entrada_data(event,campo):
        entrada = campo.get()
        if not validar_data(entrada):
            campo.delete(0, 'end')

    def ativarbotãoEditar(*args):
        selecao = TreeViewParceiras.selection()

        if selecao:
            valor = bt_Editar_MEI_Parceiras.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_Editar_MEI_Parceiras.configure(state='normal')  
        else:
            bt_Editar_MEI_Parceiras.configure(state='disabled') 
    
    def verificarseleção(treeAnalisada,bt):
        seleção = treeAnalisada.selection()

        if seleção:
            valor = bt.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt.configure(state='normal') 
        else:
           bt.configure(state='disabled') 
    
    def Somentenumero(P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def Somentenumeroevigula(P):
        if str.isdigit(P) or P == "" :
            tamanho = len(P)
            if TP_REPASSE_var.get() == "Percentual":    
                if tamanho <=2:
                    return True
            
                return False
            else:
                return True
        else:
            return False
        
    def Somentenumeroevigulaeponto(P):
        if all(char.isdigit() or char in ",." for char in P) or P == "":
            return True
        else:
            return False

     #Selecionar tipo Repasse - Valor ou percentual
    
    def SelecaoMenu(choice):
        if choice == 'Percentual':
            label_REPASSE_SALAO.configure(text="Percentual Salão")
            label_REPASSE_PROFISSIONAL.configure(text="Percentual Profissional")
        if choice == 'Valor':
            label_REPASSE_SALAO.configure(text="Valor Salão")
            label_REPASSE_PROFISSIONAL.configure(text="Valor Profissional")
    def contabilidadeAssessora(choice):
        if choice == 'Não':
            Menu_CONTABILIDADE_ASSESORA.configure(state='disabled')
        if choice == 'Sim':
            Menu_CONTABILIDADE_ASSESORA.configure(state='normal') 

    def AtivarBTExcluir_Repasse(*args):
        selecao = TreeViewServicos.selection()

        if selecao:
            valor = bt_EXCLUIR_REPASSE.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_EXCLUIR_REPASSE.configure(state='normal')  
        else:
            bt_EXCLUIR_REPASSE.configure(state='disabled')
    
    def TopLevel_CadastraCont():
        #Dados contabilidade , cnpj , nome e telefone
        global entry_CNPJ_CONT_MEIS,entry_NOME_CONT_MEIS,entry_TEL_CONT_MEIS,TopLevel_CONTABILIDADE

        TopLevel_CONTABILIDADE = ctk.CTkToplevel(FrameDadosContratoParceira)
        TopLevel_CONTABILIDADE.title("Contabilidade")
        ##  TOP level
        label_CNPJ_CONT_MEIS = ctk.CTkLabel(TopLevel_CONTABILIDADE, text="CNPJ")
        entry_CNPJ_CONT_MEIS = ctk.CTkEntry(TopLevel_CONTABILIDADE)
        label_CNPJ_CONT_MEIS.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        entry_CNPJ_CONT_MEIS.grid(row=11, column=1, padx=10, pady=5, sticky="nsew") 
        
        label_NOME_CONT_MEIS = ctk.CTkLabel(TopLevel_CONTABILIDADE, text="Nome")
        entry_NOME_CONT_MEIS = ctk.CTkEntry(TopLevel_CONTABILIDADE)
        label_NOME_CONT_MEIS.grid(row=12, column=0, padx=10, pady=5, sticky="w")
        entry_NOME_CONT_MEIS.grid(row=12, column=1, padx=10, pady=5, sticky="nsew") 
        
        label_TEL_CONT_MEIS = ctk.CTkLabel(TopLevel_CONTABILIDADE, text="Telefone")
        entry_TEL_CONT_MEIS = ctk.CTkEntry(TopLevel_CONTABILIDADE)
        label_TEL_CONT_MEIS.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        entry_TEL_CONT_MEIS.grid(row=13, column=1, padx=10, pady=5, sticky="nsew") 

        
        bt_add = ctk.CTkButton(TopLevel_CONTABILIDADE,image=logo_add,text="",command=Addcontabildiades,width =20)
        bt_add.grid(row=11,rowspan=3, column=2, padx=10, pady=5, sticky="nsew")

    def Se_For_Parciera():
        FrameDadosContratoParceira.grid(row=1, column=0, sticky="nsew", padx=(5,5), pady=(5,10))
        Framelistaparceiras.grid_remove()
        label_Fantasia.grid_remove()
        entry_Fantasia.grid_remove()
        FrameDadosContratoCONTRATANTE.grid_remove()

    def Se_For_Contratante():
        Framelistaparceiras.grid(row=2, column=0,pady=5, padx=10, sticky="new")
        FrameDadosContratoCONTRATANTE.grid(row=1, column=0, sticky="nsew", padx=(5,5), pady=(5,10))
        FrameDadosContratoParceira.grid_remove()
        label_Fantasia.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_Fantasia.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="new")
         
    
    def ativardia(variavel, Dia):
        if eval(f"{variavel}_var").get() == True:
            eval(f"Hora_Abertura_{Dia}").configure(state="normal")
            eval(f"Min_Abertura_{Dia}").configure(state="normal")
            eval(f"Hora_Fechamento_{Dia}").configure(state="normal")
            eval(f"Min_Fechamento_{Dia}").configure(state="normal")
        else:
            eval(f"Hora_Abertura_{Dia}").configure(state="disabled")
            eval(f"Min_Abertura_{Dia}").configure(state="disabled")
            eval(f"Hora_Fechamento_{Dia}").configure(state="disabled")
            eval(f"Min_Fechamento_{Dia}").configure(state="disabled")
    
    def verificar_dias_marcados():
        #dias_marcados = [dia for dia in dias_da_semana if eval(f"Chk_{dia}_var").get()]
        dias_com_horarios = {}
        for dia in dias_da_semana:
            if eval(f"Chk_{dia}_var").get():
                horario_abertura = eval(f"Hora_Abertura_{dia}").get()
                Min_abertura = eval(f"Min_Abertura_{dia}").get()
                horario_fechamento = eval(f"Hora_Fechamento_{dia}").get()
                Min_fechamento = eval(f"Min_Fechamento_{dia}").get()
                dias_com_horarios[dia] = {
                    "abertura": f'{horario_abertura}:{Min_abertura}',
                    "fechamento": f'{horario_fechamento}:{Min_fechamento}'
                }
        #print(dias_com_horarios)
        #if 'TER' in dias_com_horarios:
        #    horarios_terca = dias_com_horarios['TER']
        #    print("Horários de Terça-feira:", horarios_terca)
        #else:
        #    print("Terça-feira não está marcada.")
        return dias_com_horarios
    
    
    def adicionarcnae():
        cnae = entry_CNAE.get()
        if len(cnae)==7:
            listboxCnae.insert(tk.END, cnae)
            entry_CNAE.delete(0, 'end')
            
            
    def excluircnae():
        #listboxCnae.delete(0, tk.END)
        # Obtém o índice do item selecionado
        indice_selecionado = listboxCnae.curselection()

        # Deleta o item selecionado da listboxCnae
        if indice_selecionado:
            listboxCnae.delete(indice_selecionado)   
         
            
    def obter_itens_Cnae():
        # Obtém o número total de itens na listboxCnae
        numero_itens = listboxCnae.size()

        # Lista para armazenar os itens da listboxCnae
        itens = ''
      
        # Itera sobre os índices da listboxCnae e obtém os itens
        for i in range(numero_itens):
            itens += f'{listboxCnae.get(i)}'
            if i < numero_itens-1:
                itens += ','
                

        
        return itens
    
    
    def AtivarBTExcluir_Cnae(event):

        if listboxCnae.size() > 0:
     
            bt_Excluir_cnae.configure(state=tk.NORMAL)
        else:
       
            bt_Excluir_cnae.configure(state=tk.DISABLED)
    
     
    def VerificarSomaPercentual():
        if TP_REPASSE_var.get() == "Percentual":    
            salão = entry_REPASSE_SALAO.get()
            parceiro = entry_REPASSE_PROFISSIONAL.get()
            
            soma = float(parceiro) + float(salão)
            if soma == 100:
                Envio_dados_servico('ADD')
            else:
                messagebox.showerror("Erro", "A soma dos percentuais deve ser igual a 100%")
        else:
            Envio_dados_servico('ADD')
                    
    frame_dados_mei=frameprincipal
    yes_or_not = [
        "SIM","NÃO"
    ]
    not_or_yes = [
        "NÃO","SIM"
    ]


    cor_de_borda = "gray50"
    largura_borda = 2

    
### Empresa
    ScrollFrameEmpresas = ctk.CTkScrollableFrame(Viewer.tab("Empresa"), border_width=largura_borda, border_color=cor_de_borda,height=450)
    ScrollFrameEmpresas.pack(side=TOP, fill = BOTH)
    #ScrollFrameEmpresas.grid(row=0, column=0, sticky="n")
    Viewer.tab("Empresa").grid_rowconfigure(0, weight=1)
    Viewer.tab("Empresa").grid_columnconfigure(0, weight=1)

    FrameEmpresas = ctk.CTkFrame(ScrollFrameEmpresas, border_width=largura_borda, border_color=cor_de_borda)
    FrameEmpresas.grid(row=0, column=0, sticky="n")
    ScrollFrameEmpresas.grid_rowconfigure(0, weight=1)
    ScrollFrameEmpresas.grid_columnconfigure(0, weight=1)



    FrameDadosEmpresas = ctk.CTkFrame(FrameEmpresas, border_width=largura_borda, border_color=cor_de_borda)
    FrameDadosEmpresas.grid(row=0, column=0,pady=5, padx=10, sticky="nsew")

    label_Nome = ctk.CTkLabel(FrameDadosEmpresas, text="Nome")
    entry_Nome = ctk.CTkEntry(FrameDadosEmpresas)
    label_Nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Nome.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky="new")

    label_Fantasia = ctk.CTkLabel(FrameDadosEmpresas, text="Nome Fantasia")
    entry_Fantasia = ctk.CTkEntry(FrameDadosEmpresas)
 
    
  

    label_Identificao = ctk.CTkLabel(FrameDadosEmpresas, text="Identificação")
    entry_Identificao = ctk.CTkEntry(FrameDadosEmpresas)  
    label_Identificao.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    entry_Identificao.grid(row=0, column=5, padx=10, pady=5, sticky="new")
    entry_Identificao.configure(state='disabled')

    linha = 2
    label_RAZÃO_SOCIAL = ctk.CTkLabel(FrameDadosEmpresas, text="Razão social")
    entry_RAZÃO_SOCIAL = ctk.CTkEntry(FrameDadosEmpresas)
    label_RAZÃO_SOCIAL.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_RAZÃO_SOCIAL.grid(row=linha, column=1, columnspan=3, padx=10, pady=5, sticky="new")

    label_Data_abertura_ = ctk.CTkLabel(FrameDadosEmpresas, text="Data abertura (dd/mm/aaaa)")
    entry_Data_abertura_ = ctk.CTkEntry(FrameDadosEmpresas)

    label_Data_abertura_.grid(row=linha, column=4, padx=10, pady=5, sticky="w")
    entry_Data_abertura_.grid(row=linha, column=5, padx=10, pady=5, sticky="new")
    entry_Data_abertura_.bind('<FocusOut>', lambda event: verificar_entrada_data(event, entry_Data_abertura_)) 

    linha = 3
    label_CNPJ = ctk.CTkLabel(FrameDadosEmpresas, text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(FrameDadosEmpresas)
    label_CNPJ.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_CNPJ.grid(row=linha, column=1, padx=10, pady=5, sticky="new")

    label_Situao = ctk.CTkLabel(FrameDadosEmpresas, text="Ativo")
    entry_Situao = ctk.CTkComboBox(FrameDadosEmpresas,values=yes_or_not)  
    label_Situao.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_Situao.grid(row=linha, column=3, padx=10, pady=5, sticky="new")
 
  

    label_Celular = ctk.CTkLabel(FrameDadosEmpresas, text="Celular/Whatsapp")
    entry_Celular = ctk.CTkEntry(FrameDadosEmpresas)
    label_Celular.grid(row=linha, column=4, padx=10, pady=5, sticky="w")
    entry_Celular.grid(row=linha, column=5, padx=10, pady=5, sticky="new")


    linha = 4
    label_Tributao = ctk.CTkLabel(FrameDadosEmpresas, text="Tributação")
    entry_Tributao = ctk.CTkEntry(FrameDadosEmpresas)
    label_Tributao.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_Tributao.grid(row=linha, column=1, padx=10, pady=5, sticky="new")

    label_E_mail = ctk.CTkLabel(FrameDadosEmpresas, text="E-mail")
    entry_E_mail = ctk.CTkEntry(FrameDadosEmpresas)
    label_E_mail.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_E_mail.grid(row=linha, column=3,columnspan=3, padx=10, pady=5, sticky="new")

    label_Endereo = ctk.CTkLabel(FrameDadosEmpresas, text="Endereço")
    entry_Endereo = ctk.CTkEntry(FrameDadosEmpresas)
    #label_Endereo.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    #entry_Endereo.grid(row=4, column=1,columnspan=5, padx=10, pady=5, sticky="new")
  
    # Defina a fonte sublinhada
    underline_font = ctk.CTkFont(family="Helvetica", size=12, underline=True)
    linha = 5
    

    linha = 6
    label_cep = ctk.CTkLabel(FrameDadosEmpresas, text="CEP")
    entry_cep = ctk.CTkEntry(FrameDadosEmpresas)
    label_cep.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_cep.grid(row=linha, column=1, padx=10, pady=5, sticky="new")

    label_rua = ctk.CTkLabel(FrameDadosEmpresas, text="Rua")
    entry_rua = ctk.CTkEntry(FrameDadosEmpresas)
    label_rua.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_rua.grid(row=linha, column=3, padx=10,columnspan=3, pady=5, sticky="new")

    linha = 7
    label_numero = ctk.CTkLabel(FrameDadosEmpresas, text="Nº")
    entry_numero = ctk.CTkEntry(FrameDadosEmpresas)
    label_numero.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_numero.grid(row=linha, column=1, padx=10, pady=5, sticky="new")

    label_complemento = ctk.CTkLabel(FrameDadosEmpresas, text="Complemento")
    entry_complemento = ctk.CTkEntry(FrameDadosEmpresas)
    label_complemento.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_complemento.grid(row=linha, column=3,columnspan=3 , padx=10, pady=5, sticky="new")

    linha = 8
    label_bairro = ctk.CTkLabel(FrameDadosEmpresas, text="Bairro")
    entry_bairro = ctk.CTkEntry(FrameDadosEmpresas)
    label_bairro.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_bairro.grid(row=linha, column=1, padx=10, pady=5, sticky="new")

    label_cidade = ctk.CTkLabel(FrameDadosEmpresas, text="Cidade")
    entry_cidade = ctk.CTkEntry(FrameDadosEmpresas)
    label_cidade.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_cidade.grid(row=linha, column=3, padx=10, pady=5, sticky="new")


    siglas_estados = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ]
    label_Estado = ctk.CTkLabel(FrameDadosEmpresas, text="Estado")
    entry_Estado = ctk.CTkComboBox(FrameDadosEmpresas,values= siglas_estados)

    label_Estado.grid(row=linha, column=4, padx=10, pady=5, sticky="w")
    entry_Estado.grid(row=linha, column=5, padx=10, pady=5, sticky="new")


    FrameGerais = ctk.CTkFrame(FrameEmpresas, border_width=largura_borda, border_color=cor_de_borda)
    FrameGerais.grid(row=4, column=0, sticky="new")
   
    ## Dados Gerias de Acessos 
    FrameAcessosEprefeituras = ctk.CTkFrame(FrameGerais, border_width=largura_borda, border_color=cor_de_borda)
    FrameAcessosEprefeituras.grid(row=0, column=0,columnspan=6, padx=10,pady=5, sticky="nsew")

    linha = 0
    label_Prefeitura = ctk.CTkLabel(FrameAcessosEprefeituras, text="Prefeitura")
    entry_Prefeitura = ctk.CTkEntry(FrameAcessosEprefeituras,width=150)
    label_Prefeitura.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_Prefeitura.grid(row=linha, column=1, padx=10, pady=5, sticky="new")


    label_Login = ctk.CTkLabel(FrameAcessosEprefeituras, text="Login")
    entry_Login = ctk.CTkEntry(FrameAcessosEprefeituras)
    label_Login.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_Login.grid(row=linha, column=3, padx=10, pady=5, sticky="new")

    label_Senha = ctk.CTkLabel(FrameAcessosEprefeituras, text="Senha")
    entry_Senha = ctk.CTkEntry(FrameAcessosEprefeituras)
    label_Senha.grid(row=linha, column=4, padx=10, pady=5, sticky="w")
    entry_Senha.grid(row=linha, column=5, padx=10, pady=5, sticky="new")


    linha = 1
    label_NF_LIBERADA = ctk.CTkLabel(FrameAcessosEprefeituras, text="Nota Fiscal Liberada")
    entry_NF_LIBERADA = ctk.CTkComboBox(FrameAcessosEprefeituras,values=not_or_yes)
    label_NF_LIBERADA.grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry_NF_LIBERADA.grid(row=linha, column=1, padx=10, pady=5, sticky="new")
 
    label_Inscrio_Municipal = ctk.CTkLabel(FrameAcessosEprefeituras, text="Inscrição Municipal")
    entry_Inscrio_Municipal = ctk.CTkEntry(FrameAcessosEprefeituras)
    label_Inscrio_Municipal.grid(row=linha, column=2, padx=10, pady=5, sticky="w")
    entry_Inscrio_Municipal.grid(row=linha, column=3, padx=10, pady=5, sticky="new")

    label_Inscrio_Estadual = ctk.CTkLabel(FrameAcessosEprefeituras, text="Inscrição Estadual")
    entry_Inscrio_Estadual = ctk.CTkEntry(FrameAcessosEprefeituras)
    label_Inscrio_Estadual.grid(row=linha, column=4, padx=10, pady=5, sticky="w")
    entry_Inscrio_Estadual.grid(row=linha, column=5, padx=10, pady=5, sticky="new")

    linha = 2
    FrameGOV = ctk.CTkFrame(FrameAcessosEprefeituras, border_width=largura_borda, border_color=cor_de_borda)
    FrameGOV.grid(row=linha, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    
    label_CPF = ctk.CTkLabel(FrameGOV, text="CPF")
    entry_CPF = ctk.CTkEntry(FrameGOV)
    label_CPF.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_CPF.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    label_Senha_GOV = ctk.CTkLabel(FrameGOV, text="Senha GOV")
    entry_Senha_GOV = ctk.CTkEntry(FrameGOV)
    label_Senha_GOV.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Senha_GOV.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    label_Nvel_GOV = ctk.CTkLabel(FrameGOV, text="Nível GOV")
    entry_Nvel_GOV = ctk.CTkEntry(FrameGOV)
    label_Nvel_GOV.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_Nvel_GOV.grid(row=3, column=1, padx=10, pady=5, sticky="new")

    Frame_Cod_e_CERTIFICADO = ctk.CTkFrame(FrameAcessosEprefeituras, border_width=largura_borda, border_color=cor_de_borda)
    Frame_Cod_e_CERTIFICADO.grid(row=linha, column=2, columnspan=2, padx=10, pady=5, sticky="nsew")


    label_Cdigo_de_Acesso = ctk.CTkLabel(Frame_Cod_e_CERTIFICADO, text="Código de Acesso")
    entry_Cdigo_de_Acesso = ctk.CTkEntry(Frame_Cod_e_CERTIFICADO)
    label_Cdigo_de_Acesso.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Cdigo_de_Acesso.grid(row=1, column=3, padx=10, pady=5, sticky="new")

    label_Certificado_Digital = ctk.CTkLabel(Frame_Cod_e_CERTIFICADO, text="Certificado Digital")
    entry_Certificado_Digital = ctk.CTkComboBox(Frame_Cod_e_CERTIFICADO,values=not_or_yes)
    label_Certificado_Digital.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_Certificado_Digital.grid(row=2, column=3, padx=10, pady=5, sticky="new")

    label_Senha_Certificado_Digital = ctk.CTkLabel(Frame_Cod_e_CERTIFICADO, text="Senha Ceritificado")
    entry_Senha_Certificado_Digital = ctk.CTkEntry(Frame_Cod_e_CERTIFICADO)
    label_Senha_Certificado_Digital.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    entry_Senha_Certificado_Digital.grid(row=3, column=3, padx=10, pady=5, sticky="new")

    ##Pendencias MEI
    FrameInfoDAS = ctk.CTkFrame(FrameGerais, border_width=largura_borda, border_color=cor_de_borda)
    FrameInfoDAS.grid(row=1, column=0,columnspan=6,pady=5, padx=10, sticky="nsew")
    label_Entrega_de_DAS_Mensal = ctk.CTkLabel(FrameInfoDAS, text="Entrega de DAS Mensal")
    entry_Entrega_de_DAS_Mensal = ctk.CTkEntry(FrameInfoDAS)

    label_Entrega_de_DAS_Mensal.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Entrega_de_DAS_Mensal.grid(row=0, column=1, padx=10, pady=5, sticky="new")

    label_Pendncia_de_Recolhimentos = ctk.CTkLabel(FrameInfoDAS, text="Pendência de Recolhimentos")
    entry_Pendncia_de_Recolhimentos = ctk.CTkEntry(FrameInfoDAS,width=300)

    label_Pendncia_de_Recolhimentos.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Pendncia_de_Recolhimentos.grid(row=0, column=3,columnspan=4, padx=10, pady=5, sticky="new")

    ##Pendencias Gerais

    label_Pendncias = ctk.CTkLabel(FrameGerais, text="Pendências")
    entry_Pendncias = ctk.CTkTextbox(FrameGerais)
    
    label_Pendncias.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Pendncias.grid(row=3, column=0,columnspan=6, padx=10, pady=5, sticky="new")

    label_Observaes = ctk.CTkLabel(FrameGerais, text="Observações")
    entry_Observaes = ctk.CTkTextbox(FrameGerais)

    label_Observaes.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_Observaes.grid(row=5, column=0,columnspan=6, padx=10, pady=5, sticky="new")


    

#contrato parceria
    FrameParceiras = ctk.CTkFrame(Viewer.tab("Contrato de Parceria"), border_width=largura_borda, border_color=cor_de_borda)
    FrameParceiras.grid(row=0, column=0, sticky="n")
    Viewer.tab("Contrato de Parceria").grid_rowconfigure(0, weight=1)
    Viewer.tab("Contrato de Parceria").grid_columnconfigure(0, weight=1)

    Framelistaparceiras = ctk.CTkFrame(FrameParceiras, border_width=largura_borda, border_color=cor_de_borda)
    Framelistaparceiras.grid(row=0, column=0,pady=5, padx=10, sticky="new")
    
    label_Homologado___Sindicato = ctk.CTkLabel(Framelistaparceiras, text="Parceiras")

    label_Homologado___Sindicato.grid(row=0, column=0,columnspan=4, padx=10, pady=5, sticky="nsew")

    
    #### Interface para empresa contratante 
    TreeViewParceiras = ttk.Treeview(Framelistaparceiras, columns=("#","Nome","Pendências","Situação"), show='headings')
    TreeViewParceiras.grid(row=2, column=0,columnspan=3, sticky="new", padx=(5,0), pady=(5,10))
    TreeViewParceiras.bind('<<TreeviewSelect>>',ativarbotãoEditar)
    TreeViewParceiras.bind('<Double-1>',dadosparceira)
    # Define o as colunas
    TreeViewParceiras.heading("#", text="ID")
    TreeViewParceiras.heading("Nome", text="Nome")
    TreeViewParceiras.heading("Pendências", text="Pendências")
    TreeViewParceiras.heading("Situação", text="Situação")
    
    # Define o tamanho das colunas em pixels
    TreeViewParceiras.column("#", width=50)  # 
    TreeViewParceiras.column("Nome", width=250)  # 
    TreeViewParceiras.column("Pendências", width=500)  # 
    TreeViewParceiras.column("Situação", width=100)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbarParceiras = ctk.CTkScrollbar(Framelistaparceiras, command=TreeViewParceiras.yview)
    scrollbarParceiras.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeViewParceiras.configure(yscrollcommand=scrollbarParceiras.set)    

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_MEI_Parceiras = ctk.CTkButton(master=Framelistaparceiras,image=logo_editar, text="Editar",command=lambda: Func_Mei.editar_MEI(TreeViewParceiras,tela_Mae))
    bt_Editar_MEI_Parceiras.grid(row=3, column=0,columnspan=3, sticky="new", padx=(1,0), pady=(5,10))
    bt_Editar_MEI_Parceiras.configure(state='disabled') 

    
    ### Frame dados complemetares
    
    
    
    ##Frame da Homologação 
    
    FrameDadoshomologação = ctk.CTkFrame(FrameParceiras, border_width=largura_borda, border_color=cor_de_borda)
    FrameDadoshomologação.grid(row=0, column=0, sticky="n", padx=(5,5), pady=(5,10))
    
    label_Modelo_Datavix = ctk.CTkLabel(FrameDadoshomologação, text="Modelo Datavix")
    entry_Modelo_Datavix = ctk.CTkEntry(FrameDadoshomologação)

    label_Modelo_Datavix.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Modelo_Datavix.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Homologado___Sindicato = ctk.CTkLabel(FrameDadoshomologação, text="Homologado - Sindicato")
    entry_Homologado___Sindicato = ctk.CTkEntry(FrameDadoshomologação)

    label_Homologado___Sindicato.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_Homologado___Sindicato.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
    
    label_Vencimento_ = ctk.CTkLabel(FrameDadoshomologação, text="Vencimento (dd/mm/aaaa)")
    entry_Vencimento_ = ctk.CTkEntry(FrameDadoshomologação)
    label_Vencimento_.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Vencimento_.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

    entry_Vencimento_.bind('<FocusOut>', lambda event: verificar_entrada_data(event, entry_Vencimento_))
    
  


    #### Interface para empresa parceira
    


#DASN
   

    FrameDas = ctk.CTkFrame(Viewer.tab("DASN"), border_width=largura_borda, border_color=cor_de_borda)
    ValidarapenasNumero = FrameDas.register(Somentenumero)
    ValidarNumeroevigulaeponto = FrameDas.register(Somentenumeroevigulaeponto)
                                            
    Viewer.tab("DASN").grid_rowconfigure(0, weight=1)
    Viewer.tab("DASN").grid_columnconfigure(0, weight=1)

   
    
    label_Ano_dasn = ctk.CTkLabel(FrameDas, text="Ano")
    entry_Ano_dasn= ctk.CTkEntry(FrameDas, validate="key", validatecommand=(ValidarapenasNumero, "%P"))

    label_Ano_dasn.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Ano_dasn.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Faturamento = ctk.CTkLabel(FrameDas, text="Faturamento")
    entry_Faturamento = ctk.CTkEntry(FrameDas, validate="key", validatecommand=(ValidarNumeroevigulaeponto, "%P"))

    label_Faturamento.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_Faturamento.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Observaes_dasn = ctk.CTkLabel(FrameDas, text="Observações")
    entry_Observaes_dasn = ctk.CTkEntry(FrameDas)

    label_Observaes_dasn.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Observaes_dasn.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

    bt_add = ctk.CTkButton(FrameDas,image=logo_add, text="Adicionar",command=lambda:adicição_dados_DASN('ADD'))
    bt_add.grid(row=0, column=3, padx=5, pady=5, sticky="new")

    
    bt_Excluir = ctk.CTkButton(FrameDas,image=logo_excluir, text="Excluir",command=lambda:adicição_dados_DASN('DEL'))
    bt_Excluir.grid(row=1, column=3, padx=5, pady=5, sticky="new")
    bt_Excluir.configure(state='disabled')

    TreeviewDas = ttk.Treeview(FrameDas, columns=("Ano","Faturamento","Observações"), show='headings')
    TreeviewDas.grid(row=2, column=0,columnspan=4, sticky="nsew", padx=(5,5), pady=(5,10))
    TreeviewDas.bind('<<TreeviewSelect>>',lambda event: verificarseleção(TreeviewDas, bt_Excluir))

    # Define o as colunas
    TreeviewDas.heading("Ano", text="Ano")
    TreeviewDas.heading("Faturamento", text="Faturamento")
    TreeviewDas.heading("Observações", text="Observações")
    
    
    # Define o tamanho das colunas em pixels
    TreeviewDas.column("Ano", width=200)  # 
    TreeviewDas.column("Faturamento", width=200)  # 
    TreeviewDas.column("Observações", width=200)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(FrameDas, command=TreeviewDas.yview,height=100)
    scrollbar.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeviewDas.configure(yscrollcommand=scrollbar.set)    
 
 
 
 #### Dados compelementares 
    ScrollComplementar = ctk.CTkScrollableFrame(Viewer.tab("Outras Informações"), border_width=largura_borda, border_color=cor_de_borda,height=450)
    ScrollComplementar.pack(side=TOP, fill = BOTH)
    #ScrollFrameEmpresas.grid(row=0, column=0, sticky="n")
    Viewer.tab("Outras Informações").grid_rowconfigure(0, weight=1)
    Viewer.tab("Outras Informações").grid_columnconfigure(0, weight=1)


    FramedadosComp = ctk.CTkFrame(ScrollComplementar, border_width=largura_borda, border_color=cor_de_borda)                                  
    FramedadosComp.grid(row=0, column=0, sticky="n")
    ScrollComplementar.grid_rowconfigure(0, weight=1)
    ScrollComplementar.grid_columnconfigure(0, weight=1)
    
    #Frame Dados pessoais
    FrameDadosParceira = ctk.CTkFrame(FramedadosComp, border_width=largura_borda, border_color=cor_de_borda)
    FrameDadosParceira.grid(row=0, column=0, sticky="nsew", padx=(5,5), pady=(5,10))
    
    labelDadosPessoais = ctk.CTkLabel(FrameDadosParceira, text="Dados Pessoais")
    labelDadosPessoais.grid(row=0, column=0,columnspan=5, padx=10, pady=5, sticky="nsew")
    
    label_NomePF = ctk.CTkLabel(FrameDadosParceira, text="Nome")
    entry_NomePF = ctk.CTkEntry(FrameDadosParceira)
    label_NomePF.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_NomePF.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

    label_SobrenomePF = ctk.CTkLabel(FrameDadosParceira, text="Sobrenome")
    entry_SobrenomePF = ctk.CTkEntry(FrameDadosParceira)
    label_SobrenomePF.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_SobrenomePF.grid(row=1, column=3, padx=10, pady=5, sticky="nsew")

    label_Mae = ctk.CTkLabel(FrameDadosParceira, text="Nome da Mãe")
    entry_Mae = ctk.CTkEntry(FrameDadosParceira)
    label_Mae.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Mae.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    #ESTADO_CIVIL -------------------------------------------------------------------------------------
    label_ESTADO_CIVIL = ctk.CTkLabel(FrameDadosParceira, text="Estado Civil")
    label_ESTADO_CIVIL.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    ESTADO_CIVIL_var = ctk.StringVar(value="Solteiro")
    Menu_ESTADO_CIVIL = ctk.CTkOptionMenu(FrameDadosParceira,values=['Solteiro','Casado','Viúvo','Separado juducialmente','Divorciado'],
                                           
                                            variable=ESTADO_CIVIL_var)
    Menu_ESTADO_CIVIL.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")

    #DATA DE NASCIMENTO  ---------------------------------------------------------------------------
    label_dtNascimento = ctk.CTkLabel(FrameDadosParceira, text="Data de Nascimento")
    entry_dtNascimento = ctk.CTkEntry(FrameDadosParceira)
    label_dtNascimento.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_dtNascimento.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")

    #GENERO -------------------------------------------------------------------------------------------
    label_GENERO = ctk.CTkLabel(FrameDadosParceira, text="Gênero")
    label_GENERO.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    GENERO_var = ctk.StringVar(value="Feminino")
    Menu_GENERO = ctk.CTkOptionMenu(FrameDadosParceira,values=['Feminino','Masculino'],
                                           
                                            variable=GENERO_var)
    Menu_GENERO.grid(row=4, column=3, padx=10, pady=5, sticky="new")

    #Frame rg
    FrameRG = ctk.CTkFrame(FrameDadosParceira, border_width=largura_borda, border_color=cor_de_borda)
    FrameRG.grid(row=1, column=4, rowspan=4, sticky="nsew", padx=5, pady=5)


    label_RG = ctk.CTkLabel(FrameRG, text="Nº RG")
    entry_RG = ctk.CTkEntry(FrameRG)
    label_RG.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_RG.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    label_RGOrgao = ctk.CTkLabel(FrameRG, text="Órgão Expedidor")
    entry_RGOrgao = ctk.CTkEntry(FrameRG)
    label_RGOrgao.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_RGOrgao.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

    label_RGData = ctk.CTkLabel(FrameRG, text="Data Expedição")
    entry_RGData = ctk.CTkEntry(FrameRG)
    label_RGData.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_RGData.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
    entry_RGData.bind('<FocusOut>', lambda event: verificar_entrada_data(event, entry_RGData)) 
    #Frame Dados PARCEIRA (NAO VISIVEL NO CONTRANTE)
    
    FrameDadosContratoParceira = ctk.CTkFrame(FramedadosComp, border_width=largura_borda, border_color=cor_de_borda)
    #FrameDadosContratoParceira.grid(row=1, column=0, sticky="nsew", padx=(5,5), pady=(5,10))
   
    labelTitulo = ctk.CTkLabel(FrameDadosContratoParceira, text="Dados Contrato")
    labelTitulo.grid(row=1, column=0, padx=10, columnspan=8, pady=5, sticky="new") 
    
    #TIPO DO CONTRATO---------------------------------------------------------------
    bt_digitar_contrato = ctk.CTkButton(FrameDadosContratoParceira,text="Digitar Contrato", command=envio_dados_contrato)
    bt_digitar_contrato.grid(row=1, column=0, padx=10, columnspan=8, pady=5, sticky="e")

    label_MODELO_CONTRATO = ctk.CTkLabel(FrameDadosContratoParceira, text="Modelo de contrato")
    label_MODELO_CONTRATO.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    MODELO_CONTRATO_var = ctk.StringVar(value="Contrato Padrão - Versão Datavix Contábil Digital Eireli")
    Menu_MODELO_CONTRATO = ctk.CTkOptionMenu(FrameDadosContratoParceira,values=['Contrato de Parceria (Versão 1.0) - Norma Coletiva (46473.003589/2017-99)','Contrato de Parceria - MPT - 2013 (46736.002113/2014-50)','Contrato Padrão - Versão 1.02 (46473.003589/2017-99)','Contrato Padrão - Versão Datavix Contábil Digital Eireli'],
                                            command=SelecaoMenu,
                                            variable=MODELO_CONTRATO_var)
    Menu_MODELO_CONTRATO.grid(row=3, column=1, columnspan=7, padx=10, pady=5, sticky="new")
    

                                        
                                        
    
    

    #Data de contrato     
    FrameContrato = ctk.CTkFrame(FrameDadosContratoParceira, border_width=largura_borda, border_color=cor_de_borda)
    FrameContrato.grid(row=4, column=0, columnspan=8, padx=10, pady=5, sticky="nsew")

    #Inicio da parcceria 
    label_DATA_INICIAL_PARCEIRA = ctk.CTkLabel(FrameContrato, text="Data Incio Parceria")
    entry_DATA_INICIAL_PARCEIRA = ctk.CTkEntry(FrameContrato)
    label_DATA_INICIAL_PARCEIRA.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_DATA_INICIAL_PARCEIRA.grid(row=4, column=1, padx=10, pady=5, sticky="nsew") 
    entry_DATA_INICIAL_PARCEIRA.bind('<FocusOut>', lambda event: verificar_entrada_data(event, entry_DATA_INICIAL_PARCEIRA)) 

    #Inicio da parcceria 
    label_DATA_DISTRATO_PARCEIRA = ctk.CTkLabel(FrameContrato, text="Data do Distrato")
    entry_DATA_DISTRATO_PARCEIRA = ctk.CTkEntry(FrameContrato)
    label_DATA_DISTRATO_PARCEIRA.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    entry_DATA_DISTRATO_PARCEIRA.grid(row=5, column=1, padx=10, pady=5, sticky="nsew") 
    entry_DATA_DISTRATO_PARCEIRA.bind('<FocusOut>', lambda event: verificar_entrada_data(event, entry_DATA_DISTRATO_PARCEIRA))

    Validaçao = (FrameContrato.register(validar_entrada_Numero_7Caracter), '%P')
    #Cnae profissional parceiro ####-#/##  
    label_CNAE = ctk.CTkLabel(FrameContrato, text="CNAE (Ativdade da parceira)")
    entry_CNAE = ctk.CTkEntry(FrameContrato,validate='key', validatecommand=Validaçao)
    label_CNAE.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    entry_CNAE.grid(row=4, column=3, padx=10, pady=5, sticky="nsew")
    
    bt_add = ctk.CTkButton(FrameContrato,image=logo_add, text="Adicionar",command=adicionarcnae)
    bt_add.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    
    bt_Excluir_cnae = ctk.CTkButton(FrameContrato,image=logo_excluir, text="Excluir",command=excluircnae)
    bt_Excluir_cnae.grid(row=5, column=3, padx=10, pady=5, sticky="nsew")
    bt_Excluir_cnae.configure(state='disabled')

        
    listboxCnae = tk.Listbox(FrameContrato,height=3)
    listboxCnae.grid(row=4, column=5,rowspan=2, padx=10, pady=5, sticky="nsew")
    listboxCnae.bind('<<ListboxSelect>>',AtivarBTExcluir_Cnae)
    
    

    ## Servicos Frame
    FrameServicos = ctk.CTkFrame(FrameDadosContratoParceira, border_width=largura_borda, border_color=cor_de_borda)
    FrameServicos.grid(row=5, column=0, columnspan=8, padx=10, pady=5, sticky="nsew")

    label_TP_REPASSE = ctk.CTkLabel(FrameServicos, text="Selecionar repasse")
    label_TP_REPASSE.grid(row=5, column=0, padx=10, sticky="w")
   

    TP_REPASSE_var = ctk.StringVar(value="Percentual")
    Menu_TP_REPASSE = ctk.CTkOptionMenu(FrameServicos,values=["Percentual", "Valor"],
                                            command=SelecaoMenu,
                                            variable=TP_REPASSE_var)
    Menu_TP_REPASSE.grid(row=6, column=0, padx=10, pady=5, sticky="new")
    
    
    ##NOME SERVICO ------------------------------------------
    label_NOME_SERVICO = ctk.CTkLabel(FrameServicos, text="Serviço")
    entry_NOME_SERVICO = ctk.CTkEntry(FrameServicos)
    label_NOME_SERVICO.grid(row=7, column=0, padx=10, sticky="w")
    entry_NOME_SERVICO.grid(row=8, column=0, padx=10, pady=5, sticky="new") 
    ValidarapenasNumeroeponto = FrameServicos.register(Somentenumeroevigula)
    ##PERCENTUAL REPASSE SALAO ------------------------------------------
    label_REPASSE_SALAO = ctk.CTkLabel(FrameServicos, text="Percentual Salão")
    entry_REPASSE_SALAO = ctk.CTkEntry(FrameServicos, validate="key", validatecommand=(ValidarapenasNumeroeponto, "%P"))
    label_REPASSE_SALAO.grid(row=9, column=0, padx=10, sticky="w")
    entry_REPASSE_SALAO.grid(row=10, column=0, padx=10, pady=5, sticky="new") 
    
    ##PERCENTUAL REPASSE PROFISSIONAL ------------------------------------------
    label_REPASSE_PROFISSIONAL = ctk.CTkLabel(FrameServicos, text="Percentual Profissional")
    entry_REPASSE_PROFISSIONAL = ctk.CTkEntry(FrameServicos, validate="key", validatecommand=(ValidarapenasNumeroeponto, "%P"))
    label_REPASSE_PROFISSIONAL.grid(row=11, column=0, padx=10, sticky="w")
    entry_REPASSE_PROFISSIONAL.grid(row=12, column=0, padx=10, pady=5, sticky="new") 
    
    bt_add = ctk.CTkButton(FrameServicos,image=logo_add, text="Adicionar",command=VerificarSomaPercentual)
    bt_add.grid(row=13, column=0, padx=10, pady=5, sticky="new")

  
    #TREEVIEW SERVICOS ----------------------------------------------------------------------------
    TreeViewServicos = ttk.Treeview(FrameServicos, columns=("Tipo","Serviço","Salão","Profissional"), show='headings',height=14)
    TreeViewServicos.grid(row=6, rowspan=8,column=1,columnspan=5, sticky="new", padx=(5,5), pady=(5,5))
    TreeViewServicos.bind('<<TreeviewSelect>>',AtivarBTExcluir_Repasse)

    TreeViewServicos.heading("Tipo", text="Tipo")
    TreeViewServicos.heading("Serviço", text="Serviço")
    TreeViewServicos.heading("Salão", text="Salão")
    TreeViewServicos.heading("Profissional", text="Profissional")

    TreeViewServicos.column("Tipo", width=150)  # 
    TreeViewServicos.column("Serviço", width=200)  # 
    TreeViewServicos.column("Salão", width=150)  # 
    TreeViewServicos.column("Profissional", width=150)  # 

    #SCROLL BAR DOS SERVICOS --------------------------------------------------------------------
    scrollbarServicos = ctk.CTkScrollbar(FrameServicos, command=TreeViewServicos.yview)
    scrollbarServicos.grid(row=6, rowspan=8, column=6, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeViewServicos.configure(yscrollcommand=scrollbarParceiras.set)   
    
    #BOTAO EXCLUIR SERVICOS ----------------------------------------------------------------
    
    bt_EXCLUIR_REPASSE = ctk.CTkButton(FrameServicos,image=logo_excluir, text="Excluir",command=lambda:Envio_dados_servico('DEL'))
    bt_EXCLUIR_REPASSE.grid(row=5, column=5, columnspan=2, padx=10, pady=5, sticky="new")
    bt_EXCLUIR_REPASSE.configure(state='disabled')
    
    ##  Frame----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    FrameoutrosDados_maiores = ctk.CTkFrame(FrameDadosContratoParceira, border_width=largura_borda, border_color=cor_de_borda)
    FrameoutrosDados_maiores.grid(row=6, column=0, columnspan=8, padx=10, pady=5, sticky="nsew")

    #RESPONSALVEL PELOS RECOLHIMENTOS---------------------------------------------------------------
    label_RESPONSAVEL_RECOLHIMENTO = ctk.CTkLabel(FrameoutrosDados_maiores, text="Responsável pelo recolhimento/retenção e pagamento das obrigações do PROFISSIONAL PARCEIRO")
    label_RESPONSAVEL_RECOLHIMENTO.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    RESPONSAVEL_RECOLHIMENTO_var = ctk.StringVar(value="Salão Parceiro")
    Menu_RESPONSAVEL_RECOLHIMENTO = ctk.CTkOptionMenu(FrameoutrosDados_maiores,values=['Salão Parceiro', 'Profissional Parceiro', 'Empresa Administradora', 'Contabilidade Credenciada', 'Outros'],
                                            command=SelecaoMenu,
                                            variable=RESPONSAVEL_RECOLHIMENTO_var)
    Menu_RESPONSAVEL_RECOLHIMENTO.grid(row=7, column=0, padx=10, pady=5, sticky="new")
    
    #GESTAO DE VALORES---------------------------------------------------------------
    label_GESTAO_VALORES = ctk.CTkLabel(FrameoutrosDados_maiores, text="Os valores recebidos pelo cliente final serão geridos e administrados por")
    label_GESTAO_VALORES.grid(row=8, column=0, padx=10, pady=5, sticky="w")


    ## Falta  'Empresa Admininstradora ou Gestora de Caixa' , no site precisa inserir mais dados , verificar a programação para depois incluir este item 

    GESTAO_VALORES_var = ctk.StringVar(value="Salão Parceiro")
    Menu_GESTAO_VALORES = ctk.CTkOptionMenu(FrameoutrosDados_maiores,values=['Salão Parceiro', 'Profissional Parceiro'],
                                            command=SelecaoMenu,
                                            variable=GESTAO_VALORES_var)
    Menu_GESTAO_VALORES.grid(row=9, column=0, padx=10, pady=5, sticky="new")

    

    ##  Frame ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Frame_REPASSE = ctk.CTkFrame(FrameDadosContratoParceira, border_width=largura_borda, border_color=cor_de_borda)
    Frame_REPASSE.grid(row=7, column=0, columnspan=8, padx=10, pady=5, sticky="nsew")


    #PERIODO DE REPASSE---------------------------------------------------------------
    label_PERIODO_REPASSE = ctk.CTkLabel(Frame_REPASSE, text="Periodicidade do repasse")
    label_PERIODO_REPASSE.grid(row=7, column=0, padx=10, pady=5, sticky="w")

    PERIODO_REPASSE_var = ctk.StringVar(value="Mensal")
    Menu_PERIODO_REPASSE = ctk.CTkOptionMenu(Frame_REPASSE,values=['Mensal','Quinzenal','Semanal','Diário'],
                                            command=SelecaoMenu,
                                            variable=PERIODO_REPASSE_var)
    Menu_PERIODO_REPASSE.grid(row=8, column=0, padx=10, pady=5, sticky="new")
    
    #UTILIZAR KIT PADRÃO DE MÓVEIS E UTENSÍLIOS-----------------------------------------------------
    label_BENS_MATERIAIS = ctk.CTkLabel(Frame_REPASSE, text="BENS MATERIAIS")
    #label_BENS_MATERIAIS.grid(row=7, column=1, padx=10, pady=5, columnspan=3, sticky="w")

    Sw_KIT_PADRAO = ctk.CTkSwitch(Frame_REPASSE, text="UTILIZAR KIT PADRÃO DE MÓVEIS E UTENSÍLIOS")
    #Sw_KIT_PADRAO.grid(row=8, column=1, padx=10, pady=5, columnspan=3, sticky="w")


    #--------------------------------------------------------------------------------------------  
    ## Frame-------------------------------------------------------------------------------------
    FrameoutrosDados_maiores2 = ctk.CTkFrame(FrameDadosContratoParceira, border_width=largura_borda, border_color=cor_de_borda)
    FrameoutrosDados_maiores2.grid(row=9, column=0, columnspan=8, padx=10, pady=5, sticky="nsew")
   
    #ASSESSORIA CONTABIL---------------------------------------------------------------
    label_ASSESSORIA_CONTABIL = ctk.CTkLabel(FrameoutrosDados_maiores2, text="O Profissional Parceiro possui a assessoria de uma contabilidade?")
    label_ASSESSORIA_CONTABIL.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    ASSESSORIA_CONTABIL_var = ctk.StringVar(value="Sim")
    Menu_ASSESSORIA_CONTABIL = ctk.CTkOptionMenu(FrameoutrosDados_maiores2,values=['Sim','Não'],
                                            command=contabilidadeAssessora,
                                            variable=ASSESSORIA_CONTABIL_var)
    Menu_ASSESSORIA_CONTABIL.grid(row=9, column=2, padx=10, pady=5, sticky="new")

    #NOME ASSESSORIA CONTABIL---------------------------------------------------------------
    label_CONTABILIDADE_ASSESORA = ctk.CTkLabel(FrameoutrosDados_maiores2, text="Nome")
    label_CONTABILIDADE_ASSESORA.grid(row=10, column=0, padx=10, pady=5, sticky="w")
    CONTABILIDADES_assesoras=[]
    CONTABILIDADE_ASSESORA_var = ctk.StringVar(value="")
    Menu_CONTABILIDADE_ASSESORA = ctk.CTkOptionMenu(FrameoutrosDados_maiores2,values=CONTABILIDADES_assesoras,                                           variable=CONTABILIDADE_ASSESORA_var)
    Menu_CONTABILIDADE_ASSESORA.grid(row=10, column=1, columnspan=3, padx=10, pady=5, sticky="nsew")

    bt_add = ctk.CTkButton(FrameoutrosDados_maiores2,image=logo_add,text="",command=TopLevel_CadastraCont)
    bt_add.grid(row=9, column=3, padx=10, pady=5, sticky="new")

   
   
   #------------------------------------------------------------------------------------------------#
    #Frame Dados CONTRATANTE (NAO VISIVEL NO PARCEIRA) 


    hours = [f"{i:02d}" for i in range(24)]
    minutes = [f"{i:02d}" for i in range(60)]
    dias_da_semana = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    nomes_dias = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA", "SEXTA-FEIRA", "SÁBADO", "DOMINGO"]
    tamanhohorarios = 125
    estadohorarios = 'readonly'
    

    FrameDadosContratoCONTRATANTE = ctk.CTkFrame(FramedadosComp, border_width=largura_borda, border_color=cor_de_borda)
    #FrameDadosContratoCONTRATANTE.grid(row=1, column=0, sticky="nsew", padx=(5,5), pady=(5,10))
    #label_bt = ctk.CTkButton(FrameDadosContratoCONTRATANTE, text="tt",command=verificar_dias_marcados)
    #label_bt.grid(row=0, column=1, padx=10, pady=5, columnspan=4, sticky="new")

    label_HORARIOS = ctk.CTkLabel(FrameDadosContratoCONTRATANTE, text="Horarios do salão")
    label_HORARIOS.grid(row=3, column=1, padx=10, pady=5, columnspan=4, sticky="new")


    coluna = 2
    frameColunaHorario = ctk.CTkFrame(FrameDadosContratoCONTRATANTE, border_width=largura_borda, border_color=cor_de_borda)
    frameColunaHorario.grid(row=4, column=coluna, padx=10, pady=5, sticky="new")
    Lb_abre = ctk.CTkLabel(frameColunaHorario, text="DIAS DE FUNCIONAMENTO")
    Lb_abre.grid(row=4, column=coluna, padx=10, pady=5, sticky="n")
    
    coluna = 3
    # Cria uma lista de horas e minutos
    frameColunaHorario = ctk.CTkFrame(FrameDadosContratoCONTRATANTE, border_width=largura_borda, border_color=cor_de_borda)
    frameColunaHorario.grid(row=4, column=coluna, padx=10, pady=5, sticky="new")
    Lb_abre = ctk.CTkLabel(frameColunaHorario, text="ABERTURA")
    Lb_abre.grid(row=4, column=coluna, padx=10, pady=5, sticky="nsew")

    coluna = 4
    frameColunaHorario = ctk.CTkFrame(FrameDadosContratoCONTRATANTE, border_width=largura_borda, border_color=cor_de_borda)
    frameColunaHorario.grid(row=4, column=coluna, padx=10, pady=5, sticky="new")
    Lb_abre = ctk.CTkLabel(frameColunaHorario, text="FECHAMENTO")
    Lb_abre.grid(row=4, column=coluna, padx=10, pady=5, sticky="nsew")

    # Loop para criar CheckBoxes e frames
    for i, dia in enumerate(dias_da_semana, start=5):
        # Variável e CheckBox
        coluna = 2
        globals()[f"Chk_{dia}_var"] = ctk.BooleanVar(value=False)
        globals()[f"Chk_{dia}"] = ctk.CTkCheckBox(FrameDadosContratoCONTRATANTE, text=nomes_dias[i-5], variable=globals()[f"Chk_{dia}_var"], onvalue=True, offvalue=False)
        globals()[f"Chk_{dia}"].grid(row=i, column=coluna, padx=10, pady=5, sticky="w")

        coluna = 3
        # Frames para horários de abertura
        globals()[f"frameHorarioAbertura_{dia}"] = ctk.CTkFrame(FrameDadosContratoCONTRATANTE, border_width=largura_borda, border_color=cor_de_borda)
        globals()[f"frameHorarioAbertura_{dia}"].grid(row=i, column=coluna, padx=10, pady=5, sticky="new")
        # ComboBox para horários de abertura 
        globals()[f"Hora_Abertura_{dia}"] = ctk.CTkComboBox(globals()[f"frameHorarioAbertura_{dia}"], values=hours, state=estadohorarios, width=tamanhohorarios)
        globals()[f"Hora_Abertura_{dia}"].set("00")  # Define valor padrão
        globals()[f"Hora_Abertura_{dia}"].grid(row=0, column=0, padx=10, pady=5, sticky="new")
        globals()[f"Hora_Abertura_{dia}"].configure(state="disabled")
        # ComboBox para Minutos de abertura 
        globals()[f"Min_Abertura_{dia}"] = ctk.CTkComboBox(globals()[f"frameHorarioAbertura_{dia}"], values=minutes, state=estadohorarios, width=tamanhohorarios)
        globals()[f"Min_Abertura_{dia}"].set("00")  # Define valor padrão
        globals()[f"Min_Abertura_{dia}"].grid(row=0, column=1, padx=10, pady=5, sticky="new")
        globals()[f"Min_Abertura_{dia}"].configure(state="disabled")


        coluna = 4
        # Frames para horários de fechamento
        globals()[f"frameHorarioFechamento_{dia}"] = ctk.CTkFrame(FrameDadosContratoCONTRATANTE, border_width=largura_borda, border_color=cor_de_borda)
        globals()[f"frameHorarioFechamento_{dia}"].grid(row=i, column=coluna, padx=10, pady=5, sticky="new")  # Ajuste o valor de 'i+7' conforme necessário
        # ComboBox para horários de fechamento
        globals()[f"Hora_Fechamento_{dia}"] = ctk.CTkComboBox(globals()[f"frameHorarioFechamento_{dia}"], values=hours, state=estadohorarios, width=tamanhohorarios)
        globals()[f"Hora_Fechamento_{dia}"].set("00")  # Define valor padrão
        globals()[f"Hora_Fechamento_{dia}"].grid(row=0, column=0, padx=10, pady=5, sticky="new")
        globals()[f"Hora_Fechamento_{dia}"].configure(state="disabled")
        # ComboBox para Minutos de abertura 
        globals()[f"Min_Fechamento_{dia}"] = ctk.CTkComboBox(globals()[f"frameHorarioFechamento_{dia}"], values=minutes, state=estadohorarios, width=tamanhohorarios)
        globals()[f"Min_Fechamento_{dia}"].set("00")  # Define valor padrão
        globals()[f"Min_Fechamento_{dia}"].grid(row=0, column=1, padx=10, pady=5, sticky="new")
        globals()[f"Min_Fechamento_{dia}"].configure(state="disabled")

    for dia in dias_da_semana:
        globals()[f"Chk_{dia}"].configure(command=lambda d=dia: ativardia(f"Chk_{d}", d))


   


  


    
    
#novos Campos em 22/05    
#nome_fantasia  
#razao_Social
#celular
#cep
#rua
#numero
#complemento
#bairro
#cidade
#estado
#senha_certificado
#liberação_nf
#nome_pessoa
#sobrenome
#nome_mae
#estado_civil
#genero
#data_nascimento
#numero_rg
#orgao_rg
#data_expedicao_rg
#modelo_contrato
#data_inicio_parceria
#cnae
#responsavel_recolhimento
#valores_recebidos_adm
#repasse
#kit_padrao
#assessoria_contabil
#nome_assessoria_contabil
#dias_abertura
#hora_seg
#hora_ter
#hora_qua
#hora_qui
#hora_sex
#hora_sab
#hora_dom

#reponsavel contabil (nome,cnpj,telefone)(Outra Tabela)

#servicos (Outra Tabela ?)



