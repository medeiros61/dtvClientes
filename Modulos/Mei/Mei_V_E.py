import customtkinter as ctk
from tkinter import *
import Modulos.imagens.ImagensClientes as Imagens_DataBase
import Modulos.Mei.Botoes_Edicao as bts
import Modulos.Database.Logs as log
from tkinter import messagebox
import threading
import PainelDatavix as pd

Evento_TelaVoltar = f'Usuario saiu da Edição de de MEIS'
obs_TelaVoltar=""

def definiçãotipodeentrada(tipo):
    global tpEntrada
    tpEntrada = tipo

def criartelaEdit_MEI(frame,cliente):
    print('f')

def RemovertelaEdit_MEI(): 
    frameprincipal.pack_forget()
    framepai.pack(side=RIGHT, fill = BOTH,expand=True)

    log.RegistrarEventosdeLOG(Evento_TelaVoltar,obs_TelaVoltar) 

def SalvarDados(*args):
    resposta = messagebox.askquestion("Confirmação", "Deseja realmente salvar os dados?")
    if resposta == 'yes':
        def enviodados(): 

            botões = pd.PegarBotõesPainel()
            for bt in botões:
                bt.configure(state='disabled')

            frameprincipal.pack_forget()

            framepai.configure(cursor="watch")

            bts.pegar_dados_para_envio(tpEntrada)

            for bt in botões:
                bt.configure(state='normal') 

            RemovertelaEdit_MEI()

            framepai.configure(cursor="")
            

        EnvioDados = threading.Thread(target=enviodados)
        EnvioDados.start()

def parametrosinicias(frame,Frame_atual):
    global framepai, frameprincipal
    framepai = Frame_atual
    frameprincipal = frame
    #Frame 
    master_frame = ctk.CTkFrame(master=frameprincipal, width=1040, height=580, fg_color=("#808080"))
    master_frame.pack(side=TOP, fill = X)
    
  
    #criar botão açoes
    Frametitulo = ctk.CTkFrame(master_frame)
    Frametitulo.pack(side=TOP, fill = X)

    #criar botão açoes
    FrameDados = ctk.CTkFrame(Frametitulo,height=40,width=1000)
    FrameDados.pack(side=LEFT, fill = X)
    #FrameDados.grid(row=0,rowspan=2, column=0,columnspan=5, padx=(5, 0), pady=(1, 0), sticky="nsew")

    bt_voltar = ctk.CTkButton(FrameDados,text='<',command=RemovertelaEdit_MEI,width=40,height=40)
    bt_voltar.grid(row=0,rowspan=2,pady=1,padx=1, column=0, sticky="ns")


    id = ctk.CTkLabel(FrameDados, text="")
    id.grid(row=0, column=1, padx=10, sticky="nsew")

    Tipo = ctk.CTkLabel(FrameDados, text="")
    Tipo.grid(row=0, column=2, padx=10, sticky="nsew")
    
    Contratante = ctk.CTkLabel(FrameDados, text="")
    Contratante.grid(row=1, column=1, padx=10, sticky="w")

    DadosCliente = Contratante,id,Tipo

    #
    FrameBotões = ctk.CTkFrame(Frametitulo)
    FrameBotões.pack(side=RIGHT, fill = X)
    #FrameBotões.grid(row=0,rowspan=2,pady=1,padx=1, column=9, sticky="ns")

    bt_salvar = ctk.CTkButton(FrameBotões,text='Salvar',command=SalvarDados,height=20,width=200)
    bt_salvar.grid(row=0, column=5, padx=(5, 0), pady=(1, 10), sticky="nsew")
    #bt_salvar.pack(side=TOP, fill = X)

    bt_cancelar = ctk.CTkButton(FrameBotões,text='Cancelar',command=RemovertelaEdit_MEI,height=20,width=200)
    bt_cancelar.grid(row=1, column=5, padx=(5, 0), pady=(0, 1), sticky="nsew")
    #bt_cancelar.pack(side=TOP, fill = X)


    
    # criar tabview
    tabview = ctk.CTkTabview(master_frame,width=940, height=540)
    #tabview.grid(row=4, column=0,columnspan=6, padx=5, pady=5, sticky="nsew")
    tabview.pack(side=TOP, fill = BOTH)

    tabview.add("Empresa")
    tabview.tab("Empresa").grid_columnconfigure(0, weight=1) 
    
    tabview.add("Contrato de Parceria")
    tabview.tab("Contrato de Parceria").grid_columnconfigure(0, weight=1)  

    tabview.add("DASN")
    tabview.tab("DASN").grid_columnconfigure(0, weight=1)   
    
    tabview.add("Outras Informações")
    tabview.tab("Outras Informações").grid_columnconfigure(0, weight=1)   
     
    Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel =Imagens_DataBase.baixarimagemPgclientes()  
    
    bts.criarbotoes(tabview,DadosCliente,Caminho_Logo_Edit,Caminho_Logo_Add,Caminho_Logo_Rem)
    