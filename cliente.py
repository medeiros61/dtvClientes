import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Database.Clients as dbc
from ttkthemes import ThemedStyle

def criartelaclientes(frame):
    global Scrollable,list_clients_frame,tv
    
    frame.pack(side=RIGHT, fill = BOTH,expand=True)

    clientes_data = dbc.getclientlist_complete()

    tv.heading("#", text="ID")
    tv.heading("Nome", text="Nome")
    tv.heading("UF", text="UF")
    tv.heading("Município", text="Município")
    tv.heading("Status", text="Status")
    #tv.heading("Opções", text="Opções")
    
    # Define o tamanho das colunas em pixels
    tv.column("#", width=50)  # ID
    tv.column("Nome", width=450)  # Nome
    tv.column("UF", width=50)  # UF
    tv.column("Município", width=100)  # Município
    tv.column("Status", width=80)  # Status
    #tv.column("Opções", width=100, stretch=False)  # Opções 

   
    #Conjunto para armazenar UF 
    #dados_uf_set = set()
    # Extrair UF e adicionar ao conjunto
    #for item in clientes_data:
    #    dados_uf_set.add((item[2]))
    # Converter o conjunto de volta para uma lista (se necessário)
    #dados_uf = list(dados_uf_set)

    #uf_filter_entry.configure(values = dados_uf)


    # Adicionando botões às linhas do Treeview
    try:
        for item in tv.get_children():
            tv.delete(item)
    except Exception :
        pass

    for result in clientes_data:
        tv.insert("", 'end', values=result)


def Removertelaclientes(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    global list_clients_frame,Scrollable,uf_filter_entry
    Scrollable = None
    ##Funções 
    #Filtro por nome 

    def filtrar(*args):
        nome = clinte_filter_entry.get() 

        uf = uf_filter_entry.get() 
        ativo = Status_filter_entry.get()
        
        if ativo == "ATIVO" :
            ativo = 1
        else:
            ativo = 0 
        
        if uf =="TODOS":
            uf = None

        if ativo =="TODOS":
            ativo = None

    
            
        clientesfiltrados = dbc.getclientlist_byfilter('nome_empresa',nome,'uf',uf,'ativo',ativo)
        try:
            for item in tv.get_children():
                tv.delete(item)     
        except Exception :
            pass
        for result in clientesfiltrados:
            tv.insert("", 'end', values=result)
   
    def ordenar(*args):
        pass

    

    #Frame FILTRO E LISTA
    
    master_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)

    #Frame dos itens do filtro 
    filter_frame = ctk.CTkFrame(master=master_frame, width=900, height=100, fg_color=("#808080"))
    filter_frame.pack(side=TOP, fill = X)
    
    #cliente Filter
    clinte_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    clinte_filter_frame.pack(side=LEFT)
    clinte_filter_lb = ctk.CTkLabel(master=clinte_filter_frame, text="Cliente",width=300)
    clinte_filter_lb.grid(row=1, column=0, padx=10, pady=(5, 5), sticky="nsew")
    clinte_filter_entry = ctk.CTkEntry(master=clinte_filter_frame)
    clinte_filter_entry.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="nsew")
    clinte_filter_entry.bind("<Return>",filtrar)

    #UF Filter
    # Lista de siglas dos estados brasileiros
    siglas_estados = [
        "TODOS","AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ]
    uf_filter_frame = ctk.CTkFrame(master=filter_frame, height=100, fg_color=("#808080"))
    uf_filter_frame.pack(side=LEFT)
    uf_filter_lb = ctk.CTkLabel(master=uf_filter_frame, text="UF",width=100)
    uf_filter_lb.grid(row=1, column=1, padx=10, pady=(5, 5), sticky="nsew")
    uf_filter_entry = ctk.CTkComboBox(master=uf_filter_frame,width=50,values=siglas_estados,command=filtrar)
    uf_filter_entry.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="nsew")
    
    Status_lista = [
        "TODOS","ATIVO","INATIVO"
    ]
    #Status Filter
    Status_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    Status_filter_frame.pack(side=LEFT)
    Status_filter_lb = ctk.CTkLabel(master=Status_filter_frame, text="Status",width=100)
    Status_filter_lb.grid(row=1, column=3, padx=10, pady=(5, 5), sticky="nsew")
    Status_filter_entry = ctk.CTkComboBox(master=Status_filter_frame,width=50,values=Status_lista,command=filtrar)
    Status_filter_entry.grid(row=2, column=3, padx=10, pady=(5, 5), sticky="nsew")
                            
    #Ordenar Por..(tipo de ordenação)  Filter
    ordbytype_lista = [
        "ALFABETICA","DATA DE CADASTRO"
    ]
    ordbytype_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbytype_filter_frame.pack(side=LEFT)
    ordbytype_filter_lb = ctk.CTkLabel(master=ordbytype_filter_frame, text="Ordenar por",width=50)
    ordbytype_filter_lb.grid(row=1, column=4, padx=10, pady=(5, 5), sticky="nsew")
    ordbytype_filter_entry = ctk.CTkComboBox(master=ordbytype_filter_frame,width=50,command=ordenar,values=ordbytype_lista)
    ordbytype_filter_entry.grid(row=2, column=4, padx=10, pady=(5, 5), sticky="nsew")
    
    ordbycresdec_lista = [
        "CRESCENTE","DECRESCENTE"
    ]
    #ordenar Por (Crescente e decrescente ) Filter
    ordbycresdec_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbycresdec_filter_frame.pack(side=LEFT)
    ordbycresdec_filter_lb = ctk.CTkLabel(master=ordbycresdec_filter_frame, text="Ordenar por",width=50)
    ordbycresdec_filter_lb.grid(row=1, column=5, padx=10, pady=(5, 5), sticky="nsew")
    ordbycresdec_filter_entry = ctk.CTkComboBox(master=ordbycresdec_filter_frame,width=50,command=ordenar,values=ordbycresdec_lista)
    ordbycresdec_filter_entry.grid(row=2, column=5, padx=10, pady=(5, 5), sticky="nsew")
  
    #Listagem de clientes
    list_clients_frame = ctk.CTkFrame(master=master_frame, width=900, height=480, fg_color=("#808080"))
    list_clients_frame.pack(side=TOP, fill = X)
    
    global tv
    
    EstilodeTela = ThemedStyle(list_clients_frame)
    EstilodeTela.set_theme("scidsand")
    tv = ttk.Treeview(list_clients_frame, columns=("#","Nome","UF","Município","Status"), show='headings')
    tv.grid(row=0, column=0, sticky="nsew")

   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(list_clients_frame, command=tv.yview,height=500)
    scrollbar.grid(row=0, column=1, sticky="nsew")
    tv.configure(yscrollcommand=scrollbar.set)
    #frameTreeview.configure(height=480)  # +4 para margem



