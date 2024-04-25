import customtkinter as ctk
import Modulos.Database.Meis as dbm
import tkinter as tk
from tkinter import *
from ttkthemes import ThemedStyle
from tkinter import ttk
import Modulos.Mei.Func_mei as Func_Mei


def criarbotoes(Viewer,frameprincipal,Caminho_Logo_Edit,Caminho_Logo_Add,Caminho_Logo_Rem):
    global Tipo,frame_dados_mei,Contratante,id,entry_Nome,entry_Situao,entry_Identificao,entry_CNPJ,entry_Tributao,entry_Data_abertura_,entry_Prefeitura,entry_Login,entry_Senha,entry_Pendncia_de_Recolhimentos,entry_Entrega_de_DAS_Mensal,entry_E_mail,entry_Pendncias,entry_Observaes,entry_CPF,entry_Cdigo_de_Acesso,entry_Senha_GOV,entry_Nvel_GOV,entry_Endereo,entry_Inscrio_Estadual,entry_Inscrio_Municipal,entry_Certificado_Digital,entry_Modelo_Datavix,entry_Homologado___Sindicato,entry_Vencimento_,entry_Ano,entry_Faturamento,TreeViewParceiras,scrollbarParceiras,bt_Editar_MEI_Parceiras,TabViewGlobal
    TabViewGlobal = Viewer
    
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

    def ativarbotãoEditar(*args):
        selecao = TreeViewParceiras.selection()

        if selecao:
            valor = bt_Editar_MEI_Parceiras.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_Editar_MEI_Parceiras.configure(state='normal')  
        else:
            bt_Editar_MEI_Parceiras.configure(state='disabled') 
    

    frame_dados_mei=frameprincipal
    yes_or_not = [
        "SIM","NÃO"
    ]

    cor_de_borda = "gray50"
    largura_borda = 2

