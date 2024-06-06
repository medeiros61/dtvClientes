from tkinter import *
import Modulos.Usuarios.Tela_Cadastro as TelaC
import Modulos.Cliente.Botoes_Edicao as btedit
#FUNÇÃO PARA ADICIONAR
def AdicionarUsuario(Frame):
    TelaC.CriarTelaCadatro(Frame)



#FUNÇÃO PARA EDITAR
def editar_Usuario(TreeView,Frame):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                nome = valores[1] 
                Email = valores[2] 
                role = valores[4] 
                TelaC.EditarEmailOuNome(Frame,nome,Email,role)
            else:
                print("Nenhum cliente selecionado.")

