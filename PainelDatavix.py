import customtkinter as ctk
from tkinter import *
import Modulos.Cliente.Cliente as cl
import Modulos.Mei.Mei as me
import Modulos.Usuarios.usuarios as user
import Modulos.imagens.ImagensClientes as Imagens_DataBase
import threading
import Modulos.Database.Logs as log
import warnings
import time
# Desativar todos os warnings
warnings.simplefilter("ignore")

#mensagens

Evento_Logar= 'Usuario Logou no sistema'
obs_Logar = ""
 
Evento_PainelDtv= 'Ativou Modulo Painel Datavix'
obs_PainelDtv = ""

Evento_AtivarMEI= 'Ativou Tela de MEI'
obs_AtivarMEI = ""

Evento_AtivarClientes= 'Ativou Tela de Clientes'
obs_AtivarClientes = ""

Evento_AtivarUsuarios= 'Ativou Tela de Usarios'
obs_AtivarUsuarios = ""

obs_Sair = ""
Evento_Sair= 'Usuario Deslogou do sistema'

def DataVix(DadosUsuario,janela):
    log.dadosusuario(DadosUsuario)
    log.activites("Entrar")
    log.AtivarRegistrodeLog()
    log.RegistrarEventosdeLOG(Evento_Logar,obs_Logar) 
    

    def ativarmei():
        cl.Removertelaclientes(frame_clientes)
        user.RemovertelaUsarios(frame_user)
        me.criartelaMEI(frame_mei,UserRole)
      
        log.RegistrarEventosdeLOG(Evento_AtivarMEI,obs_AtivarMEI) 
        
    def ativarclientes():
        me.RemovertelaMEI(frame_mei)
        user.RemovertelaUsarios(frame_user)
        cl.criartelaclientes(frame_clientes,UserRole)
      
        log.RegistrarEventosdeLOG(Evento_AtivarClientes,obs_AtivarClientes) 

    def ativaruser():
        me.RemovertelaMEI(frame_mei)
        cl.Removertelaclientes(frame_clientes)
        user.criartelaUsarios(frame_user,UserRole)
     
        log.RegistrarEventosdeLOG(Evento_AtivarUsuarios,obs_AtivarUsuarios) 
        
    def exit():
        screen_datavix.quit()
        screen_datavix.destroy()   
    
        log.RegistrarEventosdeLOG(Evento_Sair,obs_Sair) 
        log.activites("Sair") 
    
    def fecharjanela_anterior():
        #janela.wm_iconify()
        time.sleep(0.5)
        janela.quit()
        try: 
            janela.destroy()
        except Exception:
            pass

    def center_window(window, width, height):
        # Obter as dimensões da tela
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Calcular as coordenadas para posicionar a janela no centro
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Definir as coordenadas da janela
        window.geometry(f"{width}x{height}+{x}+{y}") 
    def on_close():
        log.activites("Sair") 
        screen_datavix.quit()
        screen_datavix.destroy() 
        log.RegistrarEventosdeLOG(Evento_Sair,obs_Sair) 
      
    Username = DadosUsuario[3]
    UserRole = DadosUsuario
    caminho = Imagens_DataBase.baixarimagemLogoDTV()
    

    screen_datavix = ctk.CTk()
    screen_datavix.protocol("WM_DELETE_WINDOW", on_close)
    screen_datavix.geometry(f"{1150}x{615}+{0}+{0}") 
    #center_window(screen_datavix,1150,615) caso queria que aparece no centro

    
    screen_datavix.title("Master")
    screen_datavix.resizable(False,False)
    #username_entry = ctk.CTkEntry(master=screen_datavix, placeholder_text="TESTE", width=300, font=("Roboto",14))
    #username_entry.pack(side=RIGHT)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    #definindo frame cliente------------------------------
    frame_clientes = ctk.CTkFrame(master=screen_datavix, width=900, height=580, fg_color=("#808080"))
    
    cl.parametrosinicias(frame_clientes)
    #------------------------------------------------------
    #frame usuarios
    frame_user = ctk.CTkFrame(master=screen_datavix, width=900, height=580, fg_color=("#808080"))
    user.parametrosinicias(frame_user) 
    #---------------------------------------------------------- frame mei
    frame_mei = ctk.CTkFrame(master=screen_datavix, width=900, height=580, fg_color=("#808080"))
    me.parametrosinicias(frame_mei)  
    #------------------------------------------------------------------------

    #aba
    options_frame = ctk.CTkFrame(master=screen_datavix, width=200, height=580, fg_color=("#808080"))
    options_frame.pack(side=LEFT, fill = Y) 
    #options_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
    #options_frame.pack_propagate(False)
    #logo datavix
    
    logo_datavix = PhotoImage(file=caminho).subsample(3, 3)
    botao_logo = ctk.CTkButton(master=options_frame, image=logo_datavix, text="", fg_color="#808080")
    botao_logo.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")
    botao_logo.configure(state="disabled")
    
    Lebel_bemvindo = ctk.CTkLabel(master=options_frame, text=f'Bem vindo {Username} !', font=("Roboto",15))
    Lebel_bemvindo.grid(row=3, column=0, pady=5, padx=10, sticky="nsew")
    #buttons
    botao_dashboard = ctk.CTkButton(master=options_frame, text="DASHBOARD")
    botao_dashboard.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="nsew")

    botao_clientes = ctk.CTkButton(master=options_frame, text="CLIENTES",command=ativarclientes)
    botao_clientes.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="nsew")
    botao_clientes.configure(state="normal")

    botao_MEI = ctk.CTkButton(master=options_frame, text="CONTROLE MEis", command=ativarmei)
    botao_MEI.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="nsew")

    botao_usuarios = ctk.CTkButton(master=options_frame, text="USUARIOS", command=ativaruser)
    botao_usuarios.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="nsew")
    
  

    botao_sair = ctk.CTkButton(master=options_frame, text="SAIR", command=exit)
    botao_sair.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="nsew")
    
   
    
    Treadfecharjanela = threading.Thread(target=fecharjanela_anterior)
    #inicia a contagem para fechar tela de carregamento
    Treadfecharjanela.start()
    
    # Ativar todos os warnings
    warnings.simplefilter("default")

    log.RegistrarEventosdeLOG(Evento_PainelDtv,obs_PainelDtv)

    screen_datavix.mainloop()

#---------------------------------------------------------------------------------#

