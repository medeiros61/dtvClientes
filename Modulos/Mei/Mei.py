import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Modulos.Database.Meis as dbmei
import Modulos.imagens.ImagensClientes as Imagens_DataBase
from ttkthemes import ThemedStyle
import Modulos.Mei.Func_mei as Func_Mei
import Modulos.Mei.Mei_V_E as Tela_Edit_C 

def criartelaMEI(frame,DadosUsuario):
    try:
        global Scrollable,list_MEI_frame,TreeviewMEI,tipo_usuario
        tipo_usuario= DadosUsuario[2]
        if tipo_usuario == 'user':
            bt_Excluir_MEI.grid_remove()
        
        filtrar()
        verificarseleção()
        Tela_Edit_C.RemovertelaEdit_MEI()
        frame.pack(side=RIGHT, fill = BOTH,expand=True)
    finally:
        print("Entrou na tela de MEI")

def RemovertelaMEI(frame): 
    try:
        frame.pack_forget()
    finally:
        pass
    
def parametrosinicias(frame):

    global list_MEI_frame,Scrollable,filtrar,verificarseleção,TreeviewMEI,bt_Excluir_MEI
    Scrollable = None
    #####################################  FUNÇÕES   #####################################################
        
    #FUNÇÃO PARA FILTRAR
    def filtrar(*args):
        nome = MEI_filter_entry.get() 

        identificacao = Identificação_filter_entry.get() 
        ativo = Status_filter_entry.get()
        
        if ativo == "ATIVO" :
            ativo = 1
        if ativo == "INATIVO" :
            ativo = 0 
        
        if identificacao =="TODOS":
            identificacao = None

        if ativo =="TODOS":
            ativo = None

    
        global MEIfiltrados
        MEIfiltrados = dbmei.getMEIlist_byfilter('nome',nome,'identificacao',identificacao,'situacao',ativo)
        ordenar()
   
    #FUNÇÃO PARA ORDENAR 
    def ordenar(*args):
        global MEIfiltrados

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
        
        DadosOrdenados = sorted(MEIfiltrados, key=lambda x: x[Ordem_P], reverse=TipoOrdem_P)
        
        try:
            for item in TreeviewMEI.get_children():
                TreeviewMEI.delete(item)     
        except Exception :
            pass
        for result in DadosOrdenados:
            TreeviewMEI.insert("", 'end', values=result)


    
    def verificarseleção(*args):
        seleção = TreeviewMEI.selection()

        if seleção:
            valor = bt_Editar_MEI.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_Editar_MEI.configure(state='normal') 
                bt_Excluir_MEI.configure(state='normal') 
                bt_Comentar_MEI.configure(state='normal') 
            
            botãoparceiras = bt_add_MEI_Parceira.cget("state")  # Obtém o estado atual do botão
            identificação = TreeviewMEI.item(seleção[0])['values'][2]
            
            if botãoparceiras == "disabled" and identificação == 'Contratante':   
                    bt_add_MEI_Parceira.configure(state='normal') 
            else:
                if identificação != 'Contratante':
                    bt_add_MEI_Parceira.configure(state='disabled')     
        else:
            bt_add_MEI_Parceira.configure(state='disabled')  
            bt_Editar_MEI.configure(state='disabled') 
            bt_Excluir_MEI.configure(state='disabled') 
            bt_Comentar_MEI.configure(state='disabled') 

    def editarcliente(*args):
        Func_Mei.editar_MEI(TreeviewMEI,Dadosparateladeedição)
        


    ##################################### FIM FUNÇÕES   #####################################################

    #Frame FILTRO E LISTA 
    master_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)

    #FRAME PARA VIZUALIZAR E EDITAR
    frame_MEI_E_V = ctk.CTkFrame(master=frame, width=900, height=580, fg_color=("#808080"))

    frame_edição_dados = frame_MEI_E_V    
    Dadosparateladeedição = frame_edição_dados,master_frame 

    Tela_Edit_C.parametrosinicias(frame_edição_dados,master_frame)

    #Listagem de MEI
    list_MEI_frame = ctk.CTkFrame(master=master_frame, width=900, height=480, fg_color=("#808080"))
    list_MEI_frame.grid(row=0, column=0, sticky="n")
    master_frame.grid_rowconfigure(0, weight=1)
    master_frame.grid_columnconfigure(0, weight=1)
    #Frame dos itens do filtro ----------------------------------------------------------------------
    filter_frame = ctk.CTkFrame(master=list_MEI_frame, width=900, height=100, fg_color=("#808080"))
    filter_frame.grid(row=0, column=0, sticky="nsew")
    
    
    #cliente Filter
    MEI_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    MEI_filter_frame.pack(side=LEFT)
    MEI_filter_lb = ctk.CTkLabel(master=MEI_filter_frame, text="Cliente",width=300)
    MEI_filter_lb.grid(row=1, column=0, padx=10, pady=(5, 5), sticky="nsew")
    MEI_filter_entry = ctk.CTkEntry(master=MEI_filter_frame)
    MEI_filter_entry.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="nsew")
    MEI_filter_entry.bind("<Return>",filtrar)

    #UF Filter
    # Lista de siglas dos estados brasileiros
    siglas_identificação = [
        "TODOS","CONTRATANTE", "PARCEIRA"
    ]
    Identificação_filter_frame = ctk.CTkFrame(master=filter_frame, height=100, fg_color=("#808080"))
    Identificação_filter_frame.pack(side=LEFT)
    Identificação_filter_lb = ctk.CTkLabel(master=Identificação_filter_frame, text="Identificação",width=100)
    Identificação_filter_lb.grid(row=1, column=1, padx=10, pady=(5, 5), sticky="nsew")
    Identificação_filter_entry = ctk.CTkComboBox(master=Identificação_filter_frame,width=50,values=siglas_identificação,command=filtrar)
    Identificação_filter_entry.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="nsew")
    
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
  
  
    #Listagem de MEI-----------------------------------------------------------------------------

    EstilodeTela = ThemedStyle(list_MEI_frame)
    EstilodeTela.set_theme("scidsand")
    TreeviewMEI = ttk.Treeview(list_MEI_frame, columns=("#","Nome","Identificação","Status"), show='headings')
    TreeviewMEI.grid(row=1, column=0, sticky="nsew")
    TreeviewMEI.bind('<<TreeviewSelect>>', verificarseleção)
    TreeviewMEI.bind('<Double-1>',editarcliente)
    # Define o as colunas
    TreeviewMEI.heading("#", text="ID")
    TreeviewMEI.heading("Nome", text="Nome")
    TreeviewMEI.heading("Identificação", text="Identificação")
    TreeviewMEI.heading("Status", text="Status")
    #TreeviewMEI.heading("Opções", text="Opções")
    
    # Define o tamanho das colunas em pixels
    TreeviewMEI.column("#", width=30)  # ID
    TreeviewMEI.column("Nome", width=380)  # Nome
    TreeviewMEI.column("Identificação", width=80)  # UF
    TreeviewMEI.column("Status", width=80)  # Status
    #TreeviewMEI.column("Opções", width=100, stretch=False)  # Opções 
   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(list_MEI_frame, command=TreeviewMEI.yview,height=478)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    TreeviewMEI.configure(yscrollcommand=scrollbar.set)
    
    #Frame dos botões de ação ----------------------------------------------------------------------
    bt_action_frame = ctk.CTkFrame(master=list_MEI_frame, fg_color=("#808080"))
    bt_action_frame.grid(row=2, column=0, sticky="nsew")
    
    Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel =Imagens_DataBase.baixarimagemPgclientes()  

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add_MEI = ctk.CTkButton(master=bt_action_frame,image=logo_add, text="Adicionar Contratante",command=lambda: Func_Mei.Adicionar_MEI_Contratante(Dadosparateladeedição))
    bt_add_MEI.grid(row=0, column=0,  padx=5, pady=1,sticky="nsew")

    bt_add_MEI_Parceira = ctk.CTkButton(master=bt_action_frame,image=logo_add, text="Adicionar Parceira",command=lambda: Func_Mei.Adicionar_MEI_Parceira(Dadosparateladeedição))
    bt_add_MEI_Parceira.grid(row=1, column=0,  padx=5, pady=1,sticky="nsew")

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_MEI = ctk.CTkButton(master=bt_action_frame,image=logo_editar, text="Editar",command=lambda: Func_Mei.editar_MEI(TreeviewMEI,Dadosparateladeedição))
    bt_Editar_MEI.grid(row=0, column=2,   padx=5, pady=5,sticky="nsew", rowspan = 2)
    
    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir_MEI = ctk.CTkButton(master=bt_action_frame,image=logo_excluir, text="Excluir MEI",command=lambda: Func_Mei.excluir_MEI(TreeviewMEI))
    bt_Excluir_MEI.grid(row=0, column=3,   padx=5, pady=5,sticky="nsew", rowspan = 2)

    logo_comentar = PhotoImage(file=Caminho_Logo_Comt).subsample(25, 25)
    bt_Comentar_MEI = ctk.CTkButton(master=bt_action_frame,image=logo_comentar, text="Adicionar Comentario",command=lambda: Func_Mei.comentar_MEI(TreeviewMEI))
    bt_Comentar_MEI.grid(row=0, column=4,  padx=5, pady=5,sticky="nsew", rowspan = 2)

    logo_excel = PhotoImage(file=Caminho_Logo_Excel).subsample(30, 30)
   
    bt_exportar_MEI = ctk.CTkButton(master=bt_action_frame, image=logo_excel,text="Exportar MEI",command= Func_Mei.Exportar_MEIs)
    bt_exportar_MEI.grid(row=0, column=5,  padx=5, pady=5,sticky="nsew", rowspan = 2)



