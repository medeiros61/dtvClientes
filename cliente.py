import customtkinter as ctk
from tkinter import *
import Database.Clients as dbc

def criartelaclientes(frame):
    global Scrollable,list_clients_frame

    frame.pack(side=RIGHT, fill = BOTH,expand=True)
    cont = 0

    if Scrollable is not None:
        Scrollable.destroy() 
        Scrollable.pack_forget()
        # Remove all widgets inside Scrollable

    Scrollable = ctk.CTkScrollableFrame(master=list_clients_frame, height=300,label_text="Lista de Empresas")
    Scrollable.pack(fill=X,pady = 20)
   

    clientes_data = dbc.getclientlist_complete()
    x = ctk.CTkFrame(Scrollable,width=800)
    x.pack(fill=X)
   
    ctk.CTkLabel(x,text=f"#").grid(row=0, column=0, padx=30, pady=(20, 10), sticky="nsew")
    ctk.CTkLabel(x,text=f"Nome").grid(row=0, column=1, padx=15, pady=(20, 10), sticky="nsew")     
    ctk.CTkLabel(x,text=f"UF").grid(row=0, column=2, padx=15, pady=(20, 10), sticky="ew")
    ctk.CTkLabel(x,text=f"Município").grid(row=0, column=3, padx=40, pady=(20, 10), sticky="nsew")
    ctk.CTkLabel(x,text=f"Status").grid(row=0, column=4, padx=40, pady=(20, 10), sticky="nsew")
    ctk.CTkLabel(x,text=f"Opções").grid(row=0, column=5, padx=40, pady=(20, 10), sticky="nsew")
   
    for result in clientes_data:
        if cont < 10:
            linha = cont +1
            id,nome_empresa,uf,municipio,ativo = result
            nome_empresa = nome_empresa.strip()
            if ativo == 1:
                ativo = 'ATIVO'
            else:
                ativo = 'INATIVO'    
            #print(result)
            
            ctk.CTkLabel(x,text=f"{id}").grid(row=linha, column=0, padx=3, pady=(20, 10), sticky="nsew")
            if len(nome_empresa) < 30:
                ctk.CTkLabel(x,text=f"{nome_empresa}").grid(row=linha, column=1, padx=3, pady=(20, 10), sticky="nsew")
            else:
                corte = nome_empresa.find(' ', 30)
                if corte >0 :
                    poscorte = corte +1 
                    nome_empresa = nome_empresa[0:corte] +"\n"+ nome_empresa[poscorte:]
                ctk.CTkLabel(x,text=f"{nome_empresa}").grid(row=linha, column=1, padx=3, pady=(20, 10), sticky="nsew")

            
            ctk.CTkLabel(x,text=f"{uf}").grid(row=linha, column=2, padx=3, pady=(20, 10), sticky="ew")
            ctk.CTkLabel(x,text=f"{municipio}").grid(row=linha, column=3, padx=3, pady=(20, 10), sticky="nsew")
            ctk.CTkLabel(x,text=f"{ativo}").grid(row=linha, column=4, padx=3, pady=(20, 10), sticky="nsew")
            y = ctk.CTkFrame(x)
            y.grid(row=linha, column=5, padx=3, pady=(20, 10), sticky="nsew")
            ctk.CTkButton(y,text='editar',height=5 ,width=5).pack(pady=3,padx=3,side=LEFT)
            ctk.CTkButton(y,text='excluir',height=5 ,width=5).pack(pady=3,padx=3,side=RIGHT)
            ctk.CTkButton(y,text='comentar',height=5 ,width=5).pack(pady=3,padx=3,side=RIGHT)
            cont = cont + 1
        if cont > 10:
            break


def Removertelaclientes(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    global list_clients_frame,Scrollable
    Scrollable = None


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

 
  



