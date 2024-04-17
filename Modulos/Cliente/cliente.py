import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Modulos.Database.Clients as dbc
import Modulos.Cliente.Func_cliente as Func_cli
import Modulos.imagens.ImagensClientes as Imagens_DataBase
from ttkthemes import ThemedStyle
import Modulos.Cliente.Cliente_V_E as Tela_Edit_C 


def criartelaclientes(frame,DadosUsuario):
    try:
        global Scrollable,list_clients_frame,TreeviewClientes,tipo_usuario
        tipo_usuario= DadosUsuario[2]
        if tipo_usuario == 'user':
            bt_Excluir_clients.grid_remove()
        
        
        
        filtrar()
        verificarseleção()
        frame.pack(side=RIGHT, fill = BOTH,expand=True)

        #clientes_data = dbc.getclientlist_complete()

        #Conjunto para armazenar UF 
        #dados_uf_set = set()
        # Extrair UF e adicionar ao conjunto
        #for item in clientes_data:
        #    dados_uf_set.add((item[2]))
        # Converter o conjunto de volta para uma lista (se necessário)
        #dados_uf = list(dados_uf_set)

        #uf_filter_entry.configure(values = dados_uf)


        # Adicionando botões às linhas do Treeview
        #try:
        #    for item in TreeviewClientes.get_children():
        #        TreeviewClientes.delete(item)
        #except Exception :
        #    pass

        #for result in clientes_data:
        #    TreeviewClientes.insert("", 'end', values=result)
    finally:
        pass

def Removertelaclientes(frame): 
    try:
        frame.pack_forget()
    finally:
        pass
