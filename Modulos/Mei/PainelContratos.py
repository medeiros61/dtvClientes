
import customtkinter as ctk
from tkinter import ttk
import Modulos.ContratoParceria.EnvioContrato as Selenium
import Modulos.Mei.Botoes_Edicao as Bt_edit
import PainelDatavix as pd
import threading

execuçao = 0
def incluir_dados_viewDG(itens):
    global execuçao
    TreeViewDG_Contrato.insert("", 'end', values=itens)
    if execuçao == 0:
        FrameContratos.grid(row=9, column=0, padx=2, pady=(20, 10), sticky="nsew") 
        execuçao += 1 
         
def criarinterface():
    global TreeViewDG_Contrato,FrameContratos
    OptionFrame = pd.option_frm()

    FrameContratos = ctk.CTkFrame(OptionFrame)
    

    NomeLB = ctk.CTkLabel(FrameContratos,text='Contratos')
    NomeLB.grid(row=1, column=0,columnspan=5, sticky="new", padx=(0,0), pady=(2,2))
    
    TreeViewDG_Contrato = ttk.Treeview(FrameContratos, columns=("Empresa","Status"), show='headings',height=5)
    TreeViewDG_Contrato.grid(row=2, column=0,columnspan=3, sticky="new", padx=(5,0), pady=(5,10))
    TreeViewDG_Contrato.bind('<Double-1>',abrir_link)
        # Define o as colunas
    TreeViewDG_Contrato.heading("Empresa", text="Empresa")
    TreeViewDG_Contrato.heading("Status", text="Status")


    # Define o tamanho das colunas em pixels
    TreeViewDG_Contrato.column("Empresa", width=100)  # 
    TreeViewDG_Contrato.column("Status", width=60)  # 
    

    # Adicionar barra de rolagem vertical ao Treeview
    scrollbarParceiras = ctk.CTkScrollbar(FrameContratos, command=TreeViewDG_Contrato.yview,height=20)
    scrollbarParceiras.grid(row=2, column=4, padx=(0,0), pady=(5,10), sticky="nsew")
    TreeViewDG_Contrato.configure(yscrollcommand=scrollbarParceiras.set)    

def abrir_link(event):
    item = TreeViewDG_Contrato.selection()
    if item:
        item_values = TreeViewDG_Contrato.item(item, 'values')
        status = item_values[1]
        if status == 'Concluído':    
            link = item_values[0].split("link: ")[-1]  # Extrai o link do valor do item
            thread1 = threading.Thread(target=lambda: Selenium.abrircontrato(link))
            thread1.start()

def atualizar_treeview(treeview, id, link):
    for item in treeview.get_children():
        item_values = treeview.item(item, 'values')
        empresa = item_values[0]
        status = item_values[1]

        if f"ID:{id}" in empresa:
            novo_nome = f"{empresa} link: {link}"
            novo_status = "Concluído"
            treeview.item(item, values=(novo_nome, novo_status))
            print(f"concluido - {novo_nome}")
            break


def digitação_contrato():
    
 
    erroscont = 0    
    Itens = Bt_edit.pegar_dados_Contrato()
    while len(Itens)>0:
            contrato,id = Itens[0] 
            
            dados = contrato[2]  
            nome = dados[1]        
            try:
                Link = Selenium.enviarcontrato(contrato)
                Bt_edit.Deletar_Primeiro_Contrato()
                atualizar_treeview(TreeViewDG_Contrato, id, Link)
                erroscont = 0
            except Exception:
                if erroscont > 4:
                    break
                erroscont += 1
                print("Erro ao enviar contrato")
                pass
            
            Itens = Bt_edit.pegar_dados_Contrato()