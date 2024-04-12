import customtkinter as ctk
from tkinter import *

def criartelaclientes(frame):
    frame.pack(side=RIGHT, fill = BOTH,expand=True)

def Removertelaclientes(frame): 
    frame.pack_forget()

def parametrosinicias(frame):

    #Frame FILTRO E LISTA
    master_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#807090"))
    master_frame.pack(side=TOP, fill = X)

    #Frame dos itens do filtro
    filter_frame = ctk.CTkFrame(master=master_frame, width=900, height=100, fg_color=("#801090"))
    filter_frame.pack(side=TOP, fill = X)
    
    #UF Filter
    uf_filter_frame = ctk.CTkFrame(master=filter_frame, height=100, fg_color=("#807090"))
    uf_filter_frame.pack(side=LEFT)
    uf_filter_lb = ctk.CTkLabel(master=uf_filter_frame, text="UF",width=50)
    uf_filter_lb.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="nsew")
    uf_filter_entry = ctk.CTkComboBox(master=uf_filter_frame,width=50)
    uf_filter_entry.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="nsew")

    #cliente Filter
    clinte_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#807090"))
    clinte_filter_frame.pack(side=LEFT)
    clinte_filter_lb = ctk.CTkLabel(master=clinte_filter_frame, text="Clientes",width=300)
    clinte_filter_lb.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="nsew")
    clinte_filter_entry = ctk.CTkEntry(master=clinte_filter_frame)
    clinte_filter_entry.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="nsew")
    
    #Por pagina Filter
    porpg_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#807090"))
    porpg_filter_frame.pack(side=LEFT)
    porpg_filter_lb = ctk.CTkLabel(master=porpg_filter_frame, text="Por Página",width=50)
    porpg_filter_lb.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="nsew")
    porpg_filter_entry = ctk.CTkComboBox(master=porpg_filter_frame,width=50)
    porpg_filter_entry.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="nsew")
    
    #Ordenar Por..(tipo de ordenação)  Filter
    ordbytype_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#807090"))
    ordbytype_filter_frame.pack(side=LEFT)
    ordbytype_filter_lb = ctk.CTkLabel(master=ordbytype_filter_frame, text="Ordenar por",width=50)
    ordbytype_filter_lb.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="nsew")
    ordbytype_filter_entry = ctk.CTkComboBox(master=ordbytype_filter_frame,width=50)
    ordbytype_filter_entry.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="nsew")
    
    #ordenar Por (Crescente e decrescente ) Filter
    ordbycresdec_filter_frame = ctk.CTkFrame(master=filter_frame,height=100, fg_color=("#807090"))
    ordbycresdec_filter_frame.pack(side=LEFT)
    ordbycresdec_filter_lb = ctk.CTkLabel(master=ordbycresdec_filter_frame, text="Ordenar por",width=50)
    ordbycresdec_filter_lb.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="nsew")
    ordbycresdec_filter_entry = ctk.CTkComboBox(master=ordbycresdec_filter_frame,width=50)
    ordbycresdec_filter_entry.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="nsew")

    #Listagem de clientes
    list_clients_frame = ctk.CTkFrame(master=master_frame, width=900, height=480, fg_color=("#809090"))
    list_clients_frame.pack(side=TOP, fill = X)