def parametrosinicias(frame):
    global list_clients_frame,Scrollable,uf_filter_entry,filtrar,verificarseleção,TreeviewClientes,frame_edição_dados,bt_Excluir_clients
    Scrollable = None
    #####################################  FUNÇÕES   #####################################################
   
    #FUNÇÃO PARA FILTRAR
    def filtrar(*args):
        nome = clinte_filter_entry.get() 

        uf = uf_filter_entry.get() 
        ativo = Status_filter_entry.get()
        
        if ativo == "ATIVO" :
            ativo = 1
        if ativo == "INATIVO" :
            ativo = 0 
        
        if uf =="TODOS":
            uf = None

        if ativo =="TODOS":
            ativo = None

    
        global clientesfiltrados
        clientesfiltrados = dbc.getclientlist_byfilter('nome_empresa',nome,'uf',uf,'ativo',ativo)
        ordenar()
   
    #FUNÇÃO PARA ORDENAR 
    def ordenar(*args):
        global clientesfiltrados

        Ordem = ordbytype_filter_entry.get()
        TipoOrdem = ordbycresdec_filter_entry.get()
        
        if Ordem == "ALFABETICA":
            Ordem_P = 1
        if Ordem == "DATA DE CADASTRO":
            Ordem_P = 0    
        if TipoOrdem == "CRESCENTE":
            TipoOrdem_P = False
        else:    
            TipoOrdem_P = True
        
        DadosOrdenados = sorted(clientesfiltrados, key=lambda x: x[Ordem_P], reverse=TipoOrdem_P)
        
        try:
            for item in TreeviewClientes.get_children():
                TreeviewClientes.delete(item)     
        except Exception :
            pass
        for result in DadosOrdenados:
            TreeviewClientes.insert("", 'end', values=result)



    ##################################### FIM FUNÇÕES   #####################################################
     
    
    #Frame FILTRO E LISTA 
    master_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)
    
    #FRAME PARA VIZUALIZAR E EDITAR
    frame_Cliente_E_V = ctk.CTkFrame(master=frame, width=900, height=580, fg_color=("#808080"))

    frame_edição_dados = frame_Cliente_E_V    
    Dadosparateladeedição = frame_edição_dados,master_frame 

    Tela_Edit_C.parametrosinicias(frame_edição_dados,master_frame)
    #Listagem de clientes
    list_clients_frame = ctk.CTkFrame(master=master_frame, width=900, height=480, fg_color=("#808080"))
    list_clients_frame.pack(side=TOP, fill = X)
    
    #Frame dos itens do filtro ----------------------------------------------------------------------
    filter_frame = ctk.CTkFrame(master=list_clients_frame, width=900, height=100, fg_color=("#808080"))
    filter_frame.grid(row=0, column=0, sticky="nsew")
    
    
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
        "DATA DE CADASTRO","ALFABETICA"
    ]
    ordbytype_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbytype_filter_frame.pack(side=LEFT)
    ordbytype_filter_lb = ctk.CTkLabel(master=ordbytype_filter_frame, text="Ordenar por",width=100)
    ordbytype_filter_lb.grid(row=1, column=4, padx=10, pady=(5, 5), sticky="nsew")
    ordbytype_filter_entry = ctk.CTkComboBox(master=ordbytype_filter_frame,width=50,command=ordenar,values=ordbytype_lista)
    ordbytype_filter_entry.grid(row=2, column=4, padx=10, pady=(5, 5), sticky="nsew")
    
    ordbycresdec_lista = [
        "CRESCENTE","DECRESCENTE"
    ]
    #ordenar Por (Crescente e decrescente ) Filter
    ordbycresdec_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbycresdec_filter_frame.pack(side=LEFT)
    ordbycresdec_filter_lb = ctk.CTkLabel(master=ordbycresdec_filter_frame, text="Ordenar por",width=100)
    ordbycresdec_filter_lb.grid(row=1, column=5, padx=10, pady=(5, 5), sticky="nsew")
    ordbycresdec_filter_entry = ctk.CTkComboBox(master=ordbycresdec_filter_frame,width=50,command=ordenar,values=ordbycresdec_lista)
    ordbycresdec_filter_entry.grid(row=2, column=5, padx=10, pady=(5, 5), sticky="nsew")
  
  
    #Listagem de clientes-----------------------------------------------------------------------------

    def verificarseleção(*args):
        seleção = TreeviewClientes.selection()

        if seleção:
            valor = bt_Editar_clients.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_Editar_clients.configure(state='normal') 
                bt_Excluir_clients.configure(state='normal') 
                bt_Comentar_clients.configure(state='normal') 
        else:
            
            bt_Editar_clients.configure(state='disabled') 
            bt_Excluir_clients.configure(state='disabled') 
            bt_Comentar_clients.configure(state='disabled')

    
    
    EstilodeTela = ThemedStyle(list_clients_frame)
    EstilodeTela.set_theme("scidsand")
    TreeviewClientes = ttk.Treeview(list_clients_frame, columns=("#","Nome","UF","Município","Status"), show='headings')
    TreeviewClientes.grid(row=1, column=0, sticky="nsew")
    TreeviewClientes.bind('<<TreeviewSelect>>', verificarseleção)
    
    # Define o as colunas
    TreeviewClientes.heading("#", text="ID")
    TreeviewClientes.heading("Nome", text="Nome")
    TreeviewClientes.heading("UF", text="UF")
    TreeviewClientes.heading("Município", text="Município")
    TreeviewClientes.heading("Status", text="Status")
    #TreeviewClientes.heading("Opções", text="Opções")
    
    # Define o tamanho das colunas em pixels
    TreeviewClientes.column("#", width=50)  # ID
    TreeviewClientes.column("Nome", width=450)  # Nome
    TreeviewClientes.column("UF", width=50)  # UF
    TreeviewClientes.column("Município", width=100)  # Município
    TreeviewClientes.column("Status", width=80)  # Status
    #TreeviewClientes.column("Opções", width=100, stretch=False)  # Opções 
   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(list_clients_frame, command=TreeviewClientes.yview,height=500)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    TreeviewClientes.configure(yscrollcommand=scrollbar.set)
    
    #Frame dos botões de ação ----------------------------------------------------------------------
    bt_action_frame = ctk.CTkFrame(master=list_clients_frame, fg_color=("#808080"))
    bt_action_frame.grid(row=2, column=0, sticky="nsew")
    
    


    Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel =Imagens_DataBase.baixarimagemPgclientes()  

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add_clients = ctk.CTkButton(master=bt_action_frame,image=logo_add, text="Adicionair Cliente",command= Func_cli.Adicionar_cliente)
    bt_add_clients.grid(row=0, column=0,  padx=5, pady=5,sticky="nsew")

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_clients = ctk.CTkButton(master=bt_action_frame,image=logo_editar, text="Editar",command=lambda: Func_cli.editar_cliente(TreeviewClientes,Dadosparateladeedição))
    bt_Editar_clients.grid(row=0, column=2,   padx=5, pady=5,sticky="nsew")
    
    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir_clients = ctk.CTkButton(master=bt_action_frame,image=logo_excluir, text="Excluir Cliente",command=lambda: Func_cli.excluir_cliente(TreeviewClientes))
    bt_Excluir_clients.grid(row=0, column=3,   padx=5, pady=5,sticky="nsew")

    logo_comentar = PhotoImage(file=Caminho_Logo_Comt).subsample(25, 25)
    bt_Comentar_clients = ctk.CTkButton(master=bt_action_frame,image=logo_comentar, text="Adicionar Comentario",command=lambda: Func_cli.comentar_cliente(TreeviewClientes))
    bt_Comentar_clients.grid(row=0, column=4,  padx=5, pady=5,sticky="nsew")

    logo_excel = PhotoImage(file=Caminho_Logo_Excel).subsample(30, 30)
   
    bt_exportar_clients = ctk.CTkButton(master=bt_action_frame, image=logo_excel,text="Exportar clientes",command=Func_cli.Exportar_clientes)
    bt_exportar_clients.grid(row=0, column=5,  padx=5, pady=5,sticky="nsew")



