import customtkinter as ctk
import tkinter as tk
from tkinter import *
import Modulos.Database.Clients as dbc
from ttkthemes import ThemedStyle
from tkinter import ttk 


def criarbotoes(Viewer,Caminho_Logo_Add,Caminho_Logo_Rem,DadosCliente):

    global NumeroID,Frame_dados_cliente_titulo,entry_Alvara_de_funcionamento,entry_Licenca_ambiental,entry_Data_vencimento_Ambiental,entry_Bombeiros,entry_Data_vencimento_Bombeiros,entry_Data_vencimento_Func,entry_Alvara_sanitrio,entry_Data_vencimento_Sanitario,entry_Nome_empresa,entry_CNPJ,entry_Estado,entry_Municpio,entry_Atividade,entry_Data_abertura_,entry_Ativo,entry_Link_WhatsApp,entry_Formas_de_tributao,entry_Anexo_simples_nacional,entry_Folha_de_pagamento,entry_Responsvel_contabil,entry_Responsvel_fiscal,entry_Responsvel_societrio,entry_Responsvel_DP,entry_Domiclio_eletrnico,entry_Email,entry_Nome_representante,entry_CPF_representante_legal,entry_Data_de_nascimento_,entry_Contabilidade_finalizada_,entry_Certificado_digital,entry_Senha_certificado,entry_Data_de_vencimento_,entry_Cdigo_e_cac,entry_Senha_EAC,entry_Cdigo_Simples,entry_Nmero_de_livros_ECD,entry_Ano_Nmero_de_livros_ECD,entry_Nmero_de_livros_ECF,entry_Ano_Nmero_de_livros_ECF,entry_Inscrio_estadual,entry_Credenciamento_NFE,entry_Nmero_CSC,entry_Site_caixa_postal,entry_Inscrio_municipal,entry_Site,entry_Login,entry_Senha,entry_Demais_senhas,entry_Senha_Abertura_Processos,entry_Observaes,entry_Alvara_de_funcionamento,entry_Alvara_sanitrio,entry_Licenca_ambiental,entry_Bombeiros,entry_ltima_alterao_contratual_,entry_Nmero_alterao_contratual,entry_Folha_de_pagto,entry_Quantidade_de_funcionrios,entry_Prolabore,entry_Quantidade_de_scios,entry_Esocial_usurio,entry_Esocial_senha,entry_Esocial_cdigo_de_acesso,entry_FAP_usurio,entry_FAP_senha,entry_Empregador_WEB_usurio,entry_Empregador_WEB_senha,entry_Sistema,entry_Site_Bpo,entry_Usurio,entry_Senha_simples,entry_Banco_1,entry_Banco_2,entry_Tipo_de_BPO,entry_Estado_estaduais,entry_Observaes_gerais_Societario,entry_Observaes_gerais_bpo,siglas_estados,not_or_yes,yes_or_not,formasdetributacao

    #Configurações de borda
    cor_de_borda = "gray50"
    largura_borda = 2
    Frame_dados_cliente_titulo=DadosCliente

