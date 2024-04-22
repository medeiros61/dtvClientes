import customtkinter as ctk
from tkinter import *
import tela as tl

window_login = ctk.CTk()
window_login.geometry("500x300")
window_login.resizable(False,False)
window_login.title("Login")


texto = ctk.CTkLabel(window_login, text="Fazer login")
texto.pack(padx=10, pady=10)

login = ctk.CTkEntry(window_login, placeholder_text="Login")
login.pack(padx=10, pady=10)

senha = ctk.CTkEntry(window_login, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(window_login, text="Entrar", command=tl.DataVix)
botao.pack(padx=10, pady=10)











window_login.mainloop()