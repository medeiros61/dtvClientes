import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Modulos.Database.Clients as dbc
import Modulos.Cliente.Func_cliente as Func_cli
import Modulos.imagens.ImagensClientes as Imagens_DataBase
from ttkthemes import ThemedStyle
import Modulos.Cliente.Botões_Ediçao as bts

def criartelaEdit_clientes(frame,cliente):
    print('f')

def RemovertelaEdit_clientes(): 
    frameprincipal.pack_forget()
    framepai.pack(side=RIGHT, fill = BOTH,expand=True)

def parametrosinicias(frame,Frame_atual):
    global framepai, frameprincipal
    framepai = Frame_atual
    frameprincipal = frame
    #Frame 
    master_frame = ctk.CTkFrame(master=frameprincipal, width=900, height=580, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)
   
    #criar botão açoes
    
    bt_voltar = ctk.CTkButton(master_frame,text='< Voltar',command=RemovertelaEdit_clientes)
    bt_voltar.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
    
    bt_salvar = ctk.CTkButton(master_frame,text='Salvar',command='')
    bt_salvar.grid(row=0, column=4, padx=(20, 0), pady=(20, 0), sticky="nsew")
   
    bt_cancelar = ctk.CTkButton(master_frame,text='Cancelar',command=RemovertelaEdit_clientes)
    bt_cancelar.grid(row=0, column=5, padx=(20, 0), pady=(20, 0), sticky="nsew")


    
    # criar tabview
    tabview = ctk.CTkTabview(master_frame,width=800, height=540)
    tabview.grid(row=1, column=0,columnspan=6, padx=5, pady=5, sticky="nsew")
    
    tabview.add("Cliente")
    tabview.tab("Cliente").grid_columnconfigure(0, weight=1) 
    
    tabview.add("Gerais")
    tabview.tab("Gerais").grid_columnconfigure(0, weight=1)  

    tabview.add("Federais")
    tabview.tab("Federais").grid_columnconfigure(0, weight=1)   

    tabview.add("Estaduais")
    tabview.tab("Estaduais").grid_columnconfigure(0, weight=1)   
    
    tabview.add("Municipais")
    tabview.tab("Municipais").grid_columnconfigure(0, weight=1)   

    tabview.add("Societário")
    tabview.tab("Societário").grid_columnconfigure(0, weight=1)   

    tabview.add("Departamento pessoal")
    tabview.tab("Departamento pessoal").grid_columnconfigure(0, weight=1)   

    tabview.add("BPO")
    tabview.tab("BPO").grid_columnconfigure(0, weight=1)   
    
    bts.criarbotoes(tabview)
    