import customtkinter as ctk
import tkinter
from tkinter import *
import Modulos.Database.Clients as dbc


def criarbotoes(Viewer):
    global NumeroID,entry_Nome_empresa,entry_CNPJ,entry_Estado,entry_Municpio,entry_Atividade,entry_Data_abertura_,entry_Ativo,entry_Link_WhatsApp,entry_Formas_de_tributao,entry_Anexo_simples_nacional,entry_Folha_de_pagamento,entry_Responsvel_contabil,entry_Responsvel_fiscal,entry_Responsvel_societrio,entry_Responsvel_DP,entry_Domiclio_eletrnico,entry_Email,entry_Nome_representante,entry_CPF_representante_legal,entry_Data_de_nascimento_,entry_Contabilidade_finalizada_,entry_Certificado_digital,entry_Senha_certificado,entry_Data_de_vencimento_,entry_Cdigo_e_cac,entry_Senha_EAC,entry_Cdigo_Simples,entry_Nmero_de_livros_ECD,entry_Ano_Nmero_de_livros_ECD,entry_Nmero_de_livros_ECF,entry_Ano_Nmero_de_livros_ECF,entry_UF,entry_Inscrio_estadual,entry_Credenciamento_NFE,entry_Nmero_CSC,entry_Site_caixa_postal,entry_Livros_Fiscais_Entrada_Ano_Nmero,entry_Livros_Fiscais_Inventrio_Ano_Nmero,entry_Inscrio_municipal,entry_Site,entry_Login,entry_Senha,entry_Demais_senhas,entry_Senha_Abertura_Processos,entry_Observaes,entry_Alvara_de_funcionamento,entry_Data_vencimento_,entry_Alvara_sanitrio,entry_Licenca_ambiental,entry_Bombeiros,entry_ltima_alterao_contratual_,entry_Nmero_alterao_contratual,entry_Observaes_gerais,entry_Folha_de_pagto,entry_Quantidade_de_funcionrios,entry_Prolabore,entry_Quantidade_de_scios,entry_Esocial_usurio,entry_Esocial_senha,entry_Esocial_cdigo_de_acesso,entry_FAP_usurio,entry_FAP_senha,entry_Empregador_WEB_usurio,entry_Empregador_WEB_senha,entry_Sistema,entry_Site_Bpo,entry_Usurio,entry_Senha_simples,entry_Banco_1,entry_Banco_2,entry_Tipo_de_BPO,entry_Estado_estaduais,entry_Observaes_gerais_Societario,entry_Observaes_gerais_bpo

    formasdetributacao = [
        "SIMPLES NACIONAL","MEI","PRESUMIDO","LUCRO REAL","IMUNE/ISENTA"
    ]