#------------------------------cliente
    siglas_estados = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ]
    yes_or_not = [
        "SIM","NÃO"
    ]

    framecliente = ctk.CTkFrame(Viewer.tab("Cliente"), border_width=largura_borda, border_color=cor_de_borda)
    framecliente.grid(row=0, column=0, padx=10, pady=5, sticky="new")

    NumeroID = ctk.CTkLabel(framecliente, text="ID")
    NumeroID.grid(row=0, column=1,columnspan=1, padx=10, pady=10, sticky="w")

    label_Nome_empresa = ctk.CTkLabel(framecliente, text="Nome empresa")
    entry_Nome_empresa = ctk.CTkEntry(framecliente,width=600)

    label_Nome_empresa.grid(row=0, column=0,columnspan=1, padx=10, pady=10, sticky="w")
    entry_Nome_empresa.grid(row=1, column=0,columnspan=3, padx=10, pady=15, sticky="new")

    
    label_CNPJ = ctk.CTkLabel(framecliente, text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(framecliente)

    label_CNPJ.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    entry_CNPJ.grid(row=1, column=3, padx=10, pady=15, sticky="new")


    label_Estado = ctk.CTkLabel(framecliente, text="Estado")
    entry_Estado = ctk.CTkComboBox(framecliente,values= siglas_estados)

    label_Estado.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    entry_Estado.grid(row=3, column=1, padx=10, pady=15, sticky="new")
    #entry_Estado.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="new")

    label_Municpio = ctk.CTkLabel(framecliente, text="Município")
    entry_Municpio = ctk.CTkEntry(framecliente)

    label_Municpio.grid(row=2, column=2, padx=10, pady=1, sticky="w")
    entry_Municpio.grid(row=3, column=2, padx=10, pady=15, sticky="new")


    label_Atividade = ctk.CTkLabel(framecliente, text="Atividade")
    entry_Atividade = ctk.CTkEntry(framecliente)

    label_Atividade.grid(row=2, column=0, padx=10, pady=1, sticky="w")
    entry_Atividade.grid(row=3, column=0, padx=10, pady=15, sticky="new")


    label_Data_abertura_ = ctk.CTkLabel(framecliente, text="Data abertura")
    entry_Data_abertura_ = ctk.CTkEntry(framecliente)

    label_Data_abertura_.grid(row=2, column=3, padx=10, pady=1, sticky="w")
    entry_Data_abertura_.grid(row=3, column=3, padx=10, pady=15, sticky="new")


    label_Ativo = ctk.CTkLabel(framecliente, text="Ativo")
    entry_Ativo = ctk.CTkComboBox(framecliente,values=yes_or_not)
    
    label_Ativo.grid(row=4, column=3, padx=10, pady=1, sticky="w")
    entry_Ativo.grid(row=5, column=3, padx=10, pady=15, sticky="new")


    label_Link_WhatsApp = ctk.CTkLabel(framecliente, text="Link WhatsApp")
    entry_Link_WhatsApp = ctk.CTkEntry(framecliente)

    label_Link_WhatsApp.grid(row=4, column=0,columnspan=3, padx=10, pady=1, sticky="w")
    entry_Link_WhatsApp.grid(row=5, column=0,columnspan=3, padx=10, pady=15, sticky="new")

#------------------------------Gerais
    
    formasdetributacao = [
        "SIMPLES NACIONAL","MEI","PRESUMIDO","LUCRO REAL","IMUNE/ISENTA"
    ]

    scrollframegerais = ctk.CTkScrollableFrame(Viewer.tab("Gerais"), border_width=largura_borda, border_color=cor_de_borda,width=780, height=450)
    scrollframegerais.grid(row=0, column=0, padx=1, pady=1, sticky="new")
    
    frameGerais = ctk.CTkFrame(scrollframegerais)
    frameGerais.grid(row=0, column=0, padx=10, pady=5, sticky="new")

    label_Formas_de_tributao = ctk.CTkLabel(frameGerais, text="Formas de tributação")
    entry_Formas_de_tributao = ctk.CTkComboBox(frameGerais, width=150,values=formasdetributacao)

    label_Formas_de_tributao.grid(row=0, column=0, padx=10, pady=3, sticky="w")
    entry_Formas_de_tributao.grid(row=0, column=1, padx=10, pady=3, sticky="new")


    label_Anexo_simples_nacional = ctk.CTkLabel(frameGerais, text="Anexo simples nacional")
    entry_Anexo_simples_nacional = ctk.CTkEntry(frameGerais, width=150)

    label_Anexo_simples_nacional.grid(row=1, column=0, padx=10, pady=3, sticky="w")
    entry_Anexo_simples_nacional.grid(row=1, column=1, padx=10, pady=3, sticky="new")
    

    not_or_yes = [
       "NÃO", "SIM"
    ]
    label_Folha_de_pagamento = ctk.CTkLabel(frameGerais, text="Folha de pagamento")
    entry_Folha_de_pagamento = ctk.CTkComboBox(frameGerais, width=150,values=not_or_yes)

    label_Folha_de_pagamento.grid(row=2, column=0, padx=10, pady=3, sticky="w")
    entry_Folha_de_pagamento.grid(row=2, column=1, padx=10, pady=3, sticky="new")


    label_Responsvel_contabil = ctk.CTkLabel(frameGerais, text="Responsável contabil")
    entry_Responsvel_contabil = ctk.CTkEntry(frameGerais, width=150)

    label_Responsvel_contabil.grid(row=3, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_contabil.grid(row=3, column=1, padx=10, pady=3, sticky="new")


    label_Responsvel_fiscal = ctk.CTkLabel(frameGerais, text="Responsável fiscal")
    entry_Responsvel_fiscal = ctk.CTkEntry(frameGerais, width=150)

    label_Responsvel_fiscal.grid(row=4, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_fiscal.grid(row=4, column=1, padx=10, pady=3, sticky="new")


    label_Responsvel_societrio = ctk.CTkLabel(frameGerais, text="Responsável societário")
    entry_Responsvel_societrio = ctk.CTkEntry(frameGerais, width=150)

    label_Responsvel_societrio.grid(row=5, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_societrio.grid(row=5, column=1, padx=10, pady=3, sticky="new")


    label_Responsvel_DP = ctk.CTkLabel(frameGerais, text="Responsável DP")
    entry_Responsvel_DP = ctk.CTkEntry(frameGerais, width=150)

    label_Responsvel_DP.grid(row=6, column=0, padx=10, pady=3, sticky="w")
    entry_Responsvel_DP.grid(row=6, column=1, padx=10, pady=3, sticky="new")

    

    label_Domiclio_eletrnico = ctk.CTkLabel(frameGerais, text="Domicílio eletrônico")
    entry_Domiclio_eletrnico = ctk.CTkComboBox(frameGerais, width=150,values=not_or_yes)

    label_Domiclio_eletrnico.grid(row=6, column=2, padx=10, pady=3, sticky="w")
    entry_Domiclio_eletrnico.grid(row=6, column=3, padx=10, pady=3, sticky="new")


    label_Email = ctk.CTkLabel(frameGerais, text="Email")
    entry_Email = ctk.CTkEntry(frameGerais, width=240)

    label_Email.grid(row=8, column=0, padx=10, pady=3, sticky="w")
    entry_Email.grid(row=8, column=1,columnspan=2, padx=10, pady=3, sticky="new")


    label_Nome_representante = ctk.CTkLabel(frameGerais, text="Nome representante")
    entry_Nome_representante = ctk.CTkEntry(frameGerais, width=240)

    label_Nome_representante.grid(row=9, column=0, padx=10, pady=3, sticky="w")
    entry_Nome_representante.grid(row=9, column=1,columnspan=2, padx=10, pady=3, sticky="new")


    label_CPF_representante_legal = ctk.CTkLabel(frameGerais, text="CPF representante legal")
    entry_CPF_representante_legal = ctk.CTkEntry(frameGerais, width=150)

    label_CPF_representante_legal.grid(row=0, column=2, padx=10, pady=3, sticky="w")
    entry_CPF_representante_legal.grid(row=0, column=3, padx=10, pady=3, sticky="new")


    label_Data_de_nascimento_ = ctk.CTkLabel(frameGerais, text="Data de nascimento (dd/mm/aaaa)")
    entry_Data_de_nascimento_ = ctk.CTkEntry(frameGerais, width=150)

    label_Data_de_nascimento_.grid(row=1, column=2, padx=10, pady=3, sticky="w")
    entry_Data_de_nascimento_.grid(row=1, column=3, padx=10, pady=3, sticky="new")


    label_Contabilidade_finalizada_ = ctk.CTkLabel(frameGerais, text="Contabilidade finalizada (dd/mm/aaaa)")
    entry_Contabilidade_finalizada_ = ctk.CTkEntry(frameGerais, width=150)

    label_Contabilidade_finalizada_.grid(row=2, column=2, padx=10, pady=3, sticky="w")
    entry_Contabilidade_finalizada_.grid(row=2, column=3, padx=10, pady=3, sticky="new")


    label_Certificado_digital = ctk.CTkLabel(frameGerais, text="Certificado digital")
    entry_Certificado_digital = ctk.CTkComboBox(frameGerais, width=150,values=not_or_yes)

    label_Certificado_digital.grid(row=3, column=2, padx=10, pady=3, sticky="w")
    entry_Certificado_digital.grid(row=3, column=3, padx=10, pady=3, sticky="new")


    label_Senha_certificado = ctk.CTkLabel(frameGerais, text="Senha certificado")
    entry_Senha_certificado = ctk.CTkEntry(frameGerais, width=150)

    label_Senha_certificado.grid(row=4, column=2, padx=10, pady=3, sticky="w")
    entry_Senha_certificado.grid(row=4, column=3, padx=10, pady=3, sticky="new")


    label_Data_de_vencimento_ = ctk.CTkLabel(frameGerais, text="Data de vencimento (dd/mm/aaaa)")
    entry_Data_de_vencimento_ = ctk.CTkEntry(frameGerais, width=150)

    label_Data_de_vencimento_.grid(row=5, column=2, padx=10, pady=3, sticky="w")
    entry_Data_de_vencimento_.grid(row=5, column=3, padx=10, pady=3, sticky="new")

    label_socios = ctk.CTkLabel(frameGerais, text="Socios")
    label_socios.grid(row=11, column=0,columnspan=4, padx=10, pady=3, sticky="w")

    entry_Cad_NomeSocio = ctk.CTkEntry(frameGerais)
    entry_Cad_NomeSocio.grid(row=5, column=3, padx=10, pady=3, sticky="new")

    #logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    #bt_add = ctk.CTkButton(master=frameECD,image=logo_add, text="Adicionar",command="")
    #bt_add.grid(row=0, column=3, padx=5, pady=5, sticky="new")

    #logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    #bt_Excluir = ctk.CTkButton(master=frameECD,image=logo_excluir, text="Excluir",command=lambda: "")
    #bt_Excluir.grid(row=1, column=3, padx=5, pady=5, sticky="new")

    TreeviewSocios = ttk.Treeview(frameGerais, columns=("Nome","CPF","Porcentagem"), show='headings')
    TreeviewSocios.grid(row=15, column=0,columnspan=4, sticky="nsew", padx=(1,0), pady=(5,10))
    TreeviewSocios.bind('<<TreeviewSelect>>')
    
    EstilodeTela = ThemedStyle(TreeviewSocios)
    EstilodeTela.set_theme("scidsand")

    # Define o as colunas
    TreeviewSocios.heading("Nome", text="Nome")
    TreeviewSocios.heading("CPF", text="CPF")
    TreeviewSocios.heading("Porcentagem", text="Porcentagem")
    
    
    # Define o tamanho das colunas em pixels
    TreeviewSocios.column("Nome", width=200)  # 
    TreeviewSocios.column("CPF", width=200)  # 
    TreeviewSocios.column("Porcentagem", width=200)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(frameGerais, command=TreeviewSocios.yview,height=100)
    scrollbar.grid(row=15, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeviewSocios.configure(yscrollcommand=scrollbar.set)

#------------------------------Federais
    frame_federais = ctk.CTkFrame(Viewer.tab("Federais"), border_width=largura_borda, border_color=cor_de_borda)
    frame_federais.grid(row=0, column=0, padx=10, pady=5, sticky="new")

    label_Cdigo_e_cac = ctk.CTkLabel(frame_federais, text="Código e-cac")
    entry_Cdigo_e_cac = ctk.CTkEntry(frame_federais, width=230)

    label_Cdigo_e_cac.grid(row=0, column=0, padx=5, pady=5, sticky="new")
    entry_Cdigo_e_cac.grid(row=1, column=0, padx=5, pady=5, sticky="new")


    label_Senha_EAC = ctk.CTkLabel(frame_federais, text="Senha EAC")
    entry_Senha_EAC = ctk.CTkEntry(frame_federais, width=230)

    label_Senha_EAC.grid(row=0, column=1, padx=5, pady=5, sticky="new")
    entry_Senha_EAC.grid(row=1, column=1, padx=5, pady=5, sticky="new")


    label_Cdigo_Simples = ctk.CTkLabel(frame_federais, text="Código Simples")
    entry_Cdigo_Simples = ctk.CTkEntry(frame_federais, width=230)

    label_Cdigo_Simples.grid(row=0, column=2, padx=5, pady=5, sticky="new")
    entry_Cdigo_Simples.grid(row=1, column=2, padx=5, pady=5, sticky="new")

    tab_livros=ctk.CTkTabview(frame_federais, width=750)
    tab_livros.grid(row=3, column=0,columnspan=3, padx=5, pady=5, sticky="nsew")
    tab_livros.add("livros ECD")
    tab_livros.add("livros ECF")

    ### ECD 
    frameECD = ctk.CTkFrame(tab_livros.tab("livros ECD"), border_width=largura_borda, border_color=cor_de_borda)
    frameECD.grid(row=0, column=0, padx=(10,0), pady=5, sticky="n")

    label_Nmero_de_livros_ECD = ctk.CTkLabel(frameECD, text="Numero")
    entry_Nmero_de_livros_ECD = ctk.CTkEntry(frameECD, width=200)

    label_Nmero_de_livros_ECD.grid(row=0, column=0, padx=5, pady=5, sticky="new")
    entry_Nmero_de_livros_ECD.grid(row=1, column=0, padx=(10,5), pady=5, sticky="new")


    label_Ano_Nmero_de_livros_ECD = ctk.CTkLabel(frameECD, text="Ano")
    entry_Ano_Nmero_de_livros_ECD = ctk.CTkEntry(frameECD, width=200)
    
    label_Ano_Nmero_de_livros_ECD.grid(row=0, column=1, padx=5, pady=5, sticky="new")
    entry_Ano_Nmero_de_livros_ECD.grid(row=1, column=1, padx=5, pady=5, sticky="new")
    
    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add = ctk.CTkButton(master=frameECD,image=logo_add, text="Adicionar",command="")
    bt_add.grid(row=0, column=2, padx=5, pady=5, sticky="new")

    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir = ctk.CTkButton(master=frameECD,image=logo_excluir, text="Excluir",command=lambda: "")
    bt_Excluir.grid(row=1, column=2, padx=5, pady=5, sticky="new")

        
    
    
    TreeviewECD = ttk.Treeview(frameECD, columns=("Numero","Ano"), show='headings')
    TreeviewECD.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(10,0), pady=(5,10))
    TreeviewECD.bind('<<TreeviewSelect>>')
    
    EstilodeTela = ThemedStyle(TreeviewECD)
    EstilodeTela.set_theme("scidsand")

    # Define o as colunas
    TreeviewECD.heading("Numero", text="Numero")
    TreeviewECD.heading("Ano", text="Ano")
    
    # Define o tamanho das colunas em pixels
    TreeviewECD.column("Numero", width=350)  # 
    TreeviewECD.column("Ano", width=350)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(frameECD, command=TreeviewECD.yview,height=200)
    scrollbar.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeviewECD.configure(yscrollcommand=scrollbar.set)


    ###ECF
    frameECF = ctk.CTkFrame(tab_livros.tab("livros ECF"), border_width=largura_borda, border_color=cor_de_borda)
    frameECF.grid(row=0, column=0, padx=(10,0), pady=5, sticky="n")

    label_Nmero_de_livros_ECF = ctk.CTkLabel(frameECF, text="Numero")
    entry_Nmero_de_livros_ECF = ctk.CTkEntry(frameECF, width=200)

    label_Nmero_de_livros_ECF.grid(row=0, column=0, padx=5, pady=5, sticky="new")
    entry_Nmero_de_livros_ECF.grid(row=1, column=0, padx=(10,5), pady=5, sticky="new")


    label_Ano_Nmero_de_livros_ECF = ctk.CTkLabel(frameECF, text="Ano")
    entry_Ano_Nmero_de_livros_ECF = ctk.CTkEntry(frameECF, width=200)

    label_Ano_Nmero_de_livros_ECF.grid(row=0, column=1, padx=5, pady=5, sticky="new")
    entry_Ano_Nmero_de_livros_ECF.grid(row=1, column=1, padx=5, pady=5, sticky="new")

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add = ctk.CTkButton(master=frameECF,image=logo_add, text="Adicionar",command="")
    bt_add.grid(row=0, column=2, padx=5, pady=5, sticky="new")

    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir = ctk.CTkButton(master=frameECF,image=logo_excluir, text="Excluir",command=lambda: "")
    bt_Excluir.grid(row=1, column=2, padx=5, pady=5, sticky="new")

   
    
    TreeviewECF= ttk.Treeview(frameECF, columns=("Numero","Ano"), show='headings')
    TreeviewECF.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(10,0), pady=(5,10))
    TreeviewECF.bind('<<TreeviewSelect>>')
    
    EstilodeTela = ThemedStyle(TreeviewECF)
    EstilodeTela.set_theme("scidsand")

    # Define o as colunas
    TreeviewECF.heading("Numero", text="Numero")
    TreeviewECF.heading("Ano", text="Ano")
    
    # Define o tamanho das colunas em pixels
    TreeviewECF.column("Numero", width=350)  # 
    TreeviewECF.column("Ano", width=350)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(frameECF, command=TreeviewECF.yview,height=200)
    scrollbar.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeviewECF.configure(yscrollcommand=scrollbar.set)


#------------------------------Estaduais
    frameestaduais = ctk.CTkFrame(Viewer.tab("Estaduais"), border_width=largura_borda, border_color=cor_de_borda)
    frameestaduais.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    label_Estado_estaduais = ctk.CTkLabel(frameestaduais, text="Estado")
    entry_Estado_estaduais = ctk.CTkComboBox(frameestaduais,values=siglas_estados)

    label_Estado_estaduais.grid(row=0, column=0, padx=10, pady=3, sticky="new")
    entry_Estado_estaduais.grid(row=1, column=0, padx=10, pady=0, sticky="new")

    label_Inscrio_estadual = ctk.CTkLabel(frameestaduais, text="Inscrição estadual")
    entry_Inscrio_estadual = ctk.CTkEntry(frameestaduais)

    label_Inscrio_estadual.grid(row=0, column=1, padx=10, pady=3, sticky="new")
    entry_Inscrio_estadual.grid(row=1, column=1, padx=10, pady=0, sticky="new")


    label_Credenciamento_NFE = ctk.CTkLabel(frameestaduais, text="Credenciamento NFE")
    entry_Credenciamento_NFE = ctk.CTkComboBox(frameestaduais,values=not_or_yes)

    label_Credenciamento_NFE.grid(row=0, column=2, padx=10, pady=3, sticky="new")
    entry_Credenciamento_NFE.grid(row=1, column=2, padx=10, pady=0, sticky="new")


    label_Nmero_CSC = ctk.CTkLabel(frameestaduais, text="Número CSC")
    entry_Nmero_CSC = ctk.CTkEntry(frameestaduais)

    label_Nmero_CSC.grid(row=0, column=3, padx=10, pady=3, sticky="new")
    entry_Nmero_CSC.grid(row=1, column=3, padx=10, pady=0, sticky="new")

    framecxpostal = ctk.CTkFrame(frameestaduais)
    framecxpostal.grid(row=3, column=0,columnspan=4, padx=(10,10), pady=5, sticky="new")

    label_Site_caixa_postal = ctk.CTkLabel(framecxpostal, text="Site caixa postal")
    entry_Site_caixa_postal = ctk.CTkEntry(framecxpostal, width=600)

    label_Site_caixa_postal.grid(row=2, column=0, padx=10, pady=5, sticky="new")
    entry_Site_caixa_postal.grid(row=2, column=1,columnspan=3, padx=10, pady=1, sticky="nsew")



    tab_livros_estaduais=ctk.CTkTabview(frameestaduais, width=750)
    tab_livros_estaduais.grid(row=4, column=0,columnspan=4, padx=5, pady=0, sticky="nsew")
    tab_livros_estaduais.add("Livros Fiscais Entrada")
    tab_livros_estaduais.add("Livros Fiscais Inventário")

#### Livros Fiscais Entrada ### Livros Fiscais Entrada ###
    frameLivrosEntrada = ctk.CTkFrame(tab_livros_estaduais.tab("Livros Fiscais Entrada"), border_width=largura_borda, border_color=cor_de_borda)
    frameLivrosEntrada.grid(row=0, column=0, padx=(10,0), pady=0, sticky="n")

    label_Livros_Fiscais_Entrada_Numero = ctk.CTkLabel(frameLivrosEntrada, text="Numero")
    entry_Livros_Fiscais_Entrada_Numero = ctk.CTkEntry(frameLivrosEntrada, width=50)

    label_Livros_Fiscais_Entrada_Numero.grid(row=0, column=0, padx=10, pady=2, sticky="new")
    entry_Livros_Fiscais_Entrada_Numero.grid(row=1, column=0, padx=10, pady=2, sticky="new")

    label_Livros_Fiscais_Entrada_Ano = ctk.CTkLabel(frameLivrosEntrada, text="Ano")
    entry_Livros_Fiscais_Entrada_Ano = ctk.CTkEntry(frameLivrosEntrada, width=50)

    label_Livros_Fiscais_Entrada_Ano.grid(row=0, column=1, padx=10, pady=2, sticky="new")
    entry_Livros_Fiscais_Entrada_Ano.grid(row=1, column=1, padx=10, pady=2, sticky="new")

    
    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add = ctk.CTkButton(master=frameLivrosEntrada,image=logo_add, text="Adicionar",command="")
    bt_add.grid(row=0, column=2, padx=5, pady=5, sticky="new")

    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir = ctk.CTkButton(master=frameLivrosEntrada,image=logo_excluir, text="Excluir",command=lambda: "")
    bt_Excluir.grid(row=1, column=2, padx=5, pady=2, sticky="new")

   
    
    TreeviewEntrada= ttk.Treeview(frameLivrosEntrada, columns=("Numero","Ano"), show='headings')
    TreeviewEntrada.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(10,0), pady=(5,2))
    TreeviewEntrada.bind('<<TreeviewSelect>>')
    
    EstilodeTela = ThemedStyle(TreeviewEntrada)
    EstilodeTela.set_theme("scidsand")

    # Define o as colunas
    TreeviewEntrada.heading("Numero", text="Numero")
    TreeviewEntrada.heading("Ano", text="Ano")
    
    # Define o tamanho das colunas em pixels
    TreeviewEntrada.column("Numero", width=350)  # 
    TreeviewEntrada.column("Ano", width=350)  # 

    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(frameLivrosEntrada, command=TreeviewEntrada.yview,height=150)
    scrollbar.grid(row=2, column=4, padx=(0,10), pady=(5,2), sticky="nsew")
    TreeviewEntrada.configure(yscrollcommand=scrollbar.set)





### Livros Fiscais Inventário ### Livros Fiscais Inventário ###

    frameLivrosInventario = ctk.CTkFrame(tab_livros_estaduais.tab("Livros Fiscais Inventário"), border_width=largura_borda, border_color=cor_de_borda)
    frameLivrosInventario.grid(row=0, column=0, padx=(10,0), pady=0, sticky="n")

    label_Livros_Fiscais_Inventario_Numero = ctk.CTkLabel(frameLivrosInventario, text="Numero")
    entry_Livros_Fiscais_Inventario_Numero = ctk.CTkEntry(frameLivrosInventario, width=50)

    label_Livros_Fiscais_Inventario_Numero.grid(row=0, column=0, padx=10, pady=2, sticky="new")
    entry_Livros_Fiscais_Inventario_Numero.grid(row=1, column=0, padx=10, pady=2, sticky="new")

    label_Livros_Fiscais_Inventario_Ano = ctk.CTkLabel(frameLivrosInventario, text="Ano")
    entry_Livros_Fiscais_Inventario_Ano = ctk.CTkEntry(frameLivrosInventario, width=50)

    label_Livros_Fiscais_Inventario_Ano.grid(row=0, column=1, padx=10, pady=2, sticky="new")
    entry_Livros_Fiscais_Inventario_Ano.grid(row=1, column=1, padx=10, pady=2, sticky="new")

    
    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add = ctk.CTkButton(master=frameLivrosInventario,image=logo_add, text="Adicionar",command="")
    bt_add.grid(row=0, column=2, padx=5, pady=5, sticky="new")

    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir = ctk.CTkButton(master=frameLivrosInventario,image=logo_excluir, text="Excluir",command=lambda: "")
    bt_Excluir.grid(row=1, column=2, padx=5, pady=2, sticky="new")

   
    
    TreeviewInventario= ttk.Treeview(frameLivrosInventario, columns=("Numero","Ano"), show='headings')
    TreeviewInventario.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(10,0), pady=(5,2))
    TreeviewInventario.bind('<<TreeviewSelect>>')
    
    EstilodeTela = ThemedStyle(TreeviewInventario)
    EstilodeTela.set_theme("scidsand")

    # Define o as colunas
    TreeviewInventario.heading("Numero", text="Numero")
    TreeviewInventario.heading("Ano", text="Ano")
    
    # Define o tamanho das colunas em pixels
    TreeviewInventario.column("Numero", width=350)  # 
    TreeviewInventario.column("Ano", width=350)  # 

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(frameLivrosInventario, command=TreeviewInventario.yview,height=150)
    scrollbar.grid(row=2, column=4, padx=(0,10), pady=(5,2), sticky="nsew")
    TreeviewInventario.configure(yscrollcommand=scrollbar.set)



#------------------------------Municipais
    frameMunicipais = ctk.CTkFrame(Viewer.tab("Municipais"), border_width=largura_borda, border_color=cor_de_borda)
    frameMunicipais.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    label_Inscrio_municipal = ctk.CTkLabel(frameMunicipais, text="Inscrição municipal")
    entry_Inscrio_municipal = ctk.CTkEntry(frameMunicipais, width=100)

    label_Inscrio_municipal.grid(row=0, column=0, padx=10, pady=3, sticky="w")
    entry_Inscrio_municipal.grid(row=1, column=0, padx=10, pady=3, sticky="new")


    label_Site = ctk.CTkLabel(frameMunicipais, text="Site")
    entry_Site = ctk.CTkEntry(frameMunicipais, width=50)

    label_Site.grid(row=0, column=1, columnspan=2, padx=10, pady=1, sticky="w")
    entry_Site.grid(row=1, column=1, columnspan=2, padx=10, pady=3, sticky="new")


    label_Login = ctk.CTkLabel(frameMunicipais, text="Login")
    entry_Login = ctk.CTkEntry(frameMunicipais, width=50)

    label_Login.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    entry_Login.grid(row=3, column=1, padx=10, pady=3, sticky="new")


    label_Senha = ctk.CTkLabel(frameMunicipais, text="Senha")
    entry_Senha = ctk.CTkEntry(frameMunicipais, width=50)

    label_Senha.grid(row=2, column=2, padx=10, pady=1, sticky="w")
    entry_Senha.grid(row=3, column=2, padx=10, pady=3, sticky="new")


    label_Demais_senhas = ctk.CTkLabel(frameMunicipais, text="Demais senhas")
    entry_Demais_senhas = ctk.CTkEntry(frameMunicipais, width=750)

    label_Demais_senhas.grid(row=4, column=0, padx=10, pady=1, sticky="w")
    entry_Demais_senhas.grid(row=5, column=0, columnspan=3, padx=10, pady=3, sticky="new")


    label_Senha_Abertura_Processos = ctk.CTkLabel(frameMunicipais, text="Senha Abertura Processos")
    entry_Senha_Abertura_Processos = ctk.CTkEntry(frameMunicipais)

    label_Senha_Abertura_Processos.grid(row=2, column=0, padx=10, pady=1, sticky="w")
    entry_Senha_Abertura_Processos.grid(row=3, column=0, padx=10, pady=3, sticky="new")


    label_Observaes = ctk.CTkLabel(frameMunicipais, text="Observações")
    entry_Observaes = ctk.CTkTextbox(frameMunicipais, height=200, width=750)
    

    label_Observaes.grid(row=6, column=0, columnspan=3, padx=10, pady=1, sticky="w")
    entry_Observaes.grid(row=7, column=0, columnspan=3, padx=10, pady=3, sticky="new")

#------------------------------Societario
  
    frameSocietario = ctk.CTkFrame(Viewer.tab("Societário"), border_width=largura_borda, border_color=cor_de_borda)
    frameSocietario.grid(row=0, column=0, padx=10, pady=5, sticky="new")

    #Funcionamento
    Framealvara_func = ctk.CTkFrame(frameSocietario, border_width=largura_borda, border_color=cor_de_borda)
    Framealvara_func.grid(row=0, column=0, padx=10, pady=5, sticky="new")
    
    label_Alvara_de_funcionamento = ctk.CTkLabel(Framealvara_func, text="Alvara de funcionamento")
    entry_Alvara_de_funcionamento = ctk.CTkComboBox(Framealvara_func,values=not_or_yes, width=121)

    label_Alvara_de_funcionamento.grid(row=0, column=0, padx=10, pady=5, sticky="new")
    entry_Alvara_de_funcionamento.grid(row=0, column=1, padx=10, pady=5, sticky="new")


    label_Data_vencimento_Func = ctk.CTkLabel(Framealvara_func, text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_Func = ctk.CTkEntry(Framealvara_func, width=121)

    label_Data_vencimento_Func.grid(row=1, column=0, padx=10, pady=5, sticky="new")
    entry_Data_vencimento_Func.grid(row=1, column=1, padx=10, pady=5, sticky="new")


    #Sanitario
    Framealvara_sani = ctk.CTkFrame(frameSocietario, border_width=largura_borda, border_color=cor_de_borda)
    Framealvara_sani.grid(row=1, column=0, padx=10, pady=5, sticky="new")

    label_Alvara_sanitrio = ctk.CTkLabel(Framealvara_sani, text="Alvara sanitário")
    entry_Alvara_sanitrio = ctk.CTkComboBox(Framealvara_sani, width=121,values=not_or_yes)

    label_Alvara_sanitrio.grid(row=2, column=0, padx=10, pady=5, sticky="new")
    entry_Alvara_sanitrio.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_Sanitario = ctk.CTkLabel(Framealvara_sani, text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_Sanitario = ctk.CTkEntry(Framealvara_sani, width=121)

    label_Data_vencimento_Sanitario.grid(row=3, column=0, padx=10, pady=5, sticky="new")
    entry_Data_vencimento_Sanitario.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

   
    #ambiental
    Framealvara_ambiental = ctk.CTkFrame(frameSocietario, border_width=largura_borda, border_color=cor_de_borda)
    Framealvara_ambiental.grid(row=0, column=1, padx=10, pady=5, sticky="new")
   
    label_Licenca_ambiental = ctk.CTkLabel(Framealvara_ambiental, text="Licença ambiental")
    entry_Licenca_ambiental = ctk.CTkComboBox(Framealvara_ambiental, width=121,values=not_or_yes)

    label_Licenca_ambiental.grid(row=4, column=0, padx=10, pady=5, sticky="new")
    entry_Licenca_ambiental.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_Ambiental = ctk.CTkLabel(Framealvara_ambiental, text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_Ambiental = ctk.CTkEntry(Framealvara_ambiental, width=121)

    label_Data_vencimento_Ambiental.grid(row=5, column=0, padx=10, pady=5, sticky="new")
    entry_Data_vencimento_Ambiental.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")

    #Bombeiros
    Framealvara_Bombeiro = ctk.CTkFrame(frameSocietario, border_width=largura_borda, border_color=cor_de_borda)
    Framealvara_Bombeiro.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    label_Bombeiros = ctk.CTkLabel(Framealvara_Bombeiro, text="Bombeiros")
    entry_Bombeiros = ctk.CTkComboBox(Framealvara_Bombeiro, width=121,values=not_or_yes)

    label_Bombeiros.grid(row=6, column=0, padx=10, pady=5, sticky="new")
    entry_Bombeiros.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_Bombeiros = ctk.CTkLabel(Framealvara_Bombeiro, text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_Bombeiros = ctk.CTkEntry(Framealvara_Bombeiro, width=121)

    label_Data_vencimento_Bombeiros.grid(row=7, column=0, padx=10, pady=5, sticky="new")
    entry_Data_vencimento_Bombeiros.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")

    # alteração 
    Framealterações = ctk.CTkFrame(frameSocietario, border_width=largura_borda, border_color=cor_de_borda)
    Framealterações.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    label_ltima_alterao_contratual_ = ctk.CTkLabel(Framealterações, text="Última alteração contratual (dd/mm/aaaa)")
    entry_ltima_alterao_contratual_ = ctk.CTkEntry(Framealterações, width=350)

    label_ltima_alterao_contratual_.grid(row=0, column=0, padx=10, pady=5, sticky="new")
    entry_ltima_alterao_contratual_.grid(row=1, column=0, padx=10, pady=5, sticky="new")


    label_Nmero_alterao_contratual = ctk.CTkLabel(Framealterações, text="Número alteração contratual")
    entry_Nmero_alterao_contratual = ctk.CTkEntry(Framealterações, width=350)

    label_Nmero_alterao_contratual.grid(row=0, column=1, padx=10, pady=5, sticky="new")
    entry_Nmero_alterao_contratual.grid(row=1,column=1, padx=10, pady=5, sticky="new")


    label_Observaes_gerais_Societario = ctk.CTkLabel(frameSocietario, text="Observações gerais")
    entry_Observaes_gerais_Societario = ctk.CTkTextbox(frameSocietario, width=750, height=150)

    label_Observaes_gerais_Societario.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_Observaes_gerais_Societario.grid(row=4, column=0,columnspan=2, padx=10, pady=5, sticky="new")

#------------------------------DP Pessoal
    framedpMaster = ctk.CTkFrame(Viewer.tab("Departamento pessoal"), border_width=largura_borda, border_color=cor_de_borda)
    framedpMaster.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    framedp = ctk.CTkFrame(framedpMaster, border_width=largura_borda, border_color=cor_de_borda)
    framedp.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    label_Folha_de_pagto = ctk.CTkLabel(framedp, text="Folha de pagto", width=20)
    entry_Folha_de_pagto = ctk.CTkComboBox(framedp,values=not_or_yes, width=80)

    label_Folha_de_pagto.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Folha_de_pagto.grid(row=0, column=1, padx=10, pady=5, sticky="new")


    label_Quantidade_de_funcionrios = ctk.CTkLabel(framedp, text="Quantidade de funcionários", width=20)
    entry_Quantidade_de_funcionrios = ctk.CTkEntry(framedp, width=20)

    label_Quantidade_de_funcionrios.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Quantidade_de_funcionrios.grid(row=0, column=3, padx=10, pady=5, sticky="new")


    label_Prolabore = ctk.CTkLabel(framedp, text="Pro labore", width=20)
    entry_Prolabore = ctk.CTkComboBox(framedp,values=not_or_yes, width=20)

    label_Prolabore.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_Prolabore.grid(row=1, column=1, padx=10, pady=5, sticky="new")


    label_Quantidade_de_scios = ctk.CTkLabel(framedp, text="Quantidade de sócios", width=20)
    entry_Quantidade_de_scios = ctk.CTkEntry(framedp, width=40)

    label_Quantidade_de_scios.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Quantidade_de_scios.grid(row=1, column=3, padx=10, pady=5, sticky="new")

    ##Dados esocial
    framedp_esocial = ctk.CTkFrame(framedpMaster, border_width=largura_borda, border_color=cor_de_borda)
    framedp_esocial.grid(row=2, column=0, padx=10, pady=5, sticky="new")

    label_Esocial_usurio = ctk.CTkLabel(framedp_esocial, text="Esocial usuário", width=100)
    entry_Esocial_usurio = ctk.CTkEntry(framedp_esocial, width=115)

    label_Esocial_usurio.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
    entry_Esocial_usurio.grid(row=1, column=0, padx=10, pady=5, sticky="new")


    label_Esocial_senha = ctk.CTkLabel(framedp_esocial, text="Esocial senha", width=100)
    entry_Esocial_senha = ctk.CTkEntry(framedp_esocial, width=115)

    label_Esocial_senha.grid(row=0, column=1, padx=10, pady=5, sticky="nw")
    entry_Esocial_senha.grid(row=1, column=1, padx=10, pady=5, sticky="new")


    label_Esocial_cdigo_de_acesso = ctk.CTkLabel(framedp_esocial, text="Esocial código de acesso", width=100)
    entry_Esocial_cdigo_de_acesso = ctk.CTkEntry(framedp_esocial, width=115)

    label_Esocial_cdigo_de_acesso.grid(row=0, column=2, padx=10, pady=5, sticky="nw")
    entry_Esocial_cdigo_de_acesso.grid(row=1, column=2, padx=10, pady=5, sticky="new")

    
    ##Demais logins
    framedp_acessos = ctk.CTkFrame(framedpMaster, border_width=largura_borda, border_color=cor_de_borda)
    framedp_acessos.grid(row=0, column=4,rowspan=3, padx=1, pady=5, sticky="nsew")

    label_FAP_usurio = ctk.CTkLabel(framedp_acessos, text="FAP usuário", width=20)
    entry_FAP_usurio = ctk.CTkEntry(framedp_acessos, width=20)

    label_FAP_usurio.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_FAP_usurio.grid(row=3, column=0, padx=10, pady=5, sticky="new")


    label_FAP_senha = ctk.CTkLabel(framedp_acessos, text="FAP senha", width=20)
    entry_FAP_senha = ctk.CTkEntry(framedp_acessos, width=20)

    label_FAP_senha.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entry_FAP_senha.grid(row=3, column=1, padx=10, pady=5, sticky="new")


    label_Empregador_WEB_usurio = ctk.CTkLabel(framedp_acessos, text="Empregador WEB usuário", width=20)
    entry_Empregador_WEB_usurio = ctk.CTkEntry(framedp_acessos, width=20)

    label_Empregador_WEB_usurio.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_Empregador_WEB_usurio.grid(row=5, column=0, padx=10, pady=5, sticky="new")


    label_Empregador_WEB_senha = ctk.CTkLabel(framedp_acessos, text="Empregador WEB senha", width=20)
    entry_Empregador_WEB_senha = ctk.CTkEntry(framedp_acessos, width=20)

    label_Empregador_WEB_senha.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    entry_Empregador_WEB_senha.grid(row=5, column=1, padx=10, pady=5, sticky="new")

#------------------------------BPO

    frameBPO = ctk.CTkFrame(Viewer.tab("BPO"), border_width=largura_borda, border_color=cor_de_borda)
    frameBPO.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    label_Sistema = ctk.CTkLabel(frameBPO, text="Sistema")
    entry_Sistema = ctk.CTkEntry(frameBPO)

    label_Sistema.grid(row=0, column=0, padx=10, pady=3, sticky="new")
    entry_Sistema.grid(row=1, column=0, padx=10, pady=3, sticky="new")


    label_Site_Bpo = ctk.CTkLabel(frameBPO, text="Site")
    entry_Site_Bpo = ctk.CTkEntry(frameBPO)

    label_Site_Bpo.grid(row=0, column=1, padx=10, pady=3, sticky="new")
    entry_Site_Bpo.grid(row=1, column=1, padx=10, pady=3, sticky="new")


    label_Usuario = ctk.CTkLabel(frameBPO, text="Usuário")
    entry_Usurio = ctk.CTkEntry(frameBPO, width=50)

    label_Usuario.grid(row=0, column=2, padx=10, pady=3, sticky="new")
    entry_Usurio.grid(row=1, column=2, padx=10, pady=3, sticky="new")


    label_Senha_simples = ctk.CTkLabel(frameBPO, text="Senha simples")
    entry_Senha_simples = ctk.CTkEntry(frameBPO, width=50)

    label_Senha_simples.grid(row=2, column=0, padx=10, pady=3, sticky="new")
    entry_Senha_simples.grid(row=3, column=0, padx=10, pady=3, sticky="new")


    label_Banco_1 = ctk.CTkLabel(frameBPO, text="Banco 1")
    entry_Banco_1 = ctk.CTkEntry(frameBPO, width=50)

    label_Banco_1.grid(row=2, column=1, padx=10, pady=3, sticky="new")
    entry_Banco_1.grid(row=3, column=1, padx=10, pady=3, sticky="new")


    label_Banco_2 = ctk.CTkLabel(frameBPO, text="Banco 2")
    entry_Banco_2 = ctk.CTkEntry(frameBPO, width=50)

    label_Banco_2.grid(row=2, column=2, padx=10, pady=3, sticky="new")
    entry_Banco_2.grid(row=3, column=2, padx=10, pady=3, sticky="new")

    frameBPOtp = ctk.CTkFrame(frameBPO, border_width=largura_borda, border_color=cor_de_borda)
    frameBPOtp.grid(row=4, column=0,columnspan=3, padx=10, pady=5, sticky="w")

    label_Tipo_de_BPO = ctk.CTkLabel(frameBPOtp, text="Tipo de BPO")
    entry_Tipo_de_BPO = ctk.CTkEntry(frameBPOtp, width=90)

    label_Tipo_de_BPO.grid(row=4, column=0, padx=10, pady=3, sticky="new")
    entry_Tipo_de_BPO.grid(row=4, column=1, padx=10, pady=3, sticky="new")


    label_Observaes_gerais_bpo = ctk.CTkLabel(frameBPO, text="Observações gerais")
    entry_Observaes_gerais_bpo = ctk.CTkTextbox(frameBPO, width=750, height=200)

    label_Observaes_gerais_bpo.grid(row=5, column=0, padx=10, pady=3, sticky="w")
    entry_Observaes_gerais_bpo.grid(row=6, column=0,columnspan=3, padx=10, pady=3, sticky="new")


def limparcampos():
    NumeroID.configure(text=f"" )
    Frame_dados_cliente_titulo.configure(text=f"")
    entry_Nome_empresa.delete(0, 'end')
    entry_CNPJ.delete(0, 'end')
    entry_Municpio.delete(0, 'end')
    entry_Atividade.delete(0, 'end')
    entry_Data_abertura_.delete(0, 'end')
    entry_Link_WhatsApp.delete(0, 'end')
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
    entry_Cdigo_e_cac.delete(0, 'end')
    entry_Senha_EAC.delete(0, 'end')
    entry_Cdigo_Simples.delete(0, 'end')
    entry_Nmero_de_livros_ECD.delete(0, 'end')
    entry_Ano_Nmero_de_livros_ECD.delete(0, 'end')
    entry_Nmero_de_livros_ECF.delete(0, 'end')
    entry_Ano_Nmero_de_livros_ECF.delete(0, 'end')
    entry_Inscrio_estadual.delete(0, 'end')
    entry_Nmero_CSC.delete(0, 'end')
    entry_Site_caixa_postal.delete(0, 'end')
    entry_Inscrio_municipal.delete(0, 'end')
    entry_Site.delete(0, 'end')
    entry_Login.delete(0, 'end')
    entry_Senha.delete(0, 'end')
    entry_Demais_senhas.delete(0, 'end')
    entry_Senha_Abertura_Processos.delete(0, 'end')
    entry_Observaes.delete('1.0', 'end')
    entry_ltima_alterao_contratual_.delete(0, 'end')
    entry_Nmero_alterao_contratual.delete(0, 'end')
    entry_Observaes_gerais_Societario.delete('1.0', 'end')
    entry_Data_vencimento_Func.delete(0, 'end')
    entry_Data_vencimento_Sanitario.delete(0, 'end')
    entry_Data_vencimento_Ambiental.delete(0, 'end')
    entry_Data_vencimento_Bombeiros.delete(0, 'end')
    entry_Quantidade_de_funcionrios.delete(0, 'end')
    entry_Quantidade_de_scios.delete(0, 'end')
    entry_Esocial_usurio.delete(0, 'end')
    entry_Esocial_senha.delete(0, 'end')
    entry_Esocial_cdigo_de_acesso.delete(0, 'end')
    entry_FAP_usurio.delete(0, 'end')
    entry_FAP_senha.delete(0, 'end')
    entry_Empregador_WEB_usurio.delete(0, 'end')
    entry_Empregador_WEB_senha.delete(0, 'end')
    entry_Sistema.delete(0, 'end')
    entry_Site_Bpo.delete(0, 'end')
    entry_Usurio.delete(0, 'end')
    entry_Senha_simples.delete(0, 'end')
    entry_Banco_1.delete(0, 'end')
    entry_Banco_2.delete(0, 'end')
    entry_Tipo_de_BPO.delete(0, 'end')
    entry_Observaes_gerais_bpo.delete('1.0', 'end')



    entry_Estado.set(siglas_estados[0]) 
    entry_Ativo.set(yes_or_not[0]) 
    entry_Formas_de_tributao.set(formasdetributacao[0]) 
    entry_Folha_de_pagamento.set(not_or_yes[0]) 
    entry_Domiclio_eletrnico.set(not_or_yes[0]) 
    entry_Certificado_digital.set(not_or_yes[0]) 
    entry_Estado_estaduais.set(siglas_estados[0])
    entry_Credenciamento_NFE.set(not_or_yes[0]) 
    entry_Alvara_de_funcionamento.set(not_or_yes[0]) 
    entry_Alvara_sanitrio.set(not_or_yes[0]) 
    entry_Licenca_ambiental.set(not_or_yes[0]) 
    entry_Bombeiros.set(not_or_yes[0]) 
    entry_Folha_de_pagto.set(not_or_yes[0]) 
    entry_Prolabore.set(not_or_yes[0])


def Importardados(idcliente):
    Listadedados, identificadores,qr = dbc.getclientdata_toEdit(idcliente)
    
    limparcampos()

    if Listadedados[1]!= "N/A" and Listadedados[0] is not None:
        Frame_dados_cliente_titulo.configure(text=f"EMPRESA: {Listadedados[1]} (ID:{Listadedados[0]})")
    else:
        Frame_dados_cliente_titulo.configure(text=f"")
    ### Cliente
    NumeroID.configure(text=f"ID Cliente: {Listadedados[0]}" ) # Campo id do banco de dados
    
    entry_Nome_empresa.insert(0,Listadedados[1]) # Campo nome_empresa do banco de dados
    
    entry_CNPJ.insert(0,Listadedados[2]) # Campo cnpj do banco de dados
    
    entry_Estado.set(Listadedados[3]) # Campo uf do banco de dados
    
    entry_Municpio.insert(0,Listadedados[4]) # Campo municipio do banco de dados
    
    entry_Atividade.insert(0,Listadedados[5]) # Campo atividade do banco de dados
   
    entry_Data_abertura_.insert(0,Listadedados[6]) # Campo data_abertura do banco de dados
    
    entry_Ativo.set(Listadedados[7]) # Campo ativo do banco de dados
    
    entry_Link_WhatsApp.insert(0,Listadedados[68])# Campo link_whatsapp do banco de dados

    ### Gerais

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
    

    entry_Cdigo_e_cac.insert(0,Listadedados[24]) # Campo codigo_ecac do banco de dados
    entry_Senha_EAC.insert(0,Listadedados[25]) # Campo senha_ecac do banco de dados
    entry_Cdigo_Simples.insert(0,Listadedados[26]) # Campo codigo_simples do banco de dados
    entry_Nmero_de_livros_ECD.insert(0,"")
    entry_Ano_Nmero_de_livros_ECD.insert(0,"")
    entry_Nmero_de_livros_ECF.insert(0,"")
    entry_Ano_Nmero_de_livros_ECF.insert(0,"")
    
    ##Estaduais

    entry_Estado_estaduais.set(Listadedados[3])
    #entry_UF.insert(0,Listadedados[25]) # Campo senha_ecac do banco de dados
    entry_Inscrio_estadual.insert(0,Listadedados[28]) # Campo inscricao_estadual do banco de dados
    entry_Credenciamento_NFE.set(Listadedados[29]) # Campo estado do banco de dados
    entry_Nmero_CSC.insert(0,Listadedados[30]) # Campo inscricao_estadual do banco de dados
    entry_Site_caixa_postal.insert(0,Listadedados[31]) # Campo credenciamento_nfe do banco de dados
    #entry_Livros_Fiscais_Entrada_Ano_Nmero.insert(0,Listadedados[30]) # Campo numero_csc do banco de dados
    #entry_Livros_Fiscais_Inventrio_Ano_Nmero.insert(0,Listadedados[31]) # Campo site_caixa_postal do banco de dados
    
    ## Municipais

    entry_Inscrio_municipal.insert(0,Listadedados[32]) # Campo inscricao_municipal do banco de dados
    entry_Site.insert(0,Listadedados[33]) # Campo site do banco de dados
    entry_Login.insert(0,Listadedados[34]) # Campo login do banco de dados
    entry_Senha.insert(0,Listadedados[35]) # Campo senha do banco de dados
    entry_Demais_senhas.insert(0,Listadedados[70]) # Campo 'municipal_demais_senhas' do banco de dados
    entry_Senha_Abertura_Processos.insert(0,Listadedados[71]) # Campo municipal_senha_abertura_processos do banco de dados
    entry_Observaes.insert('1.0',Listadedados[69]) # Campo 'municipal_observacoes' do banco de dados
    



    ## Societario

    entry_Alvara_de_funcionamento.set(Listadedados[36]) # Campo alvara_funcionamento do banco de dados
    entry_Data_vencimento_Func.insert(0,Listadedados[37]) # Campo data_vencimento_alvara_funcionamento do banco de dados
    entry_Alvara_sanitrio.set(Listadedados[38]) # Campo alvara_sanitario do banco de dados
    entry_Data_vencimento_Sanitario.insert(0,Listadedados[39]) #Campo  data_vencimento_alvara_sanitario'do banco de dados
    entry_Licenca_ambiental.set(Listadedados[40]) # Campo licenca_ambiental do banco de dados
    entry_Data_vencimento_Ambiental.insert(0,Listadedados[41]) #Campo  data_vencimento_licenca_ambiental'do banco de dados

    entry_Bombeiros.set(Listadedados[42]) # Campo dbombeiros do banco de dados
    entry_Data_vencimento_Bombeiros.insert(0,Listadedados[43]) #Campo  data_vencimento_bombeiros'do banco de dados
    entry_ltima_alterao_contratual_.insert(0,Listadedados[44]) # Campo ultima_alteracao_contratual do banco de dados
    entry_Nmero_alterao_contratual.insert(0,Listadedados[45]) # Campo numero_alteracao_contratual do banco de dados
    entry_Observaes_gerais_Societario.insert('1.0',Listadedados[46]) # Campo observacoes_gerais_societario do banco de dados
    
    ## Deparamento Pessoal 
    

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

    entry_Sistema.insert(0,Listadedados[58]) # Campo sistema_bpo do banco de dados
    entry_Site_Bpo.insert(0,Listadedados[59]) # Campo site_bpo do banco de dados
    entry_Usurio.insert(0,Listadedados[60]) # Campo usuario_bpo do banco de dados
    entry_Senha_simples.insert(0,Listadedados[61]) # Campo senha_simples_bpo do banco de dados
    entry_Banco_1.insert(0,Listadedados[62]) # Campo banco1 do banco de dados
    entry_Banco_2.insert(0,Listadedados[63]) # Campo banco2 do banco de dados
    entry_Tipo_de_BPO.insert(0,Listadedados[64]) # Campo tipo_bpo do banco de dados
    entry_Observaes_gerais_bpo.insert('1.0',Listadedados[65])