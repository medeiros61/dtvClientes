import customtkinter as ctk
from tkinter import *
import DatabaseUsers as dbc

janela = ctk.CTk()

class Application():

    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de login")
    #janela.iconbitmap("")
        janela.resizable(False,False)

    def tela_login(self):
        #Função de consulta do banco de dados e validação
        def ConsultaLogin():
            
            email = username_entry.get()
            senha = password_entry.get()
            if email != '' and senha != '':

                TesteLogin = dbc.VerificaçãoLogin(email,senha)
                if TesteLogin == True:
                    print('passou')
                else:
                    #Mostrar SPAM com erro 
                    print('Não Passou')    
            else:
                #Mostrar SPAM informando que é obrigatorio preenchimento senha e email
                print('não preencheu tudo')


    #janela = lado esquerdo
        img = PhotoImage(file="japan.png")
        label_img = ctk.CTkLabel(master=janela, image=img).place(x=5, y=65)
        label_left = ctk.CTkLabel(master=janela, text="Bem vindo", font=("Roboto", 18), text_color="#9370DB"). place(x=10, y= 10)

    #frame = lado direito
        frame = ctk.CTkFrame(master=janela, width=350, height=396)
        frame.pack(side=RIGHT)


    #frame widgets
        label = ctk.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20)).place(x=25, y=5)


        username_entry = ctk.CTkEntry(master=frame, placeholder_text="Nome de usuario", width=300, font=("Roboto",14))
        username_entry.place(x=25, y=105)
        username_label = ctk.CTkLabel(master=frame, text="*O campo de usuario e de carater obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y= 135)

        password_entry = ctk.CTkEntry(master=frame, placeholder_text="Senha de usuario", width=300, font=("Roboto",14),show="*")
        password_entry.place(x=25, y=175)
        password_label = ctk.CTkLabel(master=frame, text="*O campo de senha e de carater obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y= 205)

    #checkbox
    #    chekbox = ctk.CTkCheckBox(master=frame, text="lembrar-se de mim sempre").place(x=25, y=235)

    #botao
        botao_login = ctk.CTkButton(master=frame, text="LOGIN", width=300,command=ConsultaLogin)
        botao_login.place(x=25, y= 285)

    #span
    #    register_label= ctk.CTkLabel(master=frame, text="Se ainda nao tem\n uma conta.").place(x=25, y=325)
    #    register_button = ctk.CTkButton(master=frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334").place(x=175, y= 325)
    
        


Application()




