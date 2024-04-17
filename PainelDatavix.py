import customtkinter as ctk
from tkinter import *
import cliente as cl
import mei as me
import usuarios as user
import imagens.ImagensClientes as Imagens_DataBase


def DataVix():
    

    screen_datavix = ctk.CTk()
    screen_datavix.geometry("1150x615")
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

    def ativarmei():
        me.criartelaMEI(frame_mei)
        cl.Removertelaclientes(frame_clientes)
        user.Removertelauser(frame_user)
    def ativarclientes():
        cl.criartelaclientes(frame_clientes)
        me.RemovertelaMEI(frame_mei)
        user.Removertelauser(frame_user)
    def ativaruser():
        user.criartelauser(frame_user)
        me.RemovertelaMEI(frame_mei)
        cl.Removertelaclientes(frame_clientes)
    def exit():
        screen_datavix.destroy()    

    #aba
    options_frame = ctk.CTkFrame(master=screen_datavix, width=200, height=580, fg_color=("#808080"))
    options_frame.pack(side=LEFT, fill = Y) 
    #options_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
    #options_frame.pack_propagate(False)
    #logo datavix
    caminho = Imagens_DataBase.baixarimagemLogoDTV()
    logo_datavix = PhotoImage(file=caminho)
    botao_logo = ctk.CTkButton(master=options_frame, image=logo_datavix, text="", fg_color="#808080")
    botao_logo.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")
    botao_logo.configure(state="disabled")
    
    #buttons
    botao_dashboard = ctk.CTkButton(master=options_frame, text="DASHBOARD")
    botao_dashboard.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")

    botao_clientes = ctk.CTkButton(master=options_frame, text="CLIENTES",command=ativarclientes)
    botao_clientes.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="nsew")
    botao_clientes.configure(state="normal")

    botao_MEI = ctk.CTkButton(master=options_frame, text="CONTROLE MEis", command=ativarmei)
    botao_MEI.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="nsew")

    botao_usuarios = ctk.CTkButton(master=options_frame, text="USUARIOS", command=ativaruser)
    botao_usuarios.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="nsew")

    botao_sair = ctk.CTkButton(master=options_frame, text="SAIR", command=exit)
    botao_sair.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="nsew")
    screen_datavix.mainloop()
#---------------------------------------------------------------------------------#


DataVix()