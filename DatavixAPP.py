Versão = '1.1'

import customtkinter as ctk
from tkinter import *
import Modulos.Database.Users as dbu
import PainelDatavix as PD
import Modulos.imagens.ImagensClientes as Imagens_DataBase
import Modulos.Database.Parametros as bdp
import Modulos.Database.Email as f2aut
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import warnings
import os

import pyshortcuts
janela = ctk.CTk()

warnings.simplefilter("ignore")

podelogar = False
def fazer_atalho():

    def pegarcaminhodaappdata():
                    # Obter o diretório de dados do usuário (AppData/Roaming)
                    global appdata_roaming
                    appdata_roaming = os.getenv('APPDATA')
                    # Caminho completo para a pasta Datavix
                    datavix_path = os.path.join('C:\\', 'Datavix')
                    datavix_path = os.path.join(appdata_roaming, 'Datavix')
                    # Caminho para a pasta de imagens dentro de Datavix
                    imagens_path = os.path.join(datavix_path, 'App')
                    if not os.path.exists(imagens_path):
                            os.makedirs(imagens_path)
                    return imagens_path
    
    imagens_path = pegarcaminhodaappdata()
    caminho_exe = os.path.join(imagens_path, "DatavixAPP.exe")
    # Definir o caminho do executável e do ícone
    caminho_exe = rf"{caminho_exe}"
            
    atalho_path = os.path.join(appdata_roaming, r"\Roaming\Microsoft\Windows\Start Menu\Programs\Datavix App.lnk")
    
    icone = caminho_completo_imagem = os.path.join(imagens_path, "logodatavix.ico")
    pyshortcuts.make_shortcut(caminho_exe, atalho_path, icone)

fazer_atalho()