#------------------------------cliente
    siglas_estados = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ]
    yes_or_not = [
        "SIM","NÃO"
    ]
    NumeroID = ctk.CTkLabel(Viewer.tab("Cliente"), text="ID")
    NumeroID.grid(row=0, column=1,columnspan=1, padx=10, pady=1, sticky="w")

    label_Nome_empresa = ctk.CTkLabel(Viewer.tab("Cliente"), text="Nome empresa")
    entry_Nome_empresa = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Nome_empresa.grid(row=0, column=0,columnspan=1, padx=10, pady=1, sticky="w")
    entry_Nome_empresa.grid(row=1, column=0,columnspan=3, padx=10, pady=15, sticky="nsew")

    
    label_CNPJ = ctk.CTkLabel(Viewer.tab("Cliente"), text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_CNPJ.grid(row=0, column=3, padx=10, pady=1, sticky="w")
    entry_CNPJ.grid(row=1, column=3, padx=10, pady=15, sticky="nsew")


    label_Estado = ctk.CTkLabel(Viewer.tab("Cliente"), text="Estado")
    entry_Estado = ctk.CTkComboBox(Viewer.tab("Cliente"),values= siglas_estados)

    label_Estado.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    entry_Estado.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")
    #entry_Estado.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="nsew")

    label_Municpio = ctk.CTkLabel(Viewer.tab("Cliente"), text="Município")
    entry_Municpio = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Municpio.grid(row=2, column=2, padx=10, pady=1, sticky="w")
    entry_Municpio.grid(row=3, column=2, padx=10, pady=15, sticky="nsew")


    label_Atividade = ctk.CTkLabel(Viewer.tab("Cliente"), text="Atividade")
    entry_Atividade = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Atividade.grid(row=2, column=0, padx=10, pady=1, sticky="w")
    entry_Atividade.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")


    label_Data_abertura_ = ctk.CTkLabel(Viewer.tab("Cliente"), text="Data abertura")
    entry_Data_abertura_ = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Data_abertura_.grid(row=2, column=3, padx=10, pady=1, sticky="w")
    entry_Data_abertura_.grid(row=3, column=3, padx=10, pady=15, sticky="nsew")


    label_Ativo = ctk.CTkLabel(Viewer.tab("Cliente"), text="Ativo")
    entry_Ativo = ctk.CTkComboBox(Viewer.tab("Cliente"),values=yes_or_not)
    
    label_Ativo.grid(row=4, column=3, padx=10, pady=1, sticky="w")
    entry_Ativo.grid(row=5, column=3, padx=10, pady=15, sticky="nsew")


    label_Link_WhatsApp = ctk.CTkLabel(Viewer.tab("Cliente"), text="Link WhatsApp")
    entry_Link_WhatsApp = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Link_WhatsApp.grid(row=4, column=0,columnspan=3, padx=10, pady=1, sticky="w")
    entry_Link_WhatsApp.grid(row=5, column=0,columnspan=3, padx=10, pady=15, sticky="nsew")

#------------------------------Gerais

    label_Formas_de_tributao = ctk.CTkLabel(Viewer.tab("Gerais"), text="Formas de tributação")
    entry_Formas_de_tributao = ctk.CTkComboBox(Viewer.tab("Gerais"), width=165,values=formasdetributacao)

    label_Formas_de_tributao.grid(row=0, column=0, padx=10, pady=3, sticky="w")
    entry_Formas_de_tributao.grid(row=0, column=1, padx=10, pady=3, sticky="nsew")


    label_Anexo_simples_nacional = ctk.CTkLabel(Viewer.tab("Gerais"), text="Anexo simples nacional")
    entry_Anexo_simples_nacional = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Anexo_simples_nacional.grid(row=1, column=0, padx=10, pady=3, sticky="w")
    entry_Anexo_simples_nacional.grid(row=1, column=1, padx=10, pady=3, sticky="nsew")

    yes_or_not = [
       "NÃO", "SIM"
    ]
    label_Folha_de_pagamento = ctk.CTkLabel(Viewer.tab("Gerais"), text="Folha de pagamento")
    entry_Folha_de_pagamento = ctk.CTkComboBox(Viewer.tab("Gerais"), width=165,values=yes_or_not)

    label_Folha_de_pagamento.grid(row=2, column=0, padx=10, pady=3, sticky="w")
    entry_Folha_de_pagamento.grid(row=2, column=1, padx=10, pady=3, sticky="nsew")


    label_Responsvel_contabil = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável contabil")
    entry_Responsvel_contabil = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Responsvel_contabil.grid(row=3, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_contabil.grid(row=3, column=1, padx=10, pady=3, sticky="nsew")


    label_Responsvel_fiscal = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável fiscal")
    entry_Responsvel_fiscal = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Responsvel_fiscal.grid(row=4, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_fiscal.grid(row=4, column=1, padx=10, pady=3, sticky="nsew")


    label_Responsvel_societrio = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável societário")
    entry_Responsvel_societrio = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Responsvel_societrio.grid(row=5, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_societrio.grid(row=5, column=1, padx=10, pady=3, sticky="nsew")


    label_Responsvel_DP = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável DP")
    entry_Responsvel_DP = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Responsvel_DP.grid(row=6, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_DP.grid(row=6, column=1, padx=10, pady=3, sticky="nsew")

    

    label_Domiclio_eletrnico = ctk.CTkLabel(Viewer.tab("Gerais"), text="Domicílio eletrônico")
    entry_Domiclio_eletrnico = ctk.CTkComboBox(Viewer.tab("Gerais"), width=165,values=yes_or_not)

    label_Domiclio_eletrnico.grid(row=7, column=0, padx=10, pady=3, sticky="w")
    entry_Domiclio_eletrnico.grid(row=7, column=1, padx=10, pady=3, sticky="nsew")


    label_Email = ctk.CTkLabel(Viewer.tab("Gerais"), text="Email")
    entry_Email = ctk.CTkEntry(Viewer.tab("Gerais"), width=250)

    label_Email.grid(row=8, column=0, padx=10, pady=3, sticky="w")
    entry_Email.grid(row=8, column=1,columnspan=2, padx=10, pady=3, sticky="nsew")


    label_Nome_representante = ctk.CTkLabel(Viewer.tab("Gerais"), text="Nome representante")
    entry_Nome_representante = ctk.CTkEntry(Viewer.tab("Gerais"), width=250)

    label_Nome_representante.grid(row=9, column=0, padx=10, pady=3, sticky="w")
    entry_Nome_representante.grid(row=9, column=1,columnspan=2, padx=10, pady=3, sticky="nsew")


    label_CPF_representante_legal = ctk.CTkLabel(Viewer.tab("Gerais"), text="CPF representante legal")
    entry_CPF_representante_legal = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_CPF_representante_legal.grid(row=0, column=2, padx=10, pady=3, sticky="w")
    entry_CPF_representante_legal.grid(row=0, column=3, padx=10, pady=3, sticky="nsew")


    label_Data_de_nascimento_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Data de nascimento (dd/mm/aaaa)")
    entry_Data_de_nascimento_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Data_de_nascimento_.grid(row=1, column=2, padx=10, pady=3, sticky="w")
    entry_Data_de_nascimento_.grid(row=1, column=3, padx=10, pady=3, sticky="nsew")


    label_Contabilidade_finalizada_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Contabilidade finalizada (dd/mm/aaaa)")
    entry_Contabilidade_finalizada_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Contabilidade_finalizada_.grid(row=2, column=2, padx=10, pady=3, sticky="w")
    entry_Contabilidade_finalizada_.grid(row=2, column=3, padx=10, pady=3, sticky="nsew")


    label_Certificado_digital = ctk.CTkLabel(Viewer.tab("Gerais"), text="Certificado digital")
    entry_Certificado_digital = ctk.CTkComboBox(Viewer.tab("Gerais"), width=165,values=yes_or_not)

    label_Certificado_digital.grid(row=3, column=2, padx=10, pady=3, sticky="w")
    entry_Certificado_digital.grid(row=3, column=3, padx=10, pady=3, sticky="nsew")


    label_Senha_certificado = ctk.CTkLabel(Viewer.tab("Gerais"), text="Senha certificado")
    entry_Senha_certificado = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Senha_certificado.grid(row=4, column=2, padx=10, pady=3, sticky="w")
    entry_Senha_certificado.grid(row=4, column=3, padx=10, pady=3, sticky="nsew")


    label_Data_de_vencimento_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Data de vencimento (dd/mm/aaaa)")
    entry_Data_de_vencimento_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=165)

    label_Data_de_vencimento_.grid(row=5, column=2, padx=10, pady=3, sticky="w")
    entry_Data_de_vencimento_.grid(row=5, column=3, padx=10, pady=3, sticky="nsew")

#------------------------------Federais

    frame_federais=ctk.CTkFrame(Viewer.tab("Federais"),fg_color="RED")
    frame_federais.grid(row=0, column=0, padx=5, pady=1, sticky="nsew")

    


    label_Cdigo_e_cac = ctk.CTkLabel(frame_federais, text="Código e-cac")
    entry_Cdigo_e_cac = ctk.CTkEntry(frame_federais, width=200)

    label_Cdigo_e_cac.grid(row=0, column=0, padx=5, pady=1, sticky="nsew")
    entry_Cdigo_e_cac.grid(row=1, column=0, padx=5, pady=1, sticky="w")


    label_Senha_EAC = ctk.CTkLabel(frame_federais, text="Senha EAC")
    entry_Senha_EAC = ctk.CTkEntry(frame_federais, width=200)

    label_Senha_EAC.grid(row=0, column=1, padx=5, pady=1, sticky="nsew")
    entry_Senha_EAC.grid(row=1, column=1, padx=5, pady=1, sticky="w")


    label_Cdigo_Simples = ctk.CTkLabel(frame_federais, text="Código Simples")
    entry_Cdigo_Simples = ctk.CTkEntry(frame_federais, width=200)

    label_Cdigo_Simples.grid(row=0, column=2, padx=5, pady=1, sticky="nsew")
    entry_Cdigo_Simples.grid(row=1, column=2, padx=5, pady=1, sticky="w")

    tab_livros=ctk.CTkTabview(frame_federais)
    tab_livros.grid(row=3, column=0,columnspan=3, padx=5, pady=1, sticky="nsew")
    tab_livros.add("livros ECD")
    tab_livros.tab("livros ECD").grid_columnconfigure(0,weight=1)
    tab_livros.add("livros ECF")
    tab_livros.tab("livros ECF").grid_columnconfigure(0,weight=1)

    label_Nmero_de_livros_ECD = ctk.CTkLabel(tab_livros.tab("livros ECD"), text="Numero")
    entry_Nmero_de_livros_ECD = ctk.CTkEntry(tab_livros.tab("livros ECD"), width=200)

    label_Nmero_de_livros_ECD.grid(row=0, column=0, padx=5, pady=1, sticky="nsew")
    entry_Nmero_de_livros_ECD.grid(row=1, column=0, padx=5, pady=1, sticky="w")


    label_Ano_Nmero_de_livros_ECD = ctk.CTkLabel(tab_livros.tab("livros ECD"), text="Ano")
    entry_Ano_Nmero_de_livros_ECD = ctk.CTkEntry(tab_livros.tab("livros ECD"), width=200)

    label_Ano_Nmero_de_livros_ECD.grid(row=0, column=1, padx=5, pady=1, sticky="nsew")
    entry_Ano_Nmero_de_livros_ECD.grid(row=1, column=1, padx=5, pady=1, sticky="w")


    label_Nmero_de_livros_ECF = ctk.CTkLabel(tab_livros.tab("livros ECF"), text="Numero")
    entry_Nmero_de_livros_ECF = ctk.CTkEntry(tab_livros.tab("livros ECF"), width=200)

    label_Nmero_de_livros_ECF.grid(row=2, column=1, padx=5, pady=1, sticky="nsew")
    entry_Nmero_de_livros_ECF.grid(row=3, column=1, padx=5, pady=1, sticky="w")


    label_Ano_Nmero_de_livros_ECF = ctk.CTkLabel(tab_livros.tab("livros ECF"), text="Ano")
    entry_Ano_Nmero_de_livros_ECF = ctk.CTkEntry(tab_livros.tab("livros ECF"), width=200)

    label_Ano_Nmero_de_livros_ECF.grid(row=4, column=1, padx=5, pady=1, sticky="nsew")
    entry_Ano_Nmero_de_livros_ECF.grid(row=5, column=1, padx=5, pady=1, sticky="w")

#------------------------------Estaduais

    label_Estado_estaduais = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Estado")
    entry_Estado_estaduais = ctk.CTkComboBox(Viewer.tab("Estaduais"), width=200,values=siglas_estados)

    label_Estado_estaduais.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Estado_estaduais.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")


    label_Inscrio_estadual = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Inscrição estadual")
    entry_Inscrio_estadual = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Inscrio_estadual.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Inscrio_estadual.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")


    label_Credenciamento_NFE = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Credenciamento NFE")
    entry_Credenciamento_NFE = ctk.CTkComboBox(Viewer.tab("Estaduais"), width=50,values=yes_or_not)

    label_Credenciamento_NFE.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    entry_Credenciamento_NFE.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Nmero_CSC = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Número CSC")
    entry_Nmero_CSC = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Nmero_CSC.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Nmero_CSC.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")


    label_Site_caixa_postal = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Site caixa postal")
    entry_Site_caixa_postal = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Site_caixa_postal.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")
    entry_Site_caixa_postal.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Livros_Fiscais_Entrada_Ano_Nmero = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Livros Fiscais Entrada Ano Número")
    entry_Livros_Fiscais_Entrada_Ano_Nmero = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Livros_Fiscais_Entrada_Ano_Nmero.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Livros_Fiscais_Entrada_Ano_Nmero.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")


    label_Livros_Fiscais_Inventrio_Ano_Nmero = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Livros Fiscais Inventário Ano Número")
    entry_Livros_Fiscais_Inventrio_Ano_Nmero = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Livros_Fiscais_Inventrio_Ano_Nmero.grid(row=7, column=0, padx=10, pady=15, sticky="nsew")
    entry_Livros_Fiscais_Inventrio_Ano_Nmero.grid(row=7, column=1, padx=10, pady=15, sticky="nsew")

#------------------------------Municipais

    label_Inscrio_municipal = ctk.CTkLabel(Viewer.tab("Municipais"), text="Inscrição municipal")
    entry_Inscrio_municipal = ctk.CTkEntry(Viewer.tab("Municipais"), width=100)

    label_Inscrio_municipal.grid(row=0, column=0, padx=10, pady=15, sticky="w")
    entry_Inscrio_municipal.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")


    label_Site = ctk.CTkLabel(Viewer.tab("Municipais"), text="Site")
    entry_Site = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Site.grid(row=2, column=0, padx=10, pady=1, sticky="w")
    entry_Site.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")


    label_Login = ctk.CTkLabel(Viewer.tab("Municipais"), text="Login")
    entry_Login = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Login.grid(row=4, column=0, padx=10, pady=1, sticky="w")
    entry_Login.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")


    label_Senha = ctk.CTkLabel(Viewer.tab("Municipais"), text="Senha")
    entry_Senha = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Senha.grid(row=6, column=0, padx=10, pady=1, sticky="w")
    entry_Senha.grid(row=7, column=0, padx=10, pady=15, sticky="nsew")


    label_Demais_senhas = ctk.CTkLabel(Viewer.tab("Municipais"), text="Demais senhas")
    entry_Demais_senhas = ctk.CTkEntry(Viewer.tab("Municipais"), width=300)

    label_Demais_senhas.grid(row=0, column=1, padx=10, pady=1, sticky="w")
    entry_Demais_senhas.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Senha_Abertura_Processos = ctk.CTkLabel(Viewer.tab("Municipais"), text="Senha Abertura Processos")
    entry_Senha_Abertura_Processos = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Senha_Abertura_Processos.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    entry_Senha_Abertura_Processos.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Observaes = ctk.CTkLabel(Viewer.tab("Municipais"), text="Observações")
    entry_Observaes = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Observaes.grid(row=4, column=1, padx=10, pady=1, sticky="w")
    entry_Observaes.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")

#------------------------------Societario

    label_Alvara_de_funcionamento = ctk.CTkLabel(Viewer.tab("Societário"), text="Alvara de funcionamento")
    entry_Alvara_de_funcionamento = ctk.CTkComboBox(Viewer.tab("Societário"), width=300,values=yes_or_not)

    label_Alvara_de_funcionamento.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Alvara_de_funcionamento.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Alvara_sanitrio = ctk.CTkLabel(Viewer.tab("Societário"), text="Alvara sanitário")
    entry_Alvara_sanitrio = ctk.CTkComboBox(Viewer.tab("Societário"), width=50,values=yes_or_not)

    label_Alvara_sanitrio.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Alvara_sanitrio.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_Licenca_ambiental = ctk.CTkLabel(Viewer.tab("Societário"), text="Licença ambiental")
    entry_Licenca_ambiental = ctk.CTkComboBox(Viewer.tab("Societário"), width=50,values=yes_or_not)

    label_Licenca_ambiental.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Licenca_ambiental.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Bombeiros = ctk.CTkLabel(Viewer.tab("Societário"), text="Bombeiros")
    entry_Bombeiros = ctk.CTkComboBox(Viewer.tab("Societário"), width=50,values=yes_or_not)

    label_Bombeiros.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Bombeiros.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_ltima_alterao_contratual_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Última alteração contratual (dd/mm/aaaa)")
    entry_ltima_alterao_contratual_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_ltima_alterao_contratual_.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_ltima_alterao_contratual_.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")


    label_Nmero_alterao_contratual = ctk.CTkLabel(Viewer.tab("Societário"), text="Número alteração contratual")
    entry_Nmero_alterao_contratual = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Nmero_alterao_contratual.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Nmero_alterao_contratual.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")


    label_Observaes_gerais_Societario = ctk.CTkLabel(Viewer.tab("Societário"), text="Observações gerais")
    entry_Observaes_gerais_Societario = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Observaes_gerais_Societario.grid(row=10, column=0, padx=10, pady=5, sticky="nsew")
    entry_Observaes_gerais_Societario.grid(row=10, column=1, padx=10, pady=5, sticky="nsew")

#------------------------------DP Pessoal

    label_Folha_de_pagto = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Folha de pagto")
    entry_Folha_de_pagto = ctk.CTkComboBox(Viewer.tab("Departamento pessoal"), width=50,values=yes_or_not)

    label_Folha_de_pagto.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Folha_de_pagto.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Quantidade_de_funcionrios = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Quantidade de funcionários")
    entry_Quantidade_de_funcionrios = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Quantidade_de_funcionrios.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Quantidade_de_funcionrios.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")


    label_Prolabore = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Prolabore")
    entry_Prolabore = ctk.CTkComboBox(Viewer.tab("Departamento pessoal"), width=50,values=yes_or_not)

    label_Prolabore.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_Prolabore.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")


    label_Quantidade_de_scios = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Quantidade de sócios")
    entry_Quantidade_de_scios = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Quantidade_de_scios.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    entry_Quantidade_de_scios.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")


    label_Esocial_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial usuário")
    entry_Esocial_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Esocial_usurio.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    entry_Esocial_usurio.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")


    label_Esocial_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial senha")
    entry_Esocial_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Esocial_senha.grid(row=10, column=0, padx=10, pady=5, sticky="w")
    entry_Esocial_senha.grid(row=11, column=0, padx=10, pady=5, sticky="nsew")


    label_Esocial_cdigo_de_acesso = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial código de acesso")
    entry_Esocial_cdigo_de_acesso = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=350)

    label_Esocial_cdigo_de_acesso.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_Esocial_cdigo_de_acesso.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_FAP_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="FAP usuário")
    entry_FAP_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_FAP_usurio.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entry_FAP_usurio.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_FAP_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="FAP senha")
    entry_FAP_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_FAP_senha.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    entry_FAP_senha.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Empregador_WEB_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Empregador WEB usuário")
    entry_Empregador_WEB_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Empregador_WEB_usurio.grid(row=6, column=1, padx=10, pady=5, sticky="w")
    entry_Empregador_WEB_usurio.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_Empregador_WEB_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Empregador WEB senha")
    entry_Empregador_WEB_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Empregador_WEB_senha.grid(row=8, column=1, padx=10, pady=5, sticky="w")
    entry_Empregador_WEB_senha.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")

#------------------------------BPO

    label_Sistema = ctk.CTkLabel(Viewer.tab("BPO"), text="Sistema")
    entry_Sistema = ctk.CTkEntry(Viewer.tab("BPO"), width=200)

    label_Sistema.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Sistema.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")


    label_Site_Bpo = ctk.CTkLabel(Viewer.tab("BPO"), text="Site")
    entry_Site_Bpo = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Site_Bpo.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Site_Bpo.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")


    label_Usuario = ctk.CTkLabel(Viewer.tab("BPO"), text="Usuário")
    entry_Usurio = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Usuario.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Usurio.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")


    label_Senha_simples = ctk.CTkLabel(Viewer.tab("BPO"), text="Senha simples")
    entry_Senha_simples = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Senha_simples.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Senha_simples.grid(row=7, column=0, padx=10, pady=15, sticky="nsew")


    label_Banco_1 = ctk.CTkLabel(Viewer.tab("BPO"), text="Banco 1")
    entry_Banco_1 = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Banco_1.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")
    entry_Banco_1.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Banco_2 = ctk.CTkLabel(Viewer.tab("BPO"), text="Banco 2")
    entry_Banco_2 = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Banco_2.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")
    entry_Banco_2.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Tipo_de_BPO = ctk.CTkLabel(Viewer.tab("BPO"), text="Tipo de BPO")
    entry_Tipo_de_BPO = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Tipo_de_BPO.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")
    entry_Tipo_de_BPO.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Observaes_gerais_bpo = ctk.CTkLabel(Viewer.tab("BPO"), text="Observações gerais")
    entry_Observaes_gerais_bpo = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Observaes_gerais_bpo.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")
    entry_Observaes_gerais_bpo.grid(row=7, column=1, padx=10, pady=15, sticky="nsew")



def Importardados(idcliente):
    Listadedados, identificadores,qr = dbc.getclientdata_toEdit(idcliente)
    

    ### Cliente
    NumeroID.configure(text=f"ID Cliente: {Listadedados[0]}" ) # Campo id do banco de dados
    
    entry_Nome_empresa.delete(0, 'end')
    entry_Nome_empresa.insert(0,Listadedados[1]) # Campo nome_empresa do banco de dados
    
    entry_CNPJ.delete(0, 'end')
    entry_CNPJ.insert(0,Listadedados[2]) # Campo cnpj do banco de dados
    
    entry_Estado.set(Listadedados[3]) # Campo uf do banco de dados
    
    entry_Municpio.delete(0, 'end')
    entry_Municpio.insert(0,Listadedados[4]) # Campo municipio do banco de dados
    
    entry_Atividade.delete(0, 'end')
    entry_Atividade.insert(0,Listadedados[5]) # Campo atividade do banco de dados
   
    entry_Data_abertura_.delete(0, 'end')
    entry_Data_abertura_.insert(0,Listadedados[6]) # Campo data_abertura do banco de dados
    
    entry_Ativo.set(Listadedados[7]) # Campo ativo do banco de dados
    
    entry_Link_WhatsApp.delete(0, 'end')
    entry_Link_WhatsApp.insert(0,Listadedados[68])# Campo link_whatsapp do banco de dados

    ### Gerais
    entry_Anexo_simples_nacional.delete(0, 'end')
    entry_Responsvel_contabil.delete(0, 'end')
    entry_Responsvel_fiscal.delete(0, 'end')
    entry_Responsvel_societrio.delete(0, 'end')
    entry_Responsvel_DP.delete(0, 'end')
    entry_Email.delete(0, 'end')
    entry_Nome_representante.delete(0, 'end')
    entry_CPF_representante_legal.delete(0, 'end')
    entry_Data_de_nascimento_.delete(0, 'end')
    entry_Contabilidade_finalizada_.delete(0, 'end')
    entry_Senha_certificado.delete(0, 'end')
    entry_Data_de_vencimento_.delete(0, 'end')

    entry_Formas_de_tributao.set(Listadedados[8].upper()) # Campo formas_tributacao do banco de dados
    entry_Anexo_simples_nacional.insert(0,Listadedados[9]) # Campo anexo_simples_nacional do banco de dados
    entry_Folha_de_pagamento.set(Listadedados[10]) # Campo folha_pagamento do banco de dados
    entry_Responsvel_contabil.insert(0,Listadedados[11]) # Campo responsavel_contabil do banco de dados
    entry_Responsvel_fiscal.insert(0,Listadedados[12]) # Campo responsavel_fiscal do banco de dados
    entry_Responsvel_societrio.insert(0,Listadedados[13]) # Campo responsavel_societario do banco de dados
    entry_Responsvel_DP.insert(0,Listadedados[14]) # Campo responsavel_dp do banco de dados
    entry_Domiclio_eletrnico.set(Listadedados[15]) # Campo domicilio_eletronico do banco de dados
    entry_Email.insert(0,Listadedados[16]) # Campo email do banco de dados
    entry_Nome_representante.insert(0,Listadedados[17]) # Campo nome_representante do banco de dados
    entry_CPF_representante_legal.insert(0,Listadedados[18]) # Campo cpf_representante_legal do banco de dados
    entry_Data_de_nascimento_.insert(0,Listadedados[19]) # Campo data_nascimento do banco de dados
    entry_Contabilidade_finalizada_.insert(0,Listadedados[20]) # Campo contabilidade_finalizada do banco de dados
    entry_Certificado_digital.set(Listadedados[21]) # Campo certificado_digital do banco de dados
    entry_Senha_certificado.insert(0,Listadedados[22]) # Campo senha_certificado do banco de dados
    entry_Data_de_vencimento_.insert(0,Listadedados[23]) # Campo data_vencimento_certificado do banco de dados
    
    ###Federais
    
    entry_Cdigo_e_cac.delete(0, 'end')
    entry_Senha_EAC.delete(0, 'end')
    entry_Cdigo_Simples.delete(0, 'end')
    entry_Nmero_de_livros_ECD.delete(0, 'end')
    entry_Ano_Nmero_de_livros_ECD.delete(0, 'end')
    entry_Nmero_de_livros_ECF.delete(0, 'end')
    entry_Ano_Nmero_de_livros_ECF.delete(0, 'end')

    entry_Cdigo_e_cac.insert(0,Listadedados[24]) # Campo codigo_ecac do banco de dados
    entry_Senha_EAC.insert(0,Listadedados[25]) # Campo senha_ecac do banco de dados
    entry_Cdigo_Simples.insert(0,Listadedados[26]) # Campo codigo_simples do banco de dados
    entry_Nmero_de_livros_ECD.insert(0,"")
    entry_Ano_Nmero_de_livros_ECD.insert(0,"")
    entry_Nmero_de_livros_ECF.insert(0,"")
    entry_Ano_Nmero_de_livros_ECF.insert(0,"")
    
    ##Estaduais
    entry_Inscrio_estadual.delete(0, 'end')
    entry_Nmero_CSC.delete(0, 'end')
    entry_Site_caixa_postal.delete(0, 'end')

    entry_Estado_estaduais.set(Listadedados[3])
    #entry_UF.insert(0,Listadedados[25]) # Campo senha_ecac do banco de dados
    entry_Inscrio_estadual.insert(0,Listadedados[28]) # Campo inscricao_estadual do banco de dados
    entry_Credenciamento_NFE.set(Listadedados[29]) # Campo estado do banco de dados
    entry_Nmero_CSC.insert(0,Listadedados[30]) # Campo inscricao_estadual do banco de dados
    entry_Site_caixa_postal.insert(0,Listadedados[31]) # Campo credenciamento_nfe do banco de dados
    #entry_Livros_Fiscais_Entrada_Ano_Nmero.insert(0,Listadedados[30]) # Campo numero_csc do banco de dados
    #entry_Livros_Fiscais_Inventrio_Ano_Nmero.insert(0,Listadedados[31]) # Campo site_caixa_postal do banco de dados
    
    ## Municipais
    entry_Inscrio_municipal.delete(0, 'end')
    entry_Site.delete(0, 'end')
    entry_Login.delete(0, 'end')
    entry_Senha.delete(0, 'end')
    entry_Demais_senhas.delete(0, 'end')
    entry_Senha_Abertura_Processos.delete(0, 'end')
    entry_Observaes.delete(0, 'end')

    entry_Inscrio_municipal.insert(0,Listadedados[32]) # Campo inscricao_municipal do banco de dados
    entry_Site.insert(0,Listadedados[33]) # Campo site do banco de dados
    entry_Login.insert(0,Listadedados[34]) # Campo login do banco de dados
    entry_Senha.insert(0,Listadedados[35]) # Campo senha do banco de dados
    entry_Demais_senhas.insert(0,Listadedados[36]) # Campo alvara_funcionamento do banco de dados
    entry_Senha_Abertura_Processos.insert(0,Listadedados[37]) # Campo data_vencimento_alvara_funcionamento do banco de dados
    entry_Observaes.insert(0,Listadedados[38]) # Campo alvara_sanitario do banco de dados
    
    ## Societario
    entry_Data_vencimento_.delete(0, 'end')
    entry_ltima_alterao_contratual_.delete(0, 'end')
    entry_Nmero_alterao_contratual.delete(0, 'end')
    entry_Observaes_gerais_Societario.delete(0, 'end')

    entry_Alvara_de_funcionamento.set(Listadedados[39]) # Campo data_vencimento_alvara_sanitario do banco de dados
    entry_Data_vencimento_.insert(0,Listadedados[40]) # Campo licenca_ambiental do banco de dados
    entry_Alvara_sanitrio.set(Listadedados[41]) # Campo data_vencimento_licenca_ambiental do banco de dados
    entry_Licenca_ambiental.set(Listadedados[42]) # Campo bombeiros do banco de dados
    entry_Bombeiros.set(Listadedados[43]) # Campo data_vencimento_bombeiros do banco de dados
    entry_ltima_alterao_contratual_.insert(0,Listadedados[44]) # Campo ultima_alteracao_contratual do banco de dados
    entry_Nmero_alterao_contratual.insert(0,Listadedados[45]) # Campo numero_alteracao_contratual do banco de dados
    entry_Observaes_gerais_Societario.insert(0,Listadedados[46]) # Campo observacoes_gerais_societario do banco de dados
    
    ## Deparamento Pessoal 
    
    entry_Quantidade_de_funcionrios.delete(0, 'end')
    entry_Quantidade_de_scios.delete(0, 'end')
    entry_Esocial_usurio.delete(0, 'end')
    entry_Esocial_senha.delete(0, 'end')
    entry_Esocial_cdigo_de_acesso.delete(0, 'end')
    entry_FAP_usurio.delete(0, 'end')
    entry_FAP_senha.delete(0, 'end')
    entry_Empregador_WEB_usurio.delete(0, 'end')
    entry_Empregador_WEB_senha.delete(0, 'end')

    entry_Folha_de_pagto.set(Listadedados[47]) # Campo folha_pagto do banco de dados
    entry_Quantidade_de_funcionrios.insert(0,Listadedados[48]) # Campo quantidade_funcionarios do banco de dados
    entry_Prolabore.set(Listadedados[49]) # Campo prolabore do banco de dados
    entry_Quantidade_de_scios.insert(0,Listadedados[50]) # Campo quantidade_socios do banco de dados
    entry_Esocial_usurio.insert(0,Listadedados[51]) # Campo esocial_usuario do banco de dados
    entry_Esocial_senha.insert(0,Listadedados[52]) # Campo esocial_senha do banco de dados
    entry_Esocial_cdigo_de_acesso.insert(0,Listadedados[53]) # Campo esocial_codigo_acesso do banco de dados
    entry_FAP_usurio.insert(0,Listadedados[54]) # Campo fap_usuario do banco de dados
    entry_FAP_senha.insert(0,Listadedados[55]) # Campo fap_senha do banco de dados
    entry_Empregador_WEB_usurio.insert(0,Listadedados[56]) # Campo empregador_web_usuario do banco de dados
    entry_Empregador_WEB_senha.insert(0,Listadedados[57]) # Campo empregador_web_senha do banco de dados
    
    ## Sistema
    entry_Sistema.delete(0, 'end')
    entry_Site_Bpo.delete(0, 'end')
    entry_Usurio.delete(0, 'end')
    entry_Senha_simples.delete(0, 'end')
    entry_Banco_1.delete(0, 'end')
    entry_Banco_2.delete(0, 'end')
    entry_Tipo_de_BPO.delete(0, 'end')
    entry_Observaes_gerais_bpo.delete(0, 'end')

    entry_Sistema.insert(0,Listadedados[58]) # Campo sistema_bpo do banco de dados
    entry_Site_Bpo.insert(0,Listadedados[59]) # Campo site_bpo do banco de dados
    entry_Usurio.insert(0,Listadedados[60]) # Campo usuario_bpo do banco de dados
    entry_Senha_simples.insert(0,Listadedados[61]) # Campo senha_simples_bpo do banco de dados
    entry_Banco_1.insert(0,Listadedados[62]) # Campo banco1 do banco de dados
    entry_Banco_2.insert(0,Listadedados[63]) # Campo banco2 do banco de dados
    entry_Tipo_de_BPO.insert(0,Listadedados[64]) # Campo tipo_bpo do banco de dados
    entry_Observaes_gerais_bpo.insert(0,Listadedados[65])