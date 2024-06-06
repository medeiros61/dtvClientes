import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Modulos.Database.Users as dbu

import Modulos.Usuarios.Func_users as Func_users
import Modulos.imagens.ImagensClientes as Imagens_DataBase



def criartelaUsarios(frame,DadosUsuario):
    try:
        global Scrollable,list_user_frame,TreeviewUsuarios,tipo_usuario,Usuarioinfo
        Usuarioinfo = DadosUsuario
        tipo_usuario= DadosUsuario[2]
        if tipo_usuario == 'user':
            #bt_Excluir_user.grid_remove()
            bt_add_user.grid_remove()
            bt_exportar_user.grid_remove()

        filtrar()
        verificarseleção()
        frame.pack(side=RIGHT, fill = BOTH,expand=True)
    finally:
        pass
def RemovertelaUsarios(frame): 
    try:   
        frame.pack_forget()
    finally:
        pass

def parametrosinicias(frame):
    global list_user_frame,Scrollable,filtrar,verificarseleção,TreeviewUsuarios,bt_Excluir_user,bt_add_user,bt_exportar_user
    Scrollable = None
    #####################################  FUNÇÕES   #####################################################
        
    #FUNÇÃO PARA FILTRAR
    def filtrar(*args):
        nome = name_users_filter_entry.get() 
        email = Usuarioinfo[0].lower()
        tipo = Perfil_filter_entry.get()
        
        if tipo == "ADMINISTRADOR":
            tipo = "admin"
        if tipo == "USUARIOS" :
            tipo = "user"

        if tipo =="TODOS":
            tipo = None

        if tipo_usuario == 'user':
            ConsultaSQL = dbu.listarusuariosporemail(nome,tipo,email)
        else:
            ConsultaSQL = dbu.listarusuarios(nome,tipo)
        
        global Usariosfiltrados
        Usariosfiltrados = ConsultaSQL
        ordenar()
   
    #FUNÇÃO PARA ORDENAR 
    def ordenar(*args):
        global Usariosfiltrados

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
        
        DadosOrdenados = sorted(Usariosfiltrados, key=lambda x: x[Ordem_P], reverse=TipoOrdem_P)
        
        try:
            for item in TreeviewUsuarios.get_children():
                TreeviewUsuarios.delete(item)     
        except Exception :
            pass
        for result in DadosOrdenados:
            TreeviewUsuarios.insert("", 'end', values=result)



    ##################################### FIM FUNÇÕES   #####################################################

    #Frame FILTRO E LISTA 
    master_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)
    
    #Listagem de Usarios
    list_user_frame = ctk.CTkFrame(master=master_frame, width=900, height=480, fg_color=("#808080"))
    list_user_frame.grid(row=0, column=0, sticky="n")
    master_frame.grid_rowconfigure(0, weight=1)
    master_frame.grid_columnconfigure(0, weight=1)
    #Frame dos itens do filtro ----------------------------------------------------------------------
    filter_frame = ctk.CTkFrame(master=list_user_frame, width=900, height=100, fg_color=("#808080"))
    filter_frame.grid(row=0, column=0, sticky="nsew")
    
    
    #cliente Filter
    name_users_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    name_users_filter_frame.pack(side=LEFT)
    name_users_filter_lb = ctk.CTkLabel(master=name_users_filter_frame, text="Usuario",width=300)
    name_users_filter_lb.grid(row=1, column=0, padx=10, pady=(5, 5), sticky="nsew")
    name_users_filter_entry = ctk.CTkEntry(master=name_users_filter_frame)
    name_users_filter_entry.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="nsew")
    name_users_filter_entry.bind("<Return>",filtrar)


    
    Perfil_lista = [
        "TODOS","USUARIOS","ADMINISTRADOR"
    ]
    #Perfil Filter
    Perfil_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    Perfil_filter_frame.pack(side=LEFT)
    Perfil_filter_lb = ctk.CTkLabel(master=Perfil_filter_frame, text="Perfil",width=150)
    Perfil_filter_lb.grid(row=1, column=3, padx=10, pady=(5, 5), sticky="nsew")
    Perfil_filter_entry = ctk.CTkComboBox(master=Perfil_filter_frame,width=50,values=Perfil_lista,command=filtrar)
    Perfil_filter_entry.grid(row=2, column=3, padx=10, pady=(5, 5), sticky="nsew")
                            
    #Ordenar Por..(tipo de ordenação)  Filter
    ordbytype_lista = [
        "DATA DE CADASTRO","ALFABETICA"
    ]
    ordbytype_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbytype_filter_frame.pack(side=LEFT)
    ordbytype_filter_lb = ctk.CTkLabel(master=ordbytype_filter_frame, text="Ordenar por",width=140)
    ordbytype_filter_lb.grid(row=1, column=4, padx=10, pady=(5, 5), sticky="nsew")
    ordbytype_filter_entry = ctk.CTkComboBox(master=ordbytype_filter_frame,width=50,command=ordenar,values=ordbytype_lista)
    ordbytype_filter_entry.grid(row=2, column=4, padx=10, pady=(5, 5), sticky="nsew")
    
    ordbycresdec_lista = [
        "CRESCENTE","DECRESCENTE"
    ]
    #ordenar Por (Crescente e decrescente ) Filter
    ordbycresdec_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#808080"))
    ordbycresdec_filter_frame.pack(side=LEFT)
    ordbycresdec_filter_lb = ctk.CTkLabel(master=ordbycresdec_filter_frame, text="Ordenar por",width=140)
    ordbycresdec_filter_lb.grid(row=1, column=5, padx=10, pady=(5, 5), sticky="nsew")
    ordbycresdec_filter_entry = ctk.CTkComboBox(master=ordbycresdec_filter_frame,width=50,command=ordenar,values=ordbycresdec_lista)
    ordbycresdec_filter_entry.grid(row=2, column=5, padx=10, pady=(5, 5), sticky="nsew")
  
  
    #Listagem de Usarios-----------------------------------------------------------------------------

    def verificarseleção(*args):
        seleção = TreeviewUsuarios.selection()

        if seleção:
            email = Usuarioinfo[0].lower()
            emailTree = TreeviewUsuarios.item(seleção[0])['values']
            emailTree= emailTree[2].lower()
            if emailTree:
                valor = bt_Editar_user.cget("state")  # Obtém o estado atual do botão
                if valor == "disabled":   
                    bt_Editar_user.configure(state='normal') 
                    #bt_Excluir_user.configure(state='normal') 

        else:

            bt_Editar_user.configure(state='disabled') 
            #bt_Excluir_user.configure(state='disabled') 
           
    

    TreeviewUsuarios = ttk.Treeview(list_user_frame, columns=("#","Nome","Email","Data_Cadastro","Perfil"), show='headings')
    TreeviewUsuarios.grid(row=1, column=0, sticky="nsew")
    TreeviewUsuarios.bind('<<TreeviewSelect>>',verificarseleção)
    
    # Define o as colunas
    TreeviewUsuarios.heading("#", text="ID")
    TreeviewUsuarios.heading("Nome", text="Nome")
    TreeviewUsuarios.heading("Email", text="Email")
    TreeviewUsuarios.heading("Data_Cadastro", text="Data Cadastro")
    TreeviewUsuarios.heading("Perfil", text="Perfil")
    #TreeviewUsuarios.heading("Opções", text="Opções")
    
    # Define o tamanho das colunas em pixels
    TreeviewUsuarios.column("#", width=50)  # ID
    TreeviewUsuarios.column("Nome", width=200)  # Nome
    TreeviewUsuarios.column("Email", width=250)  # Email
    TreeviewUsuarios.column("Data_Cadastro", width=100)  # Data cadastro
    TreeviewUsuarios.column("Perfil", width=80)  # perfil
    #TreeviewUsuarios.column("Opções", width=100, stretch=False)  # Opções 
   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(list_user_frame, command=TreeviewUsuarios.yview,height=500)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    TreeviewUsuarios.configure(yscrollcommand=scrollbar.set)
    
    #Frame dos botões de ação ----------------------------------------------------------------------
    bt_action_frame = ctk.CTkFrame(master=list_user_frame, fg_color=("#808080"))
    bt_action_frame.grid(row=2, column=0, sticky="nsew")
    
    


    Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel =Imagens_DataBase.baixarimagemPgclientes()  

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add_user = ctk.CTkButton(master=bt_action_frame,image=logo_add, text="Adicionair Usuario",command=lambda: Func_users.AdicionarUsuario(master_frame))
    bt_add_user.grid(row=0, column=0,  padx=5, pady=5,sticky="nsew")

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_user = ctk.CTkButton(master=bt_action_frame,image=logo_editar, text="Editar",command=lambda: Func_users.editar_Usuario(TreeviewUsuarios,master_frame))
    bt_Editar_user.grid(row=0, column=2,   padx=5, pady=5,sticky="nsew")
    
    #logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    #bt_Excluir_user = ctk.CTkButton(master=bt_action_frame,image=logo_excluir, text="Excluir Cliente",command=lambda: Func_users.excluir_cliente(TreeviewUsuarios))
    #bt_Excluir_user.grid(row=0, column=3,   padx=5, pady=5,sticky="nsew")

    logo_excel = PhotoImage(file=Caminho_Logo_Excel).subsample(30, 30)
    bt_exportar_user = ctk.CTkButton(master=bt_action_frame, image=logo_excel,text="Exportar Usarios",command='')
    #bt_exportar_user.grid(row=0, column=5,  padx=5, pady=5,sticky="nsew")

    bt_Editar_user.configure(state='disabled') 
    #bt_Excluir_user.configure(state='disabled') 


    