### Empresa
    ScrollFrameEmpresas = ctk.CTkScrollableFrame(Viewer.tab("Empresa"), border_width=largura_borda, border_color=cor_de_borda,width=900, height=470)
    ScrollFrameEmpresas.grid(row=0, column=0, sticky="n")
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


    label_Situao = ctk.CTkLabel(FrameDadosEmpresas, text="Ativo")
    entry_Situao = ctk.CTkComboBox(FrameDadosEmpresas,values=yes_or_not)

    label_Situao.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Situao.grid(row=1, column=3, padx=10, pady=5, sticky="new")

    
    label_CNPJ = ctk.CTkLabel(FrameDadosEmpresas, text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(FrameDadosEmpresas)

    label_CNPJ.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_CNPJ.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    label_Data_abertura_ = ctk.CTkLabel(FrameDadosEmpresas, text="Data abertura (dd/mm/aaaa)")
    entry_Data_abertura_ = ctk.CTkEntry(FrameDadosEmpresas)

    label_Data_abertura_.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    entry_Data_abertura_.grid(row=1, column=5, padx=10, pady=5, sticky="new")
    

    label_Identificao = ctk.CTkLabel(FrameDadosEmpresas, text="Identificação")
    entry_Identificao = ctk.CTkEntry(FrameDadosEmpresas)

    label_Identificao.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    entry_Identificao.grid(row=0, column=5, padx=10, pady=5, sticky="new")


    label_Tributao = ctk.CTkLabel(FrameDadosEmpresas, text="Tributação")
    entry_Tributao = ctk.CTkEntry(FrameDadosEmpresas)

    label_Tributao.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Tributao.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    label_E_mail = ctk.CTkLabel(FrameDadosEmpresas, text="E-mail")
    entry_E_mail = ctk.CTkEntry(FrameDadosEmpresas)

    label_E_mail.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_E_mail.grid(row=2, column=3,columnspan=3, padx=10, pady=5, sticky="new")

    label_Endereo = ctk.CTkLabel(FrameDadosEmpresas, text="Endereço")
    entry_Endereo = ctk.CTkEntry(FrameDadosEmpresas)

    label_Endereo.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_Endereo.grid(row=3, column=1,columnspan=5, padx=10, pady=5, sticky="new")

    FrameGerais = ctk.CTkFrame(FrameEmpresas, border_width=largura_borda, border_color=cor_de_borda)
    FrameGerais.grid(row=3, column=0, sticky="new")
   
    ## Dados Gerias de Acessos 
    FrameAcessosEprefeituras = ctk.CTkFrame(FrameGerais, border_width=largura_borda, border_color=cor_de_borda)
    FrameAcessosEprefeituras.grid(row=0, column=0,columnspan=6, padx=10,pady=5, sticky="nsew")

    label_Prefeitura = ctk.CTkLabel(FrameAcessosEprefeituras, text="Prefeitura")
    entry_Prefeitura = ctk.CTkEntry(FrameAcessosEprefeituras,width=150)

    label_Prefeitura.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Prefeitura.grid(row=0, column=1, padx=10, pady=5, sticky="new")


    label_Login = ctk.CTkLabel(FrameAcessosEprefeituras, text="Login")
    entry_Login = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Login.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Login.grid(row=0, column=3, padx=10, pady=5, sticky="new")

    label_Senha = ctk.CTkLabel(FrameAcessosEprefeituras, text="Senha")
    entry_Senha = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Senha.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    entry_Senha.grid(row=0, column=5, padx=10, pady=5, sticky="new")

    label_CPF = ctk.CTkLabel(FrameAcessosEprefeituras, text="CPF")
    entry_CPF = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_CPF.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_CPF.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    label_Cdigo_de_Acesso = ctk.CTkLabel(FrameAcessosEprefeituras, text="Código de Acesso")
    entry_Cdigo_de_Acesso = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Cdigo_de_Acesso.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Cdigo_de_Acesso.grid(row=1, column=3, padx=10, pady=5, sticky="new")

    label_Senha_GOV = ctk.CTkLabel(FrameAcessosEprefeituras, text="Senha GOV")
    entry_Senha_GOV = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Senha_GOV.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_Senha_GOV.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    label_Nvel_GOV = ctk.CTkLabel(FrameAcessosEprefeituras, text="Nível GOV")
    entry_Nvel_GOV = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Nvel_GOV.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_Nvel_GOV.grid(row=2, column=3, padx=10, pady=5, sticky="new")

    label_Inscrio_Estadual = ctk.CTkLabel(FrameAcessosEprefeituras, text="Inscrição Estadual")
    entry_Inscrio_Estadual = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Inscrio_Estadual.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    entry_Inscrio_Estadual.grid(row=1, column=5, padx=10, pady=5, sticky="new")


    label_Inscrio_Municipal = ctk.CTkLabel(FrameAcessosEprefeituras, text="Inscrição Municipal")
    entry_Inscrio_Municipal = ctk.CTkEntry(FrameAcessosEprefeituras)

    label_Inscrio_Municipal.grid(row=2, column=4, padx=10, pady=5, sticky="w")
    entry_Inscrio_Municipal.grid(row=2, column=5, padx=10, pady=5, sticky="new")


    label_Certificado_Digital = ctk.CTkLabel(FrameAcessosEprefeituras, text="Certificado Digital")
    entry_Certificado_Digital = ctk.CTkComboBox(FrameAcessosEprefeituras,values=yes_or_not)

    label_Certificado_Digital.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_Certificado_Digital.grid(row=3, column=1, padx=10, pady=5, sticky="new")

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

    label_Modelo_Datavix = ctk.CTkLabel(FrameParceiras, text="Modelo Datavix")
    entry_Modelo_Datavix = ctk.CTkEntry(FrameParceiras)

    label_Modelo_Datavix.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Modelo_Datavix.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Homologado___Sindicato = ctk.CTkLabel(FrameParceiras, text="Homologado - Sindicato")
    entry_Homologado___Sindicato = ctk.CTkEntry(FrameParceiras)

    label_Homologado___Sindicato.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_Homologado___Sindicato.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Vencimento_ = ctk.CTkLabel(FrameParceiras, text="Vencimento (dd/mm/aaaa)")
    entry_Vencimento_ = ctk.CTkEntry(FrameParceiras)

    label_Vencimento_.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Vencimento_.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

    
    

    TreeViewParceiras = ttk.Treeview(FrameParceiras, columns=("#","Nome","Pendências","Situação"), show='headings')
    TreeViewParceiras.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(1,0), pady=(5,10))
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
    scrollbarParceiras = ctk.CTkScrollbar(FrameParceiras, command=TreeViewParceiras.yview,height=100)
    scrollbarParceiras.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
    TreeViewParceiras.configure(yscrollcommand=scrollbarParceiras.set)    

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_MEI_Parceiras = ctk.CTkButton(master=FrameParceiras,image=logo_editar, text="Editar",command=lambda: Func_Mei.editar_MEI(TreeViewParceiras,tela_Mae))
    bt_Editar_MEI_Parceiras.grid(row=3, column=0,columnspan=3, sticky="nsew", padx=(1,0), pady=(5,10))
    bt_Editar_MEI_Parceiras.configure(state='disabled') 