def TelaLogin():
    def Redefinirsenha():   
        def telacodigo():

            if entryemail.get() != '':
                temBD = dbu.VerificaçãoEmail_existe(entryemail.get())
                if temBD:
                    f2aut.EnviodoToken(entryemail.get())
                    
                def vericação_cod(): 
                    Verificação = f2aut.verificação(entryCod.get())
                    if Verificação :
                        telasenha() 
                        
                    else:
                        messagebox.showerror("Erro", "Código inválido. Por favor, tente novamente.")
                        entryCod.delete(0, END)

                def telasenha():    
                    def change_password():
                        new_password = new_password_entry.get()
                        confirm_password = confirm_password_entry.get()

                        if new_password == confirm_password:
                            # Update the password in the database
                            dbu.Alterasenha(entryemail.get(), new_password)
                            messagebox.showinfo("Sucesso", "Senha alterada com sucesso.")
                            JanelaSenha.destroy()
                        else:
                            messagebox.showerror("Erro", "As senhas não coincidem. Por favor, tente novamente.")


                    FramenovaSenha = ctk.CTkFrame(JanelaSenha)
                    FramenovaSenha.grid(row=0, column=0, padx=10,rowspan=3, pady=5, sticky="new")
                    new_password_label = ctk.CTkLabel(FramenovaSenha, text="Nova Senha:")
                    new_password_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
                    new_password_entry = ctk.CTkEntry(FramenovaSenha, width=300, show="*")
                    new_password_entry.grid(row=0, column=1, padx=10, pady=5, sticky="e")
                    confirm_password_label = ctk.CTkLabel(FramenovaSenha, text="Repita a nova senha:")
                    confirm_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
                    confirm_password_entry = ctk.CTkEntry(FramenovaSenha, width=300, show="*")
                    confirm_password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")
                    bt_change_password = ctk.CTkButton(FramenovaSenha, text="Mudar senha", command=change_password)
                    bt_change_password.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="new")


             
                Frameemail.grid_remove()
                framecodigo = ctk.CTkFrame(JanelaSenha)
                framecodigo.grid(row=0, column=0, padx=10,rowspan=3, pady=5, sticky="new")

                lebalCod = ctk.CTkLabel(framecodigo, width=300,text='Insira o codigo')
                lebalCod.grid(row=0, column=0, padx=10, pady=5, sticky="new")

                entryCod = ctk.CTkEntry(framecodigo, width=300)
                entryCod.grid(row=1, column=0, padx=10, pady=5, sticky="new")

                btCod = ctk.CTkButton(framecodigo, width=300,text='Enviar',command=vericação_cod)
                btCod.grid(row=2, column=0, padx=10, pady=5, sticky="new")


        JanelaSenha = ctk.CTkToplevel(janela)
        JanelaSenha.title('Esqueci minha senha')
        
        Frameemail= ctk.CTkFrame(JanelaSenha)
        Frameemail.grid(row=0, column=0, padx=10,rowspan=3, pady=5, sticky="new")

        lebalemail = ctk.CTkLabel(Frameemail, width=300,text='Insira seu E-mail')
        lebalemail.grid(row=0, column=0, padx=10, pady=5, sticky="new")

        entryemail = ctk.CTkEntry(Frameemail, width=300)
        entryemail.grid(row=1, column=0, padx=10, pady=5, sticky="new")

        btemail = ctk.CTkButton(Frameemail, width=300,text='Enviar codigo',command=telacodigo)
        btemail.grid(row=2, column=0, padx=10, pady=5, sticky="new")

        
    def center_window(window, width, height):
        # Obter as dimensões da tela
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Calcular as coordenadas para posicionar a janela no centro
        x = (screen_width - width) // 2
        y = (screen_height - height)  // 2  
        # Definir as coordenadas da janela
        window.geometry(f"{width}x{height}+{x}+{y}") 

    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela():
        janela.geometry(f"{700}x{400}+{0}+{0}") 
        janela.iconbitmap(default='logodatavix.ico')
        #center_window(janela, 700, 400) caso queria que aparece no centro

        janela.title("Sistema de Datavix")
    #janela.iconbitmap("")
        janela.resizable(False,False)

    def tela_login():
        #Função de consulta do banco de dados e validação
        def ConsultaLogin(*args):
            
            email = username_entry.get()
            senha = password_entry.get()

            if email != '' and senha != '':
                global TesteLogin  
                TesteLogin = dbu.VerificaçãoLogin(email,senha)
                
                try: 
                    if TesteLogin[0] == True:
                        TesteLogin
                except Exception:    
                    tamanho =[TesteLogin]
                    if len(tamanho) == 1:
                        TesteLogin = TesteLogin, TesteLogin
                
                if TesteLogin[0] == True:
                    
                    global podelogar
                    podelogar = True                   
                    if podelogar == True:
                       
                       
                  
                        def carregar():
                            global telacarregamento
                            ### tela de carregamento 
                            telacarregamento = tk.Tk()
                            framecarregamento = ttk.Frame(telacarregamento)
                            framecarregamento.pack(side=LEFT,fill=X,expand=True)

                            telacarregamento.overrideredirect(True)

                            center_window(telacarregamento, 100, 100)
               
                            CarregandoLB = ttk.Label(framecarregamento, text="Por favor aguarde\n\nCarregando...\n")

                            CarregandoLB.pack(side=TOP,fill=BOTH,expand=True)
                            barradeprogresso = ttk.Progressbar(framecarregamento)
                            barradeprogresso.pack(side=BOTTOM,fill=BOTH,expand=True)
                            barradeprogresso.configure(mode="indeterminate")
                            barradeprogresso.start()  
                            
                            telacarregamento.mainloop() 
                           
                        Usuario = TesteLogin[1]
                        label_img.place_forget()
                        frame.pack_forget()

                        tread_painel = threading.Thread(target=carregar)
                        #inicia o carregamento da tela do painel datavix
                        tread_painel.start()

                        #destroi a instancia atual do ctk(Não pode ter 2 abertas)
                        janela.destroy() 

                        PD.DataVix(Usuario,telacarregamento)

                        
                        
                else:
                    messagebox.showinfo("Erro", "Login ou senha inválidos")    
                    #erro_senha.place(x=25, y=250)
                    #erro_senha_vazio.place_forget()
                    podelogar = False
                    #Mostrar SPAM com erro 
                    
            else:
                messagebox.showinfo("Erro", "Favor preencher o campo de usuário e senha")    
                #erro_senha_vazio.place(x=25, y=250)
                #erro_senha.place_forget()
                #Mostrar SPAM informando que é obrigatorio preenchimento senha e email
          


    #janela = lado esquerdo
        caminho = Imagens_DataBase.baixarimagemLogoDTV()
        img = PhotoImage(file=caminho)
        label_img = ctk.CTkLabel(master=janela, image=img, text=" ")
        label_img.place(x=35, y=110)
        #label_left = ctk.CTkLabel(master=janela, text="Bem vindo", font=("Roboto", 18), text_color="#9370DB"). place(x=10, y= 10)

    #frame = lado direito
        frame = ctk.CTkFrame(master=janela, width=350, height=396)
        frame.pack(side=RIGHT)


    #frame widgets
        label = ctk.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20)).place(x=25, y=5)


        username_entry = ctk.CTkEntry(master=frame, placeholder_text="Nome de usuario", width=300, font=("Roboto",14))
        username_entry.place(x=25, y=105)
        username_entry.bind('<Return>',ConsultaLogin)
       
        #username_label = ctk.CTkLabel(master=frame, text="*O campo de usuario e de carater obrigatorio.", text_color="red", font=("Roboto", 10)). place(x=25, y= 135)

        password_entry = ctk.CTkEntry(master=frame, placeholder_text="Senha de usuario", width=300, font=("Roboto",14),show="*")
        password_entry.place(x=25, y=175)
        password_entry.bind('<Return>',ConsultaLogin)
        #password_label = ctk.CTkLabel(master=frame, text="*O campo de senha e de carater obrigatorio.", text_color="red", font=("Roboto", 10)). place(x=25, y= 205)
       
        erro_senha = ctk.CTkLabel(master=frame, text="login ou senha inválidos", width=300, text_color="red", font=("Roboto",14))
        #erro_senha.place(x=25, y=250)

        erro_senha_vazio = ctk.CTkLabel(master=frame, text="Favor preencher o campo de usuário e senha", width=300, text_color="red", font=("Roboto",14))
        #erro_senha_vazio.place(x=25, y=250)

        

        
    

    
    #checkbox
    #   
    #  chekbox = ctk.CTkCheckBox(master=frame, text="lembrar-se de mim sempre").place(x=25, y=235)
        
    #botao
        botao_login = ctk.CTkButton(master=frame, text="Login", width=300,command=ConsultaLogin).place(x=25, y= 285)
        primeiro_acesso = ctk.CTkButton(master=frame, text="Esqueci a senha", width=150,command=Redefinirsenha).place(x=175, y=320)
    #span
         
    #    register_button = ctk.CTkButton(master=frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334").place(x=175, y= 325)
    tema()
    tela()
    tela_login()
    janela.mainloop()
    
Vatual = bdp.pegar_parametro('versao_atual')
if Vatual == Versão: 
    TelaLogin()
else:
    # Especifique o caminho relativo para o arquivo EXE
    caminho_do_exe = r'DatavixAPP_Update.exe'

    os.execl(caminho_do_exe,'DatavixAPP.exe',Vatual)    






