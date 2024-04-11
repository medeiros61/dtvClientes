import loginv2
import customtkinter as ctk
from tkinter import *

def DataVix():
    screen_datavix = ctk.CTkToplevel()
    screen_datavix.geometry("1100x580")
    screen_datavix.title("Master")
    screen_datavix.resizable(False,False)
    username_entry = ctk.CTkEntry(master=screen_datavix, placeholder_text="TESTE", width=300, font=("Roboto",14))
    username_entry.place(x=500, y=200)
    #aba
    options_frame = ctk.CTkFrame(master=screen_datavix, width=200, height=580, fg_color=("#808080"))
    options_frame.pack(side=LEFT)
    options_frame.pack_propagate(False)
    #buttons
    botao_dashboard = ctk.CTkButton(master=options_frame, text="DASHBOARD")
    botao_dashboard.place(x=32, y=250)

    botao_clientes = ctk.CTkButton(master=options_frame, text="CLIENTES")
    botao_clientes.place(x=32, y=300)

    botao_MEI = ctk.CTkButton(master=options_frame, text="CONTROLE MEis")
    botao_MEI.place(x=32, y=350)

    botao_usuarios = ctk.CTkButton(master=options_frame, text="USUARIOS")
    botao_usuarios.place(x=32, y=400)

    botao_sair = ctk.CTkButton(master=options_frame, text="SAIR")
    botao_sair.place(x=32, y=450)
#---------------------------------------------------------------------------------#