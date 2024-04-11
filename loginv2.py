import customtkinter as ctk

window_login = ctk.CTk()
window_login.geometry("500x300")
window_login.resizable


def DataVix():
    screen_datavix = ctk.CTkToplevel()
    screen_datavix.geometry("1100x580")
    


texto = ctk.CTkLabel(window_login, text="Fazer login")
texto.pack(padx=10, pady=10)

login = ctk.CTkEntry(window_login, placeholder_text="Login")
login.pack(padx=10, pady=10)

senha = ctk.CTkEntry(window_login, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(window_login, text="Entrar", command=DataVix)
botao.pack(padx=10, pady=10)

window_login.mainloop()