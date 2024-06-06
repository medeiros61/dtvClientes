import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import Modulos.Database.Users as dbu
import PainelDatavix as pd
import Modulos.Database.Logs as log

def CriarTelaCadatro(FrameOriginal):
    def verificar_e_Cadastrar():
        Nome = Entry_Nome.get()
        Email = Entry_Email.get()
        Tipo = Tipos_VAR.get()
        if Nome =='' or Email =='':
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            dbu.Criar_Usuario(Nome, Email, Tipo)
            JanelaCadatro.destroy()
            log.RegistrarEventosdeLOG(f'Cadastro de um novo usuario',f'Novo Usuario: {Nome} , {Email} , {Tipo}') 
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso")



    cor_de_borda = "gray50"
    largura_borda = 2

    JanelaCadatro = ctk.CTkToplevel(FrameOriginal)
    JanelaCadatro.title("Cadastro de Usuário")
    JanelaCadatro.geometry("400x400")

    FrameCampos = ctk.CTkFrame(JanelaCadatro, border_width=largura_borda, border_color=cor_de_borda)
    FrameCampos.pack(pady=5,padx=5,expand=True,fill=X,side=TOP)
    
    Label_Nome = ctk.CTkLabel(FrameCampos,text="Nome",anchor='w')
    Label_Nome.pack(pady=10,padx=10,fill=X, expand=True)

    Entry_Nome = ctk.CTkEntry(FrameCampos)
    Entry_Nome.pack(pady=10,padx=10,fill=X, expand=True)

    Label_Email = ctk.CTkLabel(FrameCampos,text="Email",anchor='w')
    Label_Email.pack(pady=10,padx=10,fill=X, expand=True)

    Entry_Email = ctk.CTkEntry(FrameCampos)
    Entry_Email.pack(pady=10,padx=10,fill=X, expand=True)

    Label_Tipo = ctk.CTkLabel(FrameCampos,text="Tipo",anchor='w')
    Label_Tipo.pack(pady=10,padx=10,fill=X, expand=True)

    Tipos = ['user','admin']
    Tipos_VAR = ctk.StringVar(value="user")
   

    Entry_Tipo = ctk.CTkComboBox(FrameCampos,values=Tipos,variable=Tipos_VAR)
    Entry_Tipo.pack(pady=10,padx=10,fill=X, expand=True)

    FrameCampos = ctk.CTkButton(JanelaCadatro, text='Cadastrar',command=verificar_e_Cadastrar)
    FrameCampos.pack(pady=5,padx=5,expand=True,fill=X,side=BOTTOM)

    
def EditarEmailOuNome(FrameOriginal,nome_atual,email_atual,role):
    def verificar_e_Cadastrar():
        Nome = Entry_Nome.get()
        Email = Entry_Email.get()
        perfil = Tipos_VAR.get()
        if Nome =='' or Email =='':
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            dbu.AlterarNomeEmail(Nome, Email,email_atual,perfil)
            JanelaCadatro.destroy()
            
            log.RegistrarEventosdeLOG(f'Atualização de Usuario ({nome_atual},{email_atual},{role})',f'Atualizado para {Nome} , {Email} , {perfil} ') 
            messagebox.showinfo("Sucesso", "Atualização realizado com sucesso")

            



    cor_de_borda = "gray50"
    largura_borda = 2

    JanelaCadatro = ctk.CTkToplevel(FrameOriginal)
    JanelaCadatro.title("Edição de Usuário")
    JanelaCadatro.geometry("400x400")

    FrameCampos = ctk.CTkFrame(JanelaCadatro, border_width=largura_borda, border_color=cor_de_borda)
    FrameCampos.pack(pady=5,padx=5,expand=True,fill=X,side=TOP)
    
    Label_Nome = ctk.CTkLabel(FrameCampos,text="Nome",anchor='w')
    Label_Nome.pack(pady=10,padx=10,fill=X, expand=True)
    
    Entry_Nome = ctk.CTkEntry(FrameCampos)
    Entry_Nome.pack(pady=10,padx=10,fill=X, expand=True)
    Entry_Nome.insert(0,f'{nome_atual}')

    Label_Email = ctk.CTkLabel(FrameCampos,text="Email",anchor='w')
    Label_Email.pack(pady=10,padx=10,fill=X, expand=True)

    Entry_Email = ctk.CTkEntry(FrameCampos)
    Entry_Email.pack(pady=10,padx=10,fill=X, expand=True)
    Entry_Email.insert(0,f'{email_atual}')

    Label_Tipo = ctk.CTkLabel(FrameCampos,text="Tipo",anchor='w')
    

    Tipos = ['user','admin']
    Tipos_VAR = ctk.StringVar(value=f"{role}")
   

    Entry_Tipo = ctk.CTkComboBox(FrameCampos,values=Tipos,variable=Tipos_VAR)
    
    Dados_Usuario = pd.InfoUser()
    tipo= Dados_Usuario[2]

    if tipo =='user':
        pass
    
    if tipo =='admin' or tipo =='master':
        Label_Tipo.pack(pady=10,padx=10,fill=X, expand=True)
        Entry_Tipo.pack(pady=10,padx=10,fill=X, expand=True)


    FrameCampos = ctk.CTkButton(JanelaCadatro, text='Salvar Edição',command=verificar_e_Cadastrar)
    FrameCampos.pack(pady=5,padx=5,expand=True,fill=X,side=BOTTOM)
   
   