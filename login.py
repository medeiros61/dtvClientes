import customtkinter as ctk
from tkinter import *
import Modulos.Database.Users as dbu
import PainelDatavix as PD
import Modulos.imagens.ImagensClientes as Imagens_DataBase
import threading
import tkinter as tk
from tkinter import ttk

janela = ctk.CTk()


podelogar = False
def TelaLogin():

        
    
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela():
        janela.geometry("700x400")
        janela.title("Sistema de Datavix")
    #janela.iconbitmap("")
        janela.resizable(False,False)

    def tela_login():
        #Função de consulta do banco de dados e validação
        def ConsultaLogin():
            
            email = username_entry.get()
            senha = password_entry.get()

            if email != '' and senha != '':
                global TesteLogin  
                TesteLogin = dbu.VerificaçãoLogin(email,senha)
                
                try: 
                    if TesteLogin[0] == True:
                        print('\n')
                except Exception:    
                    tamanho =[TesteLogin]
                    if len(tamanho) == 1:
                        TesteLogin = TesteLogin, TesteLogin
                
                if TesteLogin[0] == True:
                    print('passou')
                    global podelogar
                    podelogar = True                   
                    if podelogar == True:
                        Usuario = TesteLogin[1]
                        label_img.place_forget()
                        frame.pack_forget()
                       
                        
                        def carregar():
                            global telacarregamento
                            ### tela de carregamento 
                            telacarregamento = tk.Tk()
                            framecarregamento = ttk.Frame(telacarregamento)
                            framecarregamento.pack(side=LEFT,fill=BOTH,expand=True)
                            barradeprogresso = ttk.Progressbar(framecarregamento)
                            barradeprogresso.pack(side=TOP,fill=BOTH,expand=True)
                            barradeprogresso.configure(mode="indeterminate")
                            barradeprogresso.start()  
                            telacarregamento.mainloop() 
                           

                        tread_painel = threading.Thread(target=carregar)
                        #inicia o carregamento da tela do painel datavix
                        tread_painel.start()

                        #destroi a instancia atual do ctk(Não pode ter 2 abertas)
                        janela.destroy() 

                        PD.DataVix(Usuario,telacarregamento)

                        
                        
                else:
                    erro_senha.place(x=25, y=250)
                    erro_senha_vazio.place_forget()
                    podelogar = False
                    #Mostrar SPAM com erro 
                    print('Não Passou')    
            else:
                erro_senha_vazio.place(x=25, y=250)
                erro_senha.place_forget()
                #Mostrar SPAM informando que é obrigatorio preenchimento senha e email
                print('não preencheu tudo')


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
       
        #username_label = ctk.CTkLabel(master=frame, text="*O campo de usuario e de carater obrigatorio.", text_color="red", font=("Roboto", 10)). place(x=25, y= 135)

        password_entry = ctk.CTkEntry(master=frame, placeholder_text="Senha de usuario", width=300, font=("Roboto",14),show="*")
        password_entry.place(x=25, y=175)
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
        primeiro_acesso = ctk.CTkButton(master=frame, text="Primeiro acesso", width=150).place(x=25, y=340)
    #span
         
    #    register_button = ctk.CTkButton(master=frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334").place(x=175, y= 325)
    tema()
    tela()
    tela_login()
    janela.mainloop()
    


#User
#Usuario : t@teste
#Senha : teste
#pip install openpyxl pandas requests ttkthemes 

#master@datavix.com.br , 1234
#admin@datavix.com.br , 1234

TelaLogin()