#DASN
    FrameDas = ctk.CTkFrame(Viewer.tab("DASN"), border_width=largura_borda, border_color=cor_de_borda)
    FrameDas.grid(row=0, column=0, sticky="n")
    Viewer.tab("DASN").grid_rowconfigure(0, weight=1)
    Viewer.tab("DASN").grid_columnconfigure(0, weight=1)


    label_Ano_dasn = ctk.CTkLabel(FrameDas, text="Ano")
    entry_Ano_dasn= ctk.CTkEntry(FrameDas)

    label_Ano_dasn.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Ano_dasn.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Faturamento = ctk.CTkLabel(FrameDas, text="Faturamento")
    entry_Faturamento = ctk.CTkEntry(FrameDas)

    label_Faturamento.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_Faturamento.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Observaes_dasn = ctk.CTkLabel(FrameDas, text="Observações")
    entry_Observaes_dasn = ctk.CTkEntry(FrameDas)

    label_Observaes_dasn.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Observaes_dasn.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add = ctk.CTkButton(FrameDas,image=logo_add, text="Adicionar",command="")
    bt_add.grid(row=0, column=3, padx=5, pady=5, sticky="new")

    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir = ctk.CTkButton(FrameDas,image=logo_excluir, text="Excluir",command=lambda: "")
    bt_Excluir.grid(row=1, column=3, padx=5, pady=5, sticky="new")

    TreeviewDas = ttk.Treeview(FrameDas, columns=("Ano","Faturamento","Observações"), show='headings')
    TreeviewDas.grid(row=2, column=0,columnspan=4, sticky="nsew", padx=(5,5), pady=(5,10))
    TreeviewDas.bind('<<TreeviewSelect>>')

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







def limparbotões():
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

    try:
        for item in TreeViewParceiras.get_children():
                TreeViewParceiras.delete(item)     
    except Exception :
            pass 

def Importardados(idcliente,Dadosparateladeedição):
    global tela_Mae
    tela_Mae = Dadosparateladeedição

    Listadedados, identificadores,qr,meis = dbm.getmeidata_toEdit(idcliente)

    limparbotões()

    if Listadedados[0]:
        frame_dados_mei[1].configure(text=f"EMPRESA: {Listadedados[3]} (ID:{Listadedados[0]})")
        frame_dados_mei[2].configure(text=f"TIPO: {Listadedados[4]}")

    if Listadedados[1] != "N/A":
        nomemei=  dbm.GetnameMEI(Listadedados[1])
        
        frame_dados_mei[0].configure(text=f"CONTRATANTE: {nomemei[0]}")
        TreeViewParceiras.grid_remove()
        scrollbarParceiras.grid_remove()
        bt_Editar_MEI_Parceiras.grid_remove()
    else:
        frame_dados_mei[0].configure(text=f"")
        TreeViewParceiras.grid(row=2, column=0,columnspan=3, sticky="nsew", padx=(1,0), pady=(5,10))
        scrollbarParceiras.grid(row=2, column=4, padx=(0,10), pady=(5,10), sticky="nsew")
        bt_Editar_MEI_Parceiras.grid(row=3, column=0,columnspan=3, sticky="n", padx=(1,0), pady=(5,10))

    entry_Nome.insert(0,Listadedados[3]) # Campo nome do banco de dados


    entry_Situao.set(Listadedados[2]) # Campo situacao do banco de dados

    entry_Identificao.insert(0,Listadedados[4]) # Campo identificacao do banco de dados

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

    #entry_Ano_dasn.insert(0,Listadedados[28]) # Campo created_at do banco de dados

    #entry_Faturamento.insert(0,Listadedados[29]) # Campo updated_at do banco de dados

    #entry_Observaes_dasn.insert(0,Listadedados[29]) # Campo updated_at do banco de dados

    
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
        
