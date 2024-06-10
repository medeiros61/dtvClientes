import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
import Modulos.Database.Clients as dbc
import Modulos.Cliente.Func_cliente as Func_cli
import Modulos.imagens.ImagensClientes as Imagens_DataBase
import Modulos.Cliente.Cliente_V_E as Tela_Edit_C 
from datetime import date,datetime

cor_de_borda = "gray50"
largura_borda = 2


def criartelaclientes(frame,DadosUsuario):
    try:
        global Scrollable,list_clients_frame,TreeviewClientes,tipo_usuario,informacoes_usuario
        informacoes_usuario = DadosUsuario
        tipo_usuario= DadosUsuario[2]
        if tipo_usuario == 'user':
            bt_Excluir_clients.grid_remove()
        
        
        
        filtrar()
        verificarseleção()
        Tela_Edit_C.RemovertelaEdit_clientes()
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
    except Exception:
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
    def exportar(*args):
        Func_cli.Exportar_clientes(clinte_filter_entry.get(),uf_filter_entry.get(),Status_filter_entry.get())
        
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


    def verificarseleção(*args):
        seleção = TreeviewClientes.selection()
        PuxardadosCometarios()
        if seleção:
            valor = bt_Editar_clients.cget("state")  # Obtém o estado atual do botão
            if valor == "disabled":   
                bt_Editar_clients.configure(state='normal') 
                bt_Excluir_clients.configure(state='normal') 
                #bt_Comentar_clients.configure(state='normal') 
        else:
            
            bt_Editar_clients.configure(state='disabled') 
            bt_Excluir_clients.configure(state='disabled') 
            #bt_Comentar_clients.configure(state='disabled')
    def editarcliete(*args):
        Func_cli.editar_cliente(TreeviewClientes,Dadosparateladeedição)
        
    def PuxardadosCometarios():
        selecao = TreeviewClientes.selection()
        # Verifica se há algum item selecionado
        if selecao and SW_Comentar_clients.get() ==1:
            # Obtém as informações do item selecionado
            valores = TreeviewClientes.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do cliente
                id = valores[0]
                global nome_cliente_historico
                nome_cliente_historico = valores[1]
                if len(nome_cliente_historico) > 48:
                    nome_cliente_historico = nome_cliente_historico[0:48]+"..."

                   #nome_cliente_historico = nome_cliente_historico[0:50]+"\n"+nome_cliente_historico[51:] 

                usuario = informacoes_usuario[3]
                label_text = lbNomeEmpresa.cget("text")

                if nome_cliente_historico in label_text:
                    pass
                else:
                    lbNomeEmpresa.configure(text=f"Nome Empresa: {nome_cliente_historico}")
                    
                    lbUsuario.configure(text=f"Usuario: {usuario}")
                    Comentarios = dbc.getclientComents(id)
                    try:
                        for item in TreeViewHistorico.get_children():
                                TreeViewHistorico.delete(item)     
                    except Exception :
                            pass
                    for item in Comentarios:
                        TreeViewHistorico.insert("", 'end', values=item)

     
    def Abrircomentarios(*args):
        
        ComentarioCompleto = ctk.CTkToplevel(FrameComentarios)
 
        selecao = TreeViewHistorico.selection()
        # Verifica se há algum item selecionado
        if selecao :
            # Obtém as informações do item selecionado
            valores = TreeViewHistorico.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                data = valores[0]
                Mensagem = valores[1]
                Usuario = valores[2]
                ComentarioCompleto.title(f"{nome_cliente_historico}")

                DataLB = ctk.CTkLabel(ComentarioCompleto,text=f'Data: {data}')
                DataLB.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=5, sticky="w")
           

                UsuarioLB = ctk.CTkLabel(ComentarioCompleto,text=f'Usuario: {Usuario}')
                UsuarioLB.grid(row = 1, column = 0, columnspan = 2, padx=10, pady=5, sticky="w")
              

                MensagemLB = ctk.CTkLabel(ComentarioCompleto,text='Mensagem')
                MensagemLB.grid(row = 2, column = 0, padx=10, pady=5,columnspan=2, sticky="nsew")
                MensagemLB_inf = ctk.CTkTextbox(ComentarioCompleto,width=300)
                MensagemLB_inf.insert("1.0", Mensagem)
                MensagemLB_inf.grid(row = 3, column = 0,columnspan=2, padx=10, pady=5,sticky="nsew")
                MensagemLB_inf.configure(state='disabled')
                ComentarioCompleto.resizable(False,False)

    def ativarcomentarios():
        if SW_Comentar_clients.get() ==1:
            TreeviewClientes.grid_remove()
            TreeviewClientes.column("Nome", width=250)  # Nome
            TreeviewClientes.column("UF", width=50)  # UF
            TreeviewClientes.column("Município", width=50)  # Município
            TreeviewClientes.column("Status", width=50)# Status
            TreeviewClientes.grid(row=1, column=0, sticky="nsew")
            FrameComentarios.grid(row=1, column=2, sticky="nsew")
        else:
            FrameComentarios.grid_remove()
            TreeviewClientes.grid_remove()
            TreeviewClientes.column("Nome", width=500)  # Nome
            TreeviewClientes.column("UF", width=50)  # UF
            TreeviewClientes.column("Município", width=100)  # Município
            TreeviewClientes.column("Status", width=80)  # Status
            TreeviewClientes.grid(row=1, column=0, sticky="nsew")
    def salvarcomentarios():
        agora = datetime.now()
        agora = agora.strftime("%Y-%m-%d %H:%M:%S")
        EmailUsuario = informacoes_usuario[0] 
        IDCliente = TreeviewClientes.item(TreeviewClientes.selection()[0])['values'][0]
        Mensagem = etMensagem.get("1.0", "end-1c")
        dbc.RegisterclientComents(IDCliente,Mensagem,EmailUsuario,agora)
        item = agora,Mensagem,informacoes_usuario[3] 
        TreeViewHistorico.insert("", 'end', values=item)
        Func_cli.comentar_cliente(TreeviewClientes)
        etMensagem.delete("1.0", "end-1c")

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
    list_clients_frame.grid(row=0, column=0, sticky="n")
    master_frame.grid_rowconfigure(0, weight=1)
    master_frame.grid_columnconfigure(0, weight=1)
    
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

    
    
    FrametreewView = ctk.CTkFrame(list_clients_frame, fg_color=("#808080"))
    FrametreewView.grid(row=1, column=0,columnspan=2, sticky="n")

    ###Comentarios (Ativado no switch)
   

    FrameComentarios = ctk.CTkFrame(FrametreewView, width=450, fg_color=("#808080"))
    #FrameComentarios.grid(row=1, column=2, sticky="nsew")

    FrameRegistro = ctk.CTkFrame(FrameComentarios, border_width=largura_borda, border_color=cor_de_borda)
    FrameRegistro.grid(row=1, column=0, sticky="n")

    
    lbNomeEmpresa = ctk.CTkLabel(FrameRegistro,text='Nome Empresa:')
    lbNomeEmpresa.grid(row=1, column=0, padx=10,columnspan=2, pady=(5,1), sticky="w")

    
    lbUsuario = ctk.CTkLabel(FrameRegistro,text='Usuario:')
    lbUsuario.grid(row=2, column=0, padx=10,columnspan=2, pady=(0,5), sticky="w")


    lbMensagem = ctk.CTkLabel(FrameRegistro,text='Mensagem:')
    lbMensagem.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
    
    etMensagem = ctk.CTkTextbox(FrameRegistro,height=100,width=450)
    etMensagem.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    btsalvar = ctk.CTkButton(FrameRegistro,text='Adicionar Comentario',command=salvarcomentarios)
    btsalvar.grid(row=5, column=0, columnspan=2, padx=10, pady=(5,10), sticky="nsew")

    FrameHistorico = ctk.CTkFrame(FrameComentarios, border_width=largura_borda, border_color=cor_de_borda)
    FrameHistorico.grid(row=2, column=0, sticky="nsew")

    lbHistorico = ctk.CTkLabel(FrameHistorico,text='Historico')
    lbHistorico.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    TreeViewHistorico = ttk.Treeview(FrameHistorico, columns=("Data","Mensagem","Usuario"), show='headings',height=8)#height é a quantidade de linhas
    TreeViewHistorico.grid(row=1, column=0, padx=(10,0), pady=5, sticky="nsew")
    TreeViewHistorico.bind('<<TreeviewSelect>>')
    TreeViewHistorico.bind('<Double-1>',Abrircomentarios)
    
    # Define o as colunas
    TreeViewHistorico.heading("Data", text="Data")
    TreeViewHistorico.heading("Mensagem", text="Mensagem")
    TreeViewHistorico.heading("Usuario", text="Usuario")

    
    # Define o tamanho das colunas em pixels
    TreeViewHistorico.column("Data", width=100)  
    TreeViewHistorico.column("Mensagem", width=250) 
    TreeViewHistorico.column("Usuario", width=80)  

    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(FrameHistorico, command=TreeViewHistorico.yview,height=10)
    scrollbar.grid(row=1, column=1, padx=(0,10), pady=5, sticky="nsew")
    TreeViewHistorico.configure(yscrollcommand=scrollbar.set)


    ## Fim da configuração dos comentarios 



    TreeviewClientes = ttk.Treeview(FrametreewView, columns=("#","Nome","UF","Município","Status"), show='headings',height=23)
    TreeviewClientes.grid(row=1, column=0, sticky="nsew")
    TreeviewClientes.bind('<<TreeviewSelect>>', verificarseleção)
    TreeviewClientes.bind('<Double-1>',editarcliete)
    
    # Define o as colunas
    TreeviewClientes.heading("#", text="ID")
    TreeviewClientes.heading("Nome", text="Nome")
    TreeviewClientes.heading("UF", text="UF")
    TreeviewClientes.heading("Município", text="Município")
    TreeviewClientes.heading("Status", text="Status")
    #TreeviewClientes.heading("Opções", text="Opções")
    
    # Define o tamanho das colunas em pixels
    TreeviewClientes.column("#", width=50)  # ID
    TreeviewClientes.column("Nome", width=500)  # Nome
    TreeviewClientes.column("UF", width=50)  # UF
    TreeviewClientes.column("Município", width=100)  # Município
    TreeviewClientes.column("Status", width=80)  # Status
    #TreeviewClientes.column("Opções", width=100, stretch=False)  # Opções 
    
   

    # Adicionar barra de rolagem vertical ao Treeview
    scrollbar = ctk.CTkScrollbar(FrametreewView, command=TreeviewClientes.yview,height=500)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    TreeviewClientes.configure(yscrollcommand=scrollbar.set)
    
    #Frame dos botões de ação ----------------------------------------------------------------------
    bt_action_frame = ctk.CTkFrame(master=list_clients_frame, fg_color=("#808080"))
    bt_action_frame.grid(row=2, column=0, sticky="nsew")
    
    


    Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel =Imagens_DataBase.baixarimagemPgclientes()  

    logo_add = PhotoImage(file=Caminho_Logo_Add).subsample(25, 25)
    bt_add_clients = ctk.CTkButton(master=bt_action_frame,image=logo_add, text="Adicionar Cliente",command=lambda: Func_cli.Adicionar_cliente(Dadosparateladeedição))
    bt_add_clients.grid(row=0, column=0,  padx=5, pady=5,sticky="nsew")

    logo_editar = PhotoImage(file=Caminho_Logo_Edit).subsample(25, 25)
    bt_Editar_clients = ctk.CTkButton(master=bt_action_frame,image=logo_editar, text="Editar",command=lambda: Func_cli.editar_cliente(TreeviewClientes,Dadosparateladeedição))
    bt_Editar_clients.grid(row=0, column=2,   padx=5, pady=5,sticky="nsew")
    
    logo_excluir = PhotoImage(file=Caminho_Logo_Rem).subsample(25, 25)
    bt_Excluir_clients = ctk.CTkButton(master=bt_action_frame,image=logo_excluir, text="Excluir Cliente",command=lambda: Func_cli.excluir_cliente(TreeviewClientes))
    #bt_Excluir_clients.grid(row=0, column=3,   padx=5, pady=5,sticky="nsew")

    logo_comentar = PhotoImage(file=Caminho_Logo_Comt).subsample(25, 25)
   


    SW_Comentar_clients = ctk.CTkSwitch(master=bt_action_frame, text="Comentarios",command=ativarcomentarios)

    SW_Comentar_clients.grid(row=0, column=9,  padx=5, pady=5,sticky="e")

    logo_excel = PhotoImage(file=Caminho_Logo_Excel).subsample(30, 30)
   
    
    bt_exportar_clients = ctk.CTkButton(master=bt_action_frame, image=logo_excel,text="Exportar clientes",command=exportar)
    bt_exportar_clients.grid(row=0, column=5,  padx=5, pady=5,sticky="nsew")



