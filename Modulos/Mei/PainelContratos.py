
import customtkinter as ctk
from tkinter import ttk
import Modulos.ContratoParceria.EnvioContrato as Selenium
import Modulos.Mei.Botoes_Edicao as Bt_edit
import PainelDatavix as pd

def abrircontrato():
    pass

def incluir_dados_viewDG(itens):
    TreeViewDG_Contrato.insert("", 'end', values=itens)
    
def criarinterface():
    global TreeViewDG_Contrato
    OptionFrame = pd.option_frm()

    FrameContratos = ctk.CTkFrame(OptionFrame)
    FrameContratos.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="nsew")

    TreeViewDG_Contrato = ttk.Treeview(FrameContratos, columns=("Empresa","Status"), show='headings',height=5)
    TreeViewDG_Contrato.grid(row=2, column=0,columnspan=3, sticky="new", padx=(5,0), pady=(5,10))
    TreeViewDG_Contrato.bind('<Double-1>',abrircontrato)
        # Define o as colunas
    TreeViewDG_Contrato.heading("Empresa", text="Empresa")
    TreeViewDG_Contrato.heading("Status", text="Status")


    # Define o tamanho das colunas em pixels
    TreeViewDG_Contrato.column("Empresa", width=80)  # 
    TreeViewDG_Contrato.column("Status", width=60)  # 
    

    # Adicionar barra de rolagem vertical ao Treeview
    scrollbarParceiras = ctk.CTkScrollbar(FrameContratos, command=TreeViewDG_Contrato.yview,height=20)
    scrollbarParceiras.grid(row=2, column=4, padx=(0,0), pady=(5,10), sticky="nsew")
    TreeViewDG_Contrato.configure(yscrollcommand=scrollbarParceiras.set)    




def digitação_contrato():
    
    Lista = Bt_edit.pegar_dados_Contrato()
    for contrato in Lista :
        dados = contrato[2]  
        nome = dados[1]
        Lista = Bt_edit.pegar_dados_Contrato()
        Selenium.enviarcontrato(contrato)
        Bt_edit.Deletar_Primeiro_Contrato()