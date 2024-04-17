import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
from ttkthemes import ThemedStyle

def criartelauser(frame):
    frame.pack(side=RIGHT, fill = BOTH,expand=True)

def Removertelauser(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    frame_top_user = ctk.CTkFrame(master=frame, width=900, height=100, fg_color=("#808080"))
    frame_top_user.pack(side=TOP, fill = X)
    #--------------------------------------------
    list_users = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#F7F9F9"))
    list_users.pack(side=TOP, fill = X)

    global TreeviewUsuarios
    
    EstilodeTela = ThemedStyle(list_users)
    EstilodeTela.set_theme("scidsand")
    TreeviewUsuarios = ttk.Treeview(list_users, columns=("#","Nome","Email","Data_Cadastro","Perfil"), show='headings')
    TreeviewUsuarios.grid(row=1, column=0, sticky="nsew")
    TreeviewUsuarios.bind('<<TreeviewSelect>>')
    
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
    #TreeviewClientes.column("Opções", width=100, stretch=False)  # Opções 
   
    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(list_users, command=TreeviewUsuarios.yview,height=500)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    TreeviewUsuarios.configure(yscrollcommand=scrollbar.set)
    
    #Frame dos botões de ação ----------------------------------------------------------------------
    bt_action_frame = ctk.CTkFrame(master=list_users, fg_color=("#808080"))
    bt_action_frame.grid(row=2, column=0, sticky="ne